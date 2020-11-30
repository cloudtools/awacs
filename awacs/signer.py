# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Signer'
prefix = 'signer'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddProfilePermission = Action('AddProfilePermission')
CancelSigningProfile = Action('CancelSigningProfile')
DescribeSigningJob = Action('DescribeSigningJob')
GetSigningPlatform = Action('GetSigningPlatform')
GetSigningProfile = Action('GetSigningProfile')
ListProfilePermissions = Action('ListProfilePermissions')
ListSigningJobs = Action('ListSigningJobs')
ListSigningPlatforms = Action('ListSigningPlatforms')
ListSigningProfiles = Action('ListSigningProfiles')
ListTagsForResource = Action('ListTagsForResource')
PutSigningProfile = Action('PutSigningProfile')
RemoveProfilePermission = Action('RemoveProfilePermission')
RevokeSignature = Action('RevokeSignature')
RevokeSigningProfile = Action('RevokeSigningProfile')
StartSigningJob = Action('StartSigningJob')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
