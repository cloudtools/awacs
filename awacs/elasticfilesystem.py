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
CreateTags = Action('CreateTags')
DescribeTags = Action('DescribeTags')
DeleteTags = Action('DeleteTags')
CreateMountTarget = Action('CreateMountTarget')
ModifyMountTargetSecurityGroups = \
    Action('ModifyMountTargetSecurityGroups')
DescribeMountTargetSecurityGroups = \
    Action('DescribeMountTargetSecurityGroups')
DescribeFileSystems = Action('DescribeFileSystems')
DescribeMountTargets = Action('DescribeMountTargets')
DeleteMountTarget = Action('DeleteMountTarget')
DeleteFileSystem = Action('DeleteFileSystem')
