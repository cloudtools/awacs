# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Security Agent"
prefix = "securityagent"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddArtifact = Action("AddArtifact")
AddControl = Action("AddControl")
BatchDeletePentests = Action("BatchDeletePentests")
BatchGetAgentInstances = Action("BatchGetAgentInstances")
BatchGetArtifactMetadata = Action("BatchGetArtifactMetadata")
BatchGetFindings = Action("BatchGetFindings")
BatchGetPentestJobs = Action("BatchGetPentestJobs")
BatchGetPentests = Action("BatchGetPentests")
BatchGetSecurityTestContentMetadata = Action("BatchGetSecurityTestContentMetadata")
BatchGetTasks = Action("BatchGetTasks")
CreateAgentInstance = Action("CreateAgentInstance")
CreateApplication = Action("CreateApplication")
CreateDocumentReview = Action("CreateDocumentReview")
CreateIntegration = Action("CreateIntegration")
CreateMembership = Action("CreateMembership")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
CreatePentest = Action("CreatePentest")
DeleteAgentInstance = Action("DeleteAgentInstance")
DeleteApplication = Action("DeleteApplication")
DeleteArtifact = Action("DeleteArtifact")
DeleteControl = Action("DeleteControl")
DeleteIntegration = Action("DeleteIntegration")
DeleteMembership = Action("DeleteMembership")
DescribeFindings = Action("DescribeFindings")
GetApplication = Action("GetApplication")
GetArtifact = Action("GetArtifact")
GetCodeReviewTask = Action("GetCodeReviewTask")
GetControl = Action("GetControl")
GetDocReviewTask = Action("GetDocReviewTask")
GetDocumentReview = Action("GetDocumentReview")
GetDocumentReviewArtifact = Action("GetDocumentReviewArtifact")
GetIntegration = Action("GetIntegration")
GetLoginSessionCredentials = Action("GetLoginSessionCredentials")
HandleOneTimeLoginSession = Action("HandleOneTimeLoginSession")
InitiateProviderRegistration = Action("InitiateProviderRegistration")
ListAgentInstanceTasks = Action("ListAgentInstanceTasks")
ListAgentInstances = Action("ListAgentInstances")
ListApplications = Action("ListApplications")
ListArtifacts = Action("ListArtifacts")
ListControls = Action("ListControls")
ListDiscoveredEndpoints = Action("ListDiscoveredEndpoints")
ListDocumentReviewComments = Action("ListDocumentReviewComments")
ListDocumentReviews = Action("ListDocumentReviews")
ListFindings = Action("ListFindings")
ListIntegratedResources = Action("ListIntegratedResources")
ListIntegrations = Action("ListIntegrations")
ListMemberships = Action("ListMemberships")
ListPentestJobsForPentest = Action("ListPentestJobsForPentest")
ListPentests = Action("ListPentests")
ListResourcesFromIntegration = Action("ListResourcesFromIntegration")
ListTasks = Action("ListTasks")
StartCodeRemediation = Action("StartCodeRemediation")
StartPentestExecution = Action("StartPentestExecution")
StopPentestExecution = Action("StopPentestExecution")
ToggleManagedControl = Action("ToggleManagedControl")
UpdateAgentInstance = Action("UpdateAgentInstance")
UpdateApplication = Action("UpdateApplication")
UpdateControl = Action("UpdateControl")
UpdateFinding = Action("UpdateFinding")
UpdateIntegratedResources = Action("UpdateIntegratedResources")
UpdatePentest = Action("UpdatePentest")
VerifyTargetDomain = Action("VerifyTargetDomain")
