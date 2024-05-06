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


AssociateQAppWithUser = Action("AssociateQAppWithUser")
CopyQApp = Action("CopyQApp")
CreateLibraryItem = Action("CreateLibraryItem")
CreateLibraryItemReview = Action("CreateLibraryItemReview")
CreateQApp = Action("CreateQApp")
CreateSubscriptionToken = Action("CreateSubscriptionToken")
DeleteLibraryItem = Action("DeleteLibraryItem")
DeleteQApp = Action("DeleteQApp")
DisassociateQAppFromUser = Action("DisassociateQAppFromUser")
GetLibraryItem = Action("GetLibraryItem")
GetQApp = Action("GetQApp")
ImportDocumentToQApp = Action("ImportDocumentToQApp")
ImportDocumentToQAppSession = Action("ImportDocumentToQAppSession")
ListLibraryItems = Action("ListLibraryItems")
ListQApps = Action("ListQApps")
PredictProblemStatementFromConversation = Action(
    "PredictProblemStatementFromConversation"
)
PredictQAppFromProblemStatement = Action("PredictQAppFromProblemStatement")
StartQAppSession = Action("StartQAppSession")
StopQAppSession = Action("StopQAppSession")
UpdateLibraryItem = Action("UpdateLibraryItem")
UpdateQApp = Action("UpdateQApp")
