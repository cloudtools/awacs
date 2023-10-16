# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Textract"
prefix = "textract"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AnalyzeDocument = Action("AnalyzeDocument")
AnalyzeExpense = Action("AnalyzeExpense")
AnalyzeID = Action("AnalyzeID")
CreateAdapter = Action("CreateAdapter")
CreateAdapterVersion = Action("CreateAdapterVersion")
DeleteAdapter = Action("DeleteAdapter")
DeleteAdapterVersion = Action("DeleteAdapterVersion")
DetectDocumentText = Action("DetectDocumentText")
GetAdapter = Action("GetAdapter")
GetAdapterVersion = Action("GetAdapterVersion")
GetDocumentAnalysis = Action("GetDocumentAnalysis")
GetDocumentTextDetection = Action("GetDocumentTextDetection")
GetExpenseAnalysis = Action("GetExpenseAnalysis")
GetLendingAnalysis = Action("GetLendingAnalysis")
GetLendingAnalysisSummary = Action("GetLendingAnalysisSummary")
ListAdapterVersions = Action("ListAdapterVersions")
ListAdapters = Action("ListAdapters")
ListTagsForResource = Action("ListTagsForResource")
StartDocumentAnalysis = Action("StartDocumentAnalysis")
StartDocumentTextDetection = Action("StartDocumentTextDetection")
StartExpenseAnalysis = Action("StartExpenseAnalysis")
StartLendingAnalysis = Action("StartLendingAnalysis")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAdapter = Action("UpdateAdapter")
