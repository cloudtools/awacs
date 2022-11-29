# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS DeepLens"
prefix = "deeplens"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateServiceRoleToAccount = Action("AssociateServiceRoleToAccount")
BatchGetDevice = Action("BatchGetDevice")
BatchGetModel = Action("BatchGetModel")
BatchGetProject = Action("BatchGetProject")
CreateDeviceCertificates = Action("CreateDeviceCertificates")
CreateModel = Action("CreateModel")
CreateProject = Action("CreateProject")
DeleteModel = Action("DeleteModel")
DeleteProject = Action("DeleteProject")
DeployProject = Action("DeployProject")
DeregisterDevice = Action("DeregisterDevice")
GetAssociatedResources = Action("GetAssociatedResources")
GetDeploymentStatus = Action("GetDeploymentStatus")
GetDevice = Action("GetDevice")
GetModel = Action("GetModel")
GetProject = Action("GetProject")
ImportProjectFromTemplate = Action("ImportProjectFromTemplate")
ListDeployments = Action("ListDeployments")
ListDevices = Action("ListDevices")
ListModels = Action("ListModels")
ListProjects = Action("ListProjects")
RegisterDevice = Action("RegisterDevice")
RemoveProject = Action("RemoveProject")
UpdateProject = Action("UpdateProject")
