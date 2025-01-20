# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CloudFormation"
prefix = "cloudformation"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateOrganizationsAccess = Action("ActivateOrganizationsAccess")
ActivateType = Action("ActivateType")
BatchDescribeTypeConfigurations = Action("BatchDescribeTypeConfigurations")
CancelResourceRequest = Action("CancelResourceRequest")
CancelUpdateStack = Action("CancelUpdateStack")
ContinueUpdateRollback = Action("ContinueUpdateRollback")
CreateChangeSet = Action("CreateChangeSet")
CreateGeneratedTemplate = Action("CreateGeneratedTemplate")
CreateResource = Action("CreateResource")
CreateStack = Action("CreateStack")
CreateStackInstances = Action("CreateStackInstances")
CreateStackSet = Action("CreateStackSet")
CreateUploadBucket = Action("CreateUploadBucket")
DeactivateOrganizationsAccess = Action("DeactivateOrganizationsAccess")
DeactivateType = Action("DeactivateType")
DeleteChangeSet = Action("DeleteChangeSet")
DeleteGeneratedTemplate = Action("DeleteGeneratedTemplate")
DeleteResource = Action("DeleteResource")
DeleteStack = Action("DeleteStack")
DeleteStackInstances = Action("DeleteStackInstances")
DeleteStackSet = Action("DeleteStackSet")
DeregisterType = Action("DeregisterType")
DescribeAccountLimits = Action("DescribeAccountLimits")
DescribeChangeSet = Action("DescribeChangeSet")
DescribeChangeSetHook = Action("DescribeChangeSetHook")
DescribeChangeSetHooks = Action("DescribeChangeSetHooks")
DescribeGeneratedTemplate = Action("DescribeGeneratedTemplate")
DescribeOrganizationsAccess = Action("DescribeOrganizationsAccess")
DescribePublisher = Action("DescribePublisher")
DescribeResourceScan = Action("DescribeResourceScan")
DescribeStackDriftDetectionStatus = Action("DescribeStackDriftDetectionStatus")
DescribeStackEvents = Action("DescribeStackEvents")
DescribeStackInstance = Action("DescribeStackInstance")
DescribeStackResource = Action("DescribeStackResource")
DescribeStackResourceDrifts = Action("DescribeStackResourceDrifts")
DescribeStackResources = Action("DescribeStackResources")
DescribeStackSet = Action("DescribeStackSet")
DescribeStackSetOperation = Action("DescribeStackSetOperation")
DescribeStacks = Action("DescribeStacks")
DescribeType = Action("DescribeType")
DescribeTypeRegistration = Action("DescribeTypeRegistration")
DetectStackDrift = Action("DetectStackDrift")
DetectStackResourceDrift = Action("DetectStackResourceDrift")
DetectStackSetDrift = Action("DetectStackSetDrift")
EstimateTemplateCost = Action("EstimateTemplateCost")
ExecuteChangeSet = Action("ExecuteChangeSet")
GetGeneratedTemplate = Action("GetGeneratedTemplate")
GetResource = Action("GetResource")
GetResourceRequestStatus = Action("GetResourceRequestStatus")
GetStackPolicy = Action("GetStackPolicy")
GetTemplate = Action("GetTemplate")
GetTemplateSummary = Action("GetTemplateSummary")
ImportStacksToStackSet = Action("ImportStacksToStackSet")
ListChangeSets = Action("ListChangeSets")
ListExports = Action("ListExports")
ListGeneratedTemplates = Action("ListGeneratedTemplates")
ListHookResults = Action("ListHookResults")
ListImports = Action("ListImports")
ListResourceRequests = Action("ListResourceRequests")
ListResourceScanRelatedResources = Action("ListResourceScanRelatedResources")
ListResourceScanResources = Action("ListResourceScanResources")
ListResourceScans = Action("ListResourceScans")
ListResources = Action("ListResources")
ListStackInstanceResourceDrifts = Action("ListStackInstanceResourceDrifts")
ListStackInstances = Action("ListStackInstances")
ListStackResources = Action("ListStackResources")
ListStackSetAutoDeploymentTargets = Action("ListStackSetAutoDeploymentTargets")
ListStackSetOperationResults = Action("ListStackSetOperationResults")
ListStackSetOperations = Action("ListStackSetOperations")
ListStackSets = Action("ListStackSets")
ListStacks = Action("ListStacks")
ListTypeRegistrations = Action("ListTypeRegistrations")
ListTypeVersions = Action("ListTypeVersions")
ListTypes = Action("ListTypes")
PreviewStackUpdate = Action("PreviewStackUpdate")
PublishType = Action("PublishType")
RecordHandlerProgress = Action("RecordHandlerProgress")
RegisterPublisher = Action("RegisterPublisher")
RegisterType = Action("RegisterType")
RollbackStack = Action("RollbackStack")
SetStackPolicy = Action("SetStackPolicy")
SetTypeConfiguration = Action("SetTypeConfiguration")
SetTypeDefaultVersion = Action("SetTypeDefaultVersion")
SignalResource = Action("SignalResource")
StartResourceScan = Action("StartResourceScan")
StopStackSetOperation = Action("StopStackSetOperation")
TagResource = Action("TagResource")
TestType = Action("TestType")
UntagResource = Action("UntagResource")
UpdateGeneratedTemplate = Action("UpdateGeneratedTemplate")
UpdateResource = Action("UpdateResource")
UpdateStack = Action("UpdateStack")
UpdateStackInstances = Action("UpdateStackInstances")
UpdateStackSet = Action("UpdateStackSet")
UpdateTerminationProtection = Action("UpdateTerminationProtection")
ValidateTemplate = Action("ValidateTemplate")
