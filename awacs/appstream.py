# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon AppStream'
prefix = 'appstream'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateFleet = Action('AssociateFleet')
BatchAssociateUserStack = Action('BatchAssociateUserStack')
BatchDisassociateUserStack = Action('BatchDisassociateUserStack')
CopyImage = Action('CopyImage')
CreateDirectoryConfig = Action('CreateDirectoryConfig')
CreateFleet = Action('CreateFleet')
CreateImageBuilder = Action('CreateImageBuilder')
CreateImageBuilderStreamingURL = Action('CreateImageBuilderStreamingURL')
CreateStack = Action('CreateStack')
CreateStreamingURL = Action('CreateStreamingURL')
CreateUser = Action('CreateUser')
DeleteDirectoryConfig = Action('DeleteDirectoryConfig')
DeleteFleet = Action('DeleteFleet')
DeleteImage = Action('DeleteImage')
DeleteImageBuilder = Action('DeleteImageBuilder')
DeleteImagePermissions = Action('DeleteImagePermissions')
DeleteStack = Action('DeleteStack')
DeleteUser = Action('DeleteUser')
DescribeDirectoryConfigs = Action('DescribeDirectoryConfigs')
DescribeFleets = Action('DescribeFleets')
DescribeImageBuilders = Action('DescribeImageBuilders')
DescribeImagePermissions = Action('DescribeImagePermissions')
DescribeImages = Action('DescribeImages')
DescribeSessions = Action('DescribeSessions')
DescribeStacks = Action('DescribeStacks')
DescribeUserStackAssociations = Action('DescribeUserStackAssociations')
DescribeUsers = Action('DescribeUsers')
DisableUser = Action('DisableUser')
DisassociateFleet = Action('DisassociateFleet')
EnableUser = Action('EnableUser')
ExpireSession = Action('ExpireSession')
ListAssociatedFleets = Action('ListAssociatedFleets')
ListAssociatedStacks = Action('ListAssociatedStacks')
ListTagsForResource = Action('ListTagsForResource')
StartFleet = Action('StartFleet')
StartImageBuilder = Action('StartImageBuilder')
StopFleet = Action('StopFleet')
StopImageBuilder = Action('StopImageBuilder')
Stream = Action('Stream')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDirectoryConfig = Action('UpdateDirectoryConfig')
UpdateFleet = Action('UpdateFleet')
UpdateImagePermissions = Action('UpdateImagePermissions')
UpdateStack = Action('UpdateStack')
