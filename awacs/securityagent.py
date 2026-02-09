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
BatchGetAgentSpaces = Action("BatchGetAgentSpaces")
BatchGetArtifactMetadata = Action("BatchGetArtifactMetadata")
BatchGetFindings = Action("BatchGetFindings")
BatchGetPentestJobContentMetadata = Action("BatchGetPentestJobContentMetadata")
BatchGetPentestJobTasks = Action("BatchGetPentestJobTasks")
BatchGetPentestJobs = Action("BatchGetPentestJobs")
BatchGetPentests = Action("BatchGetPentests")
BatchGetSecurityTestContentMetadata = Action("BatchGetSecurityTestContentMetadata")
BatchGetTasks = Action("BatchGetTasks")
CreateAgentInstance = Action("CreateAgentInstance")
CreateAgentSpace = Action("CreateAgentSpace")
CreateApplication = Action("CreateApplication")
CreateDesignReview = Action("CreateDesignReview")
CreateDocumentReview = Action("CreateDocumentReview")
CreateIntegration = Action("CreateIntegration")
CreateMembership = Action("CreateMembership")
CreateOneTimeLoginSession = Action("CreateOneTimeLoginSession")
CreatePentest = Action("CreatePentest")
CreateSecurityRequirement = Action("CreateSecurityRequirement")
DeleteAgentInstance = Action("DeleteAgentInstance")
DeleteAgentSpace = Action("DeleteAgentSpace")
DeleteApplication = Action("DeleteApplication")
DeleteArtifact = Action("DeleteArtifact")
DeleteControl = Action("DeleteControl")
DeleteDesignReview = Action("DeleteDesignReview")
DeleteDocumentReview = Action("DeleteDocumentReview")
DeleteIntegration = Action("DeleteIntegration")
DeleteMembership = Action("DeleteMembership")
DeleteSecurityRequirement = Action("DeleteSecurityRequirement")
DescribeFindings = Action("DescribeFindings")
GetApplication = Action("GetApplication")
GetArtifact = Action("GetArtifact")
GetCodeReviewTask = Action("GetCodeReviewTask")
GetControl = Action("GetControl")
GetDesignReview = Action("GetDesignReview")
GetDesignReviewArtifact = Action("GetDesignReviewArtifact")
GetDocReviewTask = Action("GetDocReviewTask")
GetDocumentReview = Action("GetDocumentReview")
GetDocumentReviewArtifact = Action("GetDocumentReviewArtifact")
GetIntegration = Action("GetIntegration")
GetLoginSessionCredentials = Action("GetLoginSessionCredentials")
GetSecurityRequirement = Action("GetSecurityRequirement")
HandleOneTimeLoginSession = Action("HandleOneTimeLoginSession")
InitiateProviderRegistration = Action("InitiateProviderRegistration")
ListAgentInstanceTasks = Action("ListAgentInstanceTasks")
ListAgentInstances = Action("ListAgentInstances")
ListAgentSpaces = Action("ListAgentSpaces")
ListApplications = Action("ListApplications")
ListArtifacts = Action("ListArtifacts")
ListControls = Action("ListControls")
ListDesignReviewComments = Action("ListDesignReviewComments")
ListDesignReviews = Action("ListDesignReviews")
ListDiscoveredEndpoints = Action("ListDiscoveredEndpoints")
ListDocumentReviewComments = Action("ListDocumentReviewComments")
ListDocumentReviews = Action("ListDocumentReviews")
ListFindings = Action("ListFindings")
ListIntegratedResources = Action("ListIntegratedResources")
ListIntegrations = Action("ListIntegrations")
ListMemberships = Action("ListMemberships")
ListPentestJobTasks = Action("ListPentestJobTasks")
ListPentestJobsForPentest = Action("ListPentestJobsForPentest")
ListPentests = Action("ListPentests")
ListResourcesFromIntegration = Action("ListResourcesFromIntegration")
ListSecurityRequirements = Action("ListSecurityRequirements")
ListTasks = Action("ListTasks")
StartCodeRemediation = Action("StartCodeRemediation")
StartPentestExecution = Action("StartPentestExecution")
StartPentestJob = Action("StartPentestJob")
StopPentestExecution = Action("StopPentestExecution")
StopPentestJob = Action("StopPentestJob")
ToggleManagedControl = Action("ToggleManagedControl")
ToggleManagedSecurityRequirement = Action("ToggleManagedSecurityRequirement")
UpdateAgentInstance = Action("UpdateAgentInstance")
UpdateAgentSpace = Action("UpdateAgentSpace")
UpdateApplication = Action("UpdateApplication")
UpdateControl = Action("UpdateControl")
UpdateFinding = Action("UpdateFinding")
UpdateIntegratedResources = Action("UpdateIntegratedResources")
UpdatePentest = Action("UpdatePentest")
UpdateSecurityRequirement = Action("UpdateSecurityRequirement")
VerifyTargetDomain = Action("VerifyTargetDomain")
