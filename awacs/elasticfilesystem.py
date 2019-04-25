# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic File System'
prefix = 'elasticfilesystem'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateFileSystem = Action('CreateFileSystem')
CreateMountTarget = Action('CreateMountTarget')
CreateTags = Action('CreateTags')
DeleteFileSystem = Action('DeleteFileSystem')
DeleteMountTarget = Action('DeleteMountTarget')
DeleteTags = Action('DeleteTags')
DescribeFileSystems = Action('DescribeFileSystems')
DescribeLifecycleConfiguration = Action('DescribeLifecycleConfiguration')
DescribeMountTargetSecurityGroups = \
    Action('DescribeMountTargetSecurityGroups')
DescribeMountTargets = Action('DescribeMountTargets')
DescribeTags = Action('DescribeTags')
ModifyMountTargetSecurityGroups = \
    Action('ModifyMountTargetSecurityGroups')
PutLifecycleConfiguration = Action('PutLifecycleConfiguration')
UpdateFileSystem = Action('UpdateFileSystem')
