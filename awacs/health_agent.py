# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect Health"
prefix = "health-agent"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateSubscription = Action("ActivateSubscription")
CancelAppointment = Action("CancelAppointment")
CreateAgent = Action("CreateAgent")
CreateDomain = Action("CreateDomain")
CreateIntegration = Action("CreateIntegration")
CreateSession = Action("CreateSession")
CreateSubscription = Action("CreateSubscription")
DeactivateSubscription = Action("DeactivateSubscription")
DeleteAgent = Action("DeleteAgent")
DeleteDomain = Action("DeleteDomain")
DeleteIntegration = Action("DeleteIntegration")
GetAgent = Action("GetAgent")
GetCareTeamProvider = Action("GetCareTeamProvider")
GetDomain = Action("GetDomain")
GetIntegration = Action("GetIntegration")
GetMedicalScribeListeningSession = Action("GetMedicalScribeListeningSession")
GetPatient = Action("GetPatient")
GetPatientInsightsJob = Action("GetPatientInsightsJob")
GetPractitioner = Action("GetPractitioner")
GetSessionContext = Action("GetSessionContext")
GetSubscription = Action("GetSubscription")
InvokeAgent = Action("InvokeAgent")
ListAgents = Action("ListAgents")
ListAppointmentSlots = Action("ListAppointmentSlots")
ListDomains = Action("ListDomains")
ListIntegrations = Action("ListIntegrations")
ListPatientAppointments = Action("ListPatientAppointments")
ListPatientInsuranceCoverages = Action("ListPatientInsuranceCoverages")
ListProviders = Action("ListProviders")
ListSubscriptions = Action("ListSubscriptions")
ListTagsForResource = Action("ListTagsForResource")
MatchPatient = Action("MatchPatient")
PublishAgent = Action("PublishAgent")
RescheduleAppointment = Action("RescheduleAppointment")
ScheduleAppointment = Action("ScheduleAppointment")
StartMedicalScribeListeningSession = Action("StartMedicalScribeListeningSession")
StartPatientInsightsJob = Action("StartPatientInsightsJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateIntegration = Action("UpdateIntegration")
UpdateSession = Action("UpdateSession")
