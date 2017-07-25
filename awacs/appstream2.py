# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon AppStream 2.0'
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
CreateFleet = Action('CreateFleet')
CreateStack = Action('CreateStack')
CreateStreamingURL = Action('CreateStreamingURL')
DeleteFleet = Action('DeleteFleet')
DeleteStack = Action('DeleteStack')
DescribeFleets = Action('DescribeFleets')
DescribeImages = Action('DescribeImages')
DescribeSessions = Action('DescribeSessions')
DescribeStacks = Action('DescribeStacks')
DisassociateFleet = Action('DisassociateFleet')
ExpireSession = Action('ExpireSession')
ListAssociatedFleets = Action('ListAssociatedFleets')
ListAssociatedStacks = Action('ListAssociatedStacks')
StartFleet = Action('StartFleet')
StopFleet = Action('StopFleet')
UpdateFleet = Action('UpdateFleet')
UpdateStack = Action('UpdateStack')
