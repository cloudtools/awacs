# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Manage Amazon API Gateway"
prefix = "apigateway"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DELETE = Action("DELETE")
GET = Action("GET")
HEAD = Action("HEAD")
OPTIONS = Action("OPTIONS")
PATCH = Action("PATCH")
POST = Action("POST")
PUT = Action("PUT")
SetWebACL = Action("SetWebACL")
UpdateRestApiPolicy = Action("UpdateRestApiPolicy")
