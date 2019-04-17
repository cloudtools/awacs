# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaConnect'
prefix = 'mediaconnect'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddFlowOutputs = Action('AddFlowOutputs')
CreateFlow = Action('CreateFlow')
DeleteFlow = Action('DeleteFlow')
DescribeFlow = Action('DescribeFlow')
GrantFlowEntitlements = Action('GrantFlowEntitlements')
ListEntitlements = Action('ListEntitlements')
ListFlows = Action('ListFlows')
RemoveFlowOutput = Action('RemoveFlowOutput')
RevokeFlowEntitlement = Action('RevokeFlowEntitlement')
StartFlow = Action('StartFlow')
StopFlow = Action('StopFlow')
UpdateFlowEntitlement = Action('UpdateFlowEntitlement')
UpdateFlowOutput = Action('UpdateFlowOutput')
UpdateFlowSource = Action('UpdateFlowSource')
