# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EC2 Image Builder'
prefix = 'imagebuilder'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelImageCreation = Action('CancelImageCreation')
CreateComponent = Action('CreateComponent')
CreateContainerRecipe = Action('CreateContainerRecipe')
CreateDistributionConfiguration = \
    Action('CreateDistributionConfiguration')
CreateImage = Action('CreateImage')
CreateImagePipeline = Action('CreateImagePipeline')
CreateImageRecipe = Action('CreateImageRecipe')
CreateInfrastructureConfiguration = \
    Action('CreateInfrastructureConfiguration')
DeleteComponent = Action('DeleteComponent')
DeleteContainerRecipe = Action('DeleteContainerRecipe')
DeleteDistributionConfiguration = \
    Action('DeleteDistributionConfiguration')
DeleteImage = Action('DeleteImage')
DeleteImagePipeline = Action('DeleteImagePipeline')
DeleteImageRecipe = Action('DeleteImageRecipe')
DeleteInfrastructureConfiguration = \
    Action('DeleteInfrastructureConfiguration')
GetComponent = Action('GetComponent')
GetComponentPolicy = Action('GetComponentPolicy')
GetContainerRecipe = Action('GetContainerRecipe')
GetContainerRecipePolicy = Action('GetContainerRecipePolicy')
GetDistributionConfiguration = Action('GetDistributionConfiguration')
GetImage = Action('GetImage')
GetImagePipeline = Action('GetImagePipeline')
GetImagePolicy = Action('GetImagePolicy')
GetImageRecipe = Action('GetImageRecipe')
GetImageRecipePolicy = Action('GetImageRecipePolicy')
GetInfrastructureConfiguration = Action('GetInfrastructureConfiguration')
ListComponentBuildVersions = Action('ListComponentBuildVersions')
ListComponents = Action('ListComponents')
ListContainerRecipes = Action('ListContainerRecipes')
ListDistributionConfigurations = Action('ListDistributionConfigurations')
ListImageBuildVersions = Action('ListImageBuildVersions')
ListImagePipelineImages = Action('ListImagePipelineImages')
ListImagePipelines = Action('ListImagePipelines')
ListImageRecipes = Action('ListImageRecipes')
ListImages = Action('ListImages')
ListInfrastructureConfigurations = \
    Action('ListInfrastructureConfigurations')
ListTagsForResource = Action('ListTagsForResource')
PutComponentPolicy = Action('PutComponentPolicy')
PutContainerRecipePolicy = Action('PutContainerRecipePolicy')
PutImagePolicy = Action('PutImagePolicy')
PutImageRecipePolicy = Action('PutImageRecipePolicy')
StartImagePipelineExecution = Action('StartImagePipelineExecution')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDistributionConfiguration = \
    Action('UpdateDistributionConfiguration')
UpdateImagePipeline = Action('UpdateImagePipeline')
UpdateInfrastructureConfiguration = \
    Action('UpdateInfrastructureConfiguration')
