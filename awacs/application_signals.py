# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon CloudWatch Application Signals"
prefix = "application-signals"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchGetServiceLevelObjectiveBudgetReport = Action(
    "BatchGetServiceLevelObjectiveBudgetReport"
)
CreateServiceLevelObjective = Action("CreateServiceLevelObjective")
DeleteServiceLevelObjective = Action("DeleteServiceLevelObjective")
GetService = Action("GetService")
GetServiceLevelObjective = Action("GetServiceLevelObjective")
ListObservedEntities = Action("ListObservedEntities")
ListServiceDependencies = Action("ListServiceDependencies")
ListServiceDependents = Action("ListServiceDependents")
ListServiceLevelObjectives = Action("ListServiceLevelObjectives")
ListServiceOperations = Action("ListServiceOperations")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
StartDiscovery = Action("StartDiscovery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateServiceLevelObjective = Action("UpdateServiceLevelObjective")
