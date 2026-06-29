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


BatchDeleteInstrumentationConfigurations = Action(
    "BatchDeleteInstrumentationConfigurations"
)
BatchGetServiceLevelObjectiveBudgetReport = Action(
    "BatchGetServiceLevelObjectiveBudgetReport"
)
BatchUpdateExclusionWindows = Action("BatchUpdateExclusionWindows")
CreateInstrumentationConfiguration = Action("CreateInstrumentationConfiguration")
CreateServiceLevelObjective = Action("CreateServiceLevelObjective")
DeleteGroupingConfiguration = Action("DeleteGroupingConfiguration")
DeleteInstrumentationConfiguration = Action("DeleteInstrumentationConfiguration")
DeleteServiceLevelObjective = Action("DeleteServiceLevelObjective")
GetInstrumentationConfiguration = Action("GetInstrumentationConfiguration")
GetInstrumentationConfigurationStatus = Action("GetInstrumentationConfigurationStatus")
GetService = Action("GetService")
GetServiceLevelObjective = Action("GetServiceLevelObjective")
Link = Action("Link")
ListAuditFindings = Action("ListAuditFindings")
ListEntityEvents = Action("ListEntityEvents")
ListGroupingAttributeDefinitions = Action("ListGroupingAttributeDefinitions")
ListInstrumentationConfigurations = Action("ListInstrumentationConfigurations")
ListObservedEntities = Action("ListObservedEntities")
ListServiceDependencies = Action("ListServiceDependencies")
ListServiceDependents = Action("ListServiceDependents")
ListServiceLevelObjectiveExclusionWindows = Action(
    "ListServiceLevelObjectiveExclusionWindows"
)
ListServiceLevelObjectives = Action("ListServiceLevelObjectives")
ListServiceOperations = Action("ListServiceOperations")
ListServiceStates = Action("ListServiceStates")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
PutGroupingConfiguration = Action("PutGroupingConfiguration")
ReportInstrumentationConfigurationStatus = Action(
    "ReportInstrumentationConfigurationStatus"
)
StartDiscovery = Action("StartDiscovery")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateServiceLevelObjective = Action("UpdateServiceLevelObjective")
