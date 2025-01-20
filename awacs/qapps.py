# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Q Business Q Apps"
prefix = "qapps"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateLibraryItemReview = Action("AssociateLibraryItemReview")
AssociateQAppWithUser = Action("AssociateQAppWithUser")
BatchCreateCategory = Action("BatchCreateCategory")
BatchDeleteCategory = Action("BatchDeleteCategory")
BatchUpdateCategory = Action("BatchUpdateCategory")
CopyQApp = Action("CopyQApp")
CreateLibraryItem = Action("CreateLibraryItem")
CreateLibraryItemReview = Action("CreateLibraryItemReview")
CreatePresignedUrl = Action("CreatePresignedUrl")
CreateQApp = Action("CreateQApp")
CreateSubscriptionToken = Action("CreateSubscriptionToken")
DeleteLibraryItem = Action("DeleteLibraryItem")
DeleteQApp = Action("DeleteQApp")
DescribeQAppPermissions = Action("DescribeQAppPermissions")
DisassociateLibraryItemReview = Action("DisassociateLibraryItemReview")
DisassociateQAppFromUser = Action("DisassociateQAppFromUser")
ExportQAppSessionData = Action("ExportQAppSessionData")
GetLibraryItem = Action("GetLibraryItem")
GetQApp = Action("GetQApp")
GetQAppSession = Action("GetQAppSession")
GetQAppSessionMetadata = Action("GetQAppSessionMetadata")
ImportDocument = Action("ImportDocument")
ImportDocumentToQApp = Action("ImportDocumentToQApp")
ImportDocumentToQAppSession = Action("ImportDocumentToQAppSession")
ListCategories = Action("ListCategories")
ListLibraryItems = Action("ListLibraryItems")
ListQAppSessionData = Action("ListQAppSessionData")
ListQApps = Action("ListQApps")
ListTagsForResource = Action("ListTagsForResource")
PredictProblemStatementFromConversation = Action(
    "PredictProblemStatementFromConversation"
)
PredictQApp = Action("PredictQApp")
PredictQAppFromProblemStatement = Action("PredictQAppFromProblemStatement")
StartQAppSession = Action("StartQAppSession")
StopQAppSession = Action("StopQAppSession")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateLibraryItem = Action("UpdateLibraryItem")
UpdateLibraryItemMetadata = Action("UpdateLibraryItemMetadata")
UpdateQApp = Action("UpdateQApp")
UpdateQAppPermissions = Action("UpdateQAppPermissions")
UpdateQAppSession = Action("UpdateQAppSession")
UpdateQAppSessionMetadata = Action("UpdateQAppSessionMetadata")
