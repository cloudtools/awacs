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
CreateDataLakeNamespace = Action("CreateDataLakeNamespace")
CreateInstance = Action("CreateInstance")
CreateSSOApplication = Action("CreateSSOApplication")
DeleteDataIntegrationFlow = Action("DeleteDataIntegrationFlow")
DeleteDataLakeDataset = Action("DeleteDataLakeDataset")
DeleteDataLakeNamespace = Action("DeleteDataLakeNamespace")
DeleteInstance = Action("DeleteInstance")
DeleteSSOApplication = Action("DeleteSSOApplication")
DescribeInstance = Action("DescribeInstance")
GetBillOfMaterialsImportJob = Action("GetBillOfMaterialsImportJob")
GetDataIntegrationEvent = Action("GetDataIntegrationEvent")
GetDataIntegrationFlow = Action("GetDataIntegrationFlow")
GetDataIntegrationFlowExecution = Action("GetDataIntegrationFlowExecution")
GetDataLakeDataset = Action("GetDataLakeDataset")
GetDataLakeNamespace = Action("GetDataLakeNamespace")
GetInstance = Action("GetInstance")
ListAdminUsers = Action("ListAdminUsers")
ListDataIntegrationEvents = Action("ListDataIntegrationEvents")
ListDataIntegrationFlowExecutions = Action("ListDataIntegrationFlowExecutions")
ListDataIntegrationFlows = Action("ListDataIntegrationFlows")
ListDataLakeDatasets = Action("ListDataLakeDatasets")
ListDataLakeNamespaces = Action("ListDataLakeNamespaces")
ListInstances = Action("ListInstances")
ListTagsForResource = Action("ListTagsForResource")
RemoveAdminPermissionsForUser = Action("RemoveAdminPermissionsForUser")
SendDataIntegrationEvent = Action("SendDataIntegrationEvent")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataIntegrationFlow = Action("UpdateDataIntegrationFlow")
UpdateDataLakeDataset = Action("UpdateDataLakeDataset")
UpdateDataLakeNamespace = Action("UpdateDataLakeNamespace")
UpdateInstance = Action("UpdateInstance")
