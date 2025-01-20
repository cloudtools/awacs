# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Supply Chain"
prefix = "scn"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssignAdminPermissionsToUser = Action("AssignAdminPermissionsToUser")
CreateBillOfMaterialsImportJob = Action("CreateBillOfMaterialsImportJob")
CreateDataIntegrationFlow = Action("CreateDataIntegrationFlow")
CreateDataLakeDataset = Action("CreateDataLakeDataset")
CreateInstance = Action("CreateInstance")
CreateSSOApplication = Action("CreateSSOApplication")
DeleteDataIntegrationFlow = Action("DeleteDataIntegrationFlow")
DeleteDataLakeDataset = Action("DeleteDataLakeDataset")
DeleteInstance = Action("DeleteInstance")
DeleteSSOApplication = Action("DeleteSSOApplication")
DescribeInstance = Action("DescribeInstance")
GetBillOfMaterialsImportJob = Action("GetBillOfMaterialsImportJob")
GetDataIntegrationFlow = Action("GetDataIntegrationFlow")
GetDataLakeDataset = Action("GetDataLakeDataset")
GetInstance = Action("GetInstance")
ListAdminUsers = Action("ListAdminUsers")
ListDataIntegrationFlows = Action("ListDataIntegrationFlows")
ListDataLakeDatasets = Action("ListDataLakeDatasets")
ListInstances = Action("ListInstances")
ListTagsForResource = Action("ListTagsForResource")
RemoveAdminPermissionsForUser = Action("RemoveAdminPermissionsForUser")
SendDataIntegrationEvent = Action("SendDataIntegrationEvent")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataIntegrationFlow = Action("UpdateDataIntegrationFlow")
UpdateDataLakeDataset = Action("UpdateDataLakeDataset")
UpdateInstance = Action("UpdateInstance")
