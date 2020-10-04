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
CreateDistributionConfiguration = \
    Action('CreateDistributionConfiguration')
CreateImage = Action('CreateImage')
CreateImagePipeline = Action('CreateImagePipeline')
CreateImageRecipe = Action('CreateImageRecipe')
CreateInfrastructureConfiguration = \
    Action('CreateInfrastructureConfiguration')
DeleteComponent = Action('DeleteComponent')
DeleteDistributionConfiguration = \
    Action('DeleteDistributionConfiguration')
DeleteImage = Action('DeleteImage')
DeleteImagePipeline = Action('DeleteImagePipeline')
DeleteImageRecipe = Action('DeleteImageRecipe')
DeleteInfrastructureConfiguration = \
    Action('DeleteInfrastructureConfiguration')
GetComponent = Action('GetComponent')
GetComponentPolicy = Action('GetComponentPolicy')
GetDistributionConfiguration = Action('GetDistributionConfiguration')
GetImage = Action('GetImage')
GetImagePipeline = Action('GetImagePipeline')
GetImagePolicy = Action('GetImagePolicy')
GetImageRecipe = Action('GetImageRecipe')
GetImageRecipePolicy = Action('GetImageRecipePolicy')
GetInfrastructureConfiguration = Action('GetInfrastructureConfiguration')
ListComponentBuildVersions = Action('ListComponentBuildVersions')
ListComponents = Action('ListComponents')
ListDistributionConfigurations = Action('ListDistributionConfigurations')
ListImageBuildVersions = Action('ListImageBuildVersions')
ListImagePipelines = Action('ListImagePipelines')
ListImageRecipes = Action('ListImageRecipes')
ListImages = Action('ListImages')
ListInfrastructureConfigurations = \
    Action('ListInfrastructureConfigurations')
ListTagsForResource = Action('ListTagsForResource')
PutComponentPolicy = Action('PutComponentPolicy')
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
