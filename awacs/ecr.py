# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon EC2 Container Registry'
prefix = 'ecr'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchCheckLayerAvailability = Action('BatchCheckLayerAvailability')
BatchDeleteImage = Action('BatchDeleteImage')
BatchGetImage = Action('BatchGetImage')
CompleteLayerUpload = Action('CompleteLayerUpload')
CreateRepository = Action('CreateRepository')
DeleteLifecyclePolicy = Action('DeleteLifecyclePolicy')
DeleteRepository = Action('DeleteRepository')
DeleteRepositoryPolicy = Action('DeleteRepositoryPolicy')
DescribeImages = Action('DescribeImages')
DescribeRepositories = Action('DescribeRepositories')
GetAuthorizationToken = Action('GetAuthorizationToken')
GetDownloadUrlForLayer = Action('GetDownloadUrlForLayer')
GetLifecyclePolicy = Action('GetLifecyclePolicy')
GetLifecyclePolicyPreview = Action('GetLifecyclePolicyPreview')
GetRepositoryPolicy = Action('GetRepositoryPolicy')
InitiateLayerUpload = Action('InitiateLayerUpload')
ListImages = Action('ListImages')
ListTagsForResource = Action('ListTagsForResource')
PutImage = Action('PutImage')
PutLifecyclePolicy = Action('PutLifecyclePolicy')
SetRepositoryPolicy = Action('SetRepositoryPolicy')
StartLifecyclePolicyPreview = Action('StartLifecyclePolicyPreview')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UploadLayerPart = Action('UploadLayerPart')
