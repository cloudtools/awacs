# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon EC2 Image Builder"
prefix = "imagebuilder"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelImageCreation = Action("CancelImageCreation")
CancelLifecycleExecution = Action("CancelLifecycleExecution")
CreateComponent = Action("CreateComponent")
CreateContainerRecipe = Action("CreateContainerRecipe")
CreateDistributionConfiguration = Action("CreateDistributionConfiguration")
CreateImage = Action("CreateImage")
CreateImagePipeline = Action("CreateImagePipeline")
CreateImageRecipe = Action("CreateImageRecipe")
CreateInfrastructureConfiguration = Action("CreateInfrastructureConfiguration")
CreateLifecyclePolicy = Action("CreateLifecyclePolicy")
CreateWorkflow = Action("CreateWorkflow")
DeleteComponent = Action("DeleteComponent")
DeleteContainerRecipe = Action("DeleteContainerRecipe")
DeleteDistributionConfiguration = Action("DeleteDistributionConfiguration")
DeleteImage = Action("DeleteImage")
DeleteImagePipeline = Action("DeleteImagePipeline")
DeleteImageRecipe = Action("DeleteImageRecipe")
DeleteInfrastructureConfiguration = Action("DeleteInfrastructureConfiguration")
DeleteLifecyclePolicy = Action("DeleteLifecyclePolicy")
DeleteWorkflow = Action("DeleteWorkflow")
GetComponent = Action("GetComponent")
GetComponentPolicy = Action("GetComponentPolicy")
GetContainerRecipe = Action("GetContainerRecipe")
GetContainerRecipePolicy = Action("GetContainerRecipePolicy")
GetDistributionConfiguration = Action("GetDistributionConfiguration")
GetImage = Action("GetImage")
GetImagePipeline = Action("GetImagePipeline")
GetImagePolicy = Action("GetImagePolicy")
GetImageRecipe = Action("GetImageRecipe")
GetImageRecipePolicy = Action("GetImageRecipePolicy")
GetInfrastructureConfiguration = Action("GetInfrastructureConfiguration")
GetLifecycleExecution = Action("GetLifecycleExecution")
GetLifecyclePolicy = Action("GetLifecyclePolicy")
GetMarketplaceResource = Action("GetMarketplaceResource")
GetWorkflow = Action("GetWorkflow")
GetWorkflowExecution = Action("GetWorkflowExecution")
GetWorkflowStepExecution = Action("GetWorkflowStepExecution")
ImportComponent = Action("ImportComponent")
ImportDiskImage = Action("ImportDiskImage")
ImportVmImage = Action("ImportVmImage")
ListComponentBuildVersions = Action("ListComponentBuildVersions")
ListComponents = Action("ListComponents")
ListContainerRecipes = Action("ListContainerRecipes")
ListDistributionConfigurations = Action("ListDistributionConfigurations")
ListImageBuildVersions = Action("ListImageBuildVersions")
ListImagePackages = Action("ListImagePackages")
ListImagePipelineImages = Action("ListImagePipelineImages")
ListImagePipelines = Action("ListImagePipelines")
ListImageRecipes = Action("ListImageRecipes")
ListImageScanFindingAggregations = Action("ListImageScanFindingAggregations")
ListImageScanFindings = Action("ListImageScanFindings")
ListImages = Action("ListImages")
ListInfrastructureConfigurations = Action("ListInfrastructureConfigurations")
ListLifecycleExecutionResources = Action("ListLifecycleExecutionResources")
ListLifecycleExecutions = Action("ListLifecycleExecutions")
ListLifecyclePolicies = Action("ListLifecyclePolicies")
ListTagsForResource = Action("ListTagsForResource")
ListWaitingWorkflowSteps = Action("ListWaitingWorkflowSteps")
ListWorkflowBuildVersions = Action("ListWorkflowBuildVersions")
ListWorkflowExecutions = Action("ListWorkflowExecutions")
ListWorkflowStepExecutions = Action("ListWorkflowStepExecutions")
ListWorkflows = Action("ListWorkflows")
PutComponentPolicy = Action("PutComponentPolicy")
PutContainerRecipePolicy = Action("PutContainerRecipePolicy")
PutImagePolicy = Action("PutImagePolicy")
PutImageRecipePolicy = Action("PutImageRecipePolicy")
SendWorkflowStepAction = Action("SendWorkflowStepAction")
StartImagePipelineExecution = Action("StartImagePipelineExecution")
StartResourceStateUpdate = Action("StartResourceStateUpdate")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDistributionConfiguration = Action("UpdateDistributionConfiguration")
UpdateImagePipeline = Action("UpdateImagePipeline")
UpdateInfrastructureConfiguration = Action("UpdateInfrastructureConfiguration")
UpdateLifecyclePolicy = Action("UpdateLifecyclePolicy")
