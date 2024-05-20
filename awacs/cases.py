# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Cases"
prefix = "cases"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetField = Action("BatchGetField")
BatchPutFieldOptions = Action("BatchPutFieldOptions")
CreateCase = Action("CreateCase")
CreateDomain = Action("CreateDomain")
CreateField = Action("CreateField")
CreateLayout = Action("CreateLayout")
CreateRelatedItem = Action("CreateRelatedItem")
CreateTemplate = Action("CreateTemplate")
DeleteDomain = Action("DeleteDomain")
DeleteField = Action("DeleteField")
DeleteLayout = Action("DeleteLayout")
DeleteRelatedItem = Action("DeleteRelatedItem")
DeleteTemplate = Action("DeleteTemplate")
GetCase = Action("GetCase")
GetCaseAuditEvents = Action("GetCaseAuditEvents")
GetCaseEventConfiguration = Action("GetCaseEventConfiguration")
GetDomain = Action("GetDomain")
GetLayout = Action("GetLayout")
GetTemplate = Action("GetTemplate")
ListCasesForContact = Action("ListCasesForContact")
ListDomains = Action("ListDomains")
ListFieldOptions = Action("ListFieldOptions")
ListFields = Action("ListFields")
ListLayouts = Action("ListLayouts")
ListTagsForResource = Action("ListTagsForResource")
ListTemplates = Action("ListTemplates")
PutCaseEventConfiguration = Action("PutCaseEventConfiguration")
SearchCases = Action("SearchCases")
SearchRelatedItems = Action("SearchRelatedItems")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCase = Action("UpdateCase")
UpdateField = Action("UpdateField")
UpdateLayout = Action("UpdateLayout")
UpdateTemplate = Action("UpdateTemplate")
