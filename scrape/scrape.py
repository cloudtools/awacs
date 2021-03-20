#!/usr/bin/env python3
import asyncio
import importlib
import sys
import urllib.parse
from pathlib import Path
from typing import DefaultDict, Dict, List, Set, Tuple

import aiofiles
import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://docs.aws.amazon.com/IAM/latest/UserGuide/"

HEADER = """\
# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN
"""

CLASSES = """\
class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)
"""

CLASSES_S3 = """\
class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        # account is empty for S3
        account = ''
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)
"""

LEGACY_ARN_CLASS = """\
class {upper}_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super({upper}_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use {lower}.ARN instead.",
                      FutureWarning)
"""

LEGACY_ARNS = ["iam", "s3", "sdb", "sns", "sqs"]

BASEDIR = "awacs"

IGNORED_SERVICE_ALIASES = {
    "Amazon Kinesis Analytics V2": "kinesisanalytics",
    "Amazon Lex V2": "lex",
    "Amazon Pinpoint Email Service": "ses",
    "Amazon Simple Email Service v2": "ses",
    "AWS IoT Greengrass V2": "greengrass",
    "AWS Marketplace Catalog": "aws-marketplace",
    "AWS Marketplace Entitlement Service": "aws-marketplace",
    "AWS Marketplace Image Building Service": "aws-marketplace",
    "AWS Marketplace Metering Service": "aws-marketplace",
    "AWS Marketplace Procurement Systems Integration": "aws-marketplace",
    "AWS Private Marketplace": "aws-marketplace",
    "Elastic Load Balancing V2": "elasticloadbalancing",
}

RENAME_SERVICE = {
    "lambda": "awslambda",
}


def rename_service(name):
    return RENAME_SERVICE.get(name, name)


async def main() -> None:
    services_with_actions: DefaultDict[str, Set[str]] = DefaultDict(set)
    service_names: Dict[str, str] = {}
    service_page_responses = await collect_service_info()

    for r in service_page_responses:
        service_name, service_prefix, actions = await extract_actions(
            html=r.text
        )
        services_with_actions[service_prefix].update(actions)

        if IGNORED_SERVICE_ALIASES.get(service_name) != service_prefix:
            if (
                service_prefix in service_names
                and service_names[service_prefix] != service_name
            ):
                raise ValueError(
                    "Found two different service names for service prefix"
                    f" {service_prefix!r}: {service_names[service_prefix]!r}"
                    f" and {service_name!r}."
                )
            service_names[service_prefix] = service_name

    original_services_with_actions = await collect_existing_actions()
    for service_prefix, actions in services_with_actions.items():
        actions.update(
            original_services_with_actions.get(service_prefix) or set()
        )

    await asyncio.gather(
        *(
            write_service(
                service_prefix, service_names[service_prefix], actions
            )
            for service_prefix, actions in services_with_actions.items()
        )
    )


async def collect_existing_actions() -> Dict[str, Set[str]]:
    # pylint: disable=import-outside-toplevel
    if "" in sys.path:
        sys.path.remove(
            ""
        )  # Import the installed awacs (that was processed by 2to3)

    import awacs
    from awacs.aws import Action as BaseAction

    services_with_actions: DefaultDict[str, Set[str]] = DefaultDict(set)

    for path in (
        path.stem for path in Path(awacs.__file__).parent.glob("*.py")
    ):
        if path.startswith("__"):
            continue
        module = importlib.import_module(f"awacs.{path}")
        for action in vars(module).values():
            if not isinstance(action, BaseAction):
                continue
            services_with_actions[action.prefix].add(action.action)

    return dict(services_with_actions)


async def collect_service_info() -> List[httpx.Response]:
    max_connections = 2
    async with httpx.AsyncClient(
        http2=True,
        limits=httpx.Limits(max_connections=max_connections),
        timeout=10.0,
    ) as client:
        r = await client.get(
            urllib.parse.urljoin(
                BASE_URL,
                "reference_policies_actions-resources-contextkeys.html",
            )
        )
        parsed_html = BeautifulSoup(r.text, features="lxml")

        service_links: List[str] = []
        for link in parsed_html.body.find_all("a"):
            href = link.attrs["href"]
            if href.startswith("./list_") and href.endswith(".html"):
                service_links.append(href)

        # This doesn't work at the moment,
        # see https://github.com/encode/httpx/issues/1171
        #
        # return await asyncio.gather(
        #     *[
        #         client.get(urllib.parse.urljoin(BASE_URL, link))
        #         for link in service_links
        #     ]
        # )
        #
        # workaround
        service_page_responses = []
        for start in range(0, len(service_links), max_connections):
            service_page_responses += await asyncio.gather(
                *[
                    client.get(urllib.parse.urljoin(BASE_URL, link))
                    for link in service_links[start:start + max_connections]
                ]
            )
        return service_page_responses


async def extract_actions(html: str) -> Tuple[str, str, Set[str]]:
    parsed_html = BeautifulSoup(html, features="lxml")
    service_prefixes = parsed_html.body.find_all(is_service_prefix)
    if len(service_prefixes) < 1:
        raise ValueError("Found no service prefix.")
    if len(service_prefixes) > 1:
        raise ValueError("Found more than one service prefix.")

    service_prefix_tag = service_prefixes[0]
    service_name = service_prefix_tag.previous[: -len(" (service prefix: ")]
    service_prefix = service_prefix_tag.text
    actions = set()

    for table in parsed_html.body.find_all("table"):
        header = table.find("th")
        if not header or header.text != "Actions":
            continue
        actions |= await _actions_from_table(table)

    return service_name, service_prefix, actions


async def write_service(
    service_prefix: str, service_name: str, actions: Set[str]
) -> None:
    content: List[str] = []
    if service_prefix in LEGACY_ARNS:
        content.append("import warnings")
    content.append(HEADER)

    content.append(f"service_name = '{service_name}'")
    content.append(f"prefix = '{service_prefix}'")
    content.append("")
    content.append("")
    content.append(CLASSES_S3 if service_prefix == "s3" else CLASSES)
    content.append("")
    if service_prefix in LEGACY_ARNS:
        content.append(
            LEGACY_ARN_CLASS.format(
                lower=service_prefix, upper=service_prefix.upper()
            )
        )
        content.append("")

    for action in sorted(actions):
        action = action.strip()
        # Handle action such as "ReEncrypt*"
        if action[-1] == "*":
            action = action[:-1]
        # Wrap lines for pep8
        if len(action) > 30:
            action_string = "{action} = \\\n    Action('{action}')"
        else:
            action_string = "{action} = Action('{action}')"
        content.append(action_string.format(action=action))

    if content[-1] != "":
        # Add a final newline
        content.append("")

    awacs_service = rename_service(service_prefix.replace("-", "_"))
    filename = "".join([BASEDIR, "/", awacs_service, ".py"])
    async with aiofiles.open(filename, "w") as fp:
        await fp.write("\n".join(content))


async def _actions_from_table(table) -> Set[str]:
    actions = set()
    skip_next_lines = 0
    for table_row in table.find_all("tr"):
        if skip_next_lines:
            skip_next_lines -= 1
            continue
        table_cell = table_row.find("td")
        if not table_cell:
            continue
        skip_next_lines = int(table_cell.attrs.get("rowspan") or 1) - 1
        action: str = (table_cell.text.strip().split() or [""])[0]
        if not action:
            continue
        actions.add(action)
    return actions


def is_service_prefix(tag):
    return (
        tag
        and tag.name == "code"
        and tag.previous_element
        and tag.previous_element.endswith("(service prefix: ")
    )


if __name__ == "__main__":
    asyncio.run(main())
