# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Private CA Connector for SCEP"
prefix = "pca-connector-scep"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateChallenge = Action("CreateChallenge")
CreateConnector = Action("CreateConnector")
DeleteChallenge = Action("DeleteChallenge")
DeleteConnector = Action("DeleteConnector")
GetChallengeMetadata = Action("GetChallengeMetadata")
GetChallengePassword = Action("GetChallengePassword")
GetConnector = Action("GetConnector")
ListChallengeMetadata = Action("ListChallengeMetadata")
ListConnectors = Action("ListConnectors")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
