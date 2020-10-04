# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Network Manager'
prefix = 'networkmanager'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateCustomerGateway = Action('AssociateCustomerGateway')
AssociateLink = Action('AssociateLink')
CreateDevice = Action('CreateDevice')
CreateGlobalNetwork = Action('CreateGlobalNetwork')
CreateLink = Action('CreateLink')
CreateSite = Action('CreateSite')
DeleteDevice = Action('DeleteDevice')
DeleteGlobalNetwork = Action('DeleteGlobalNetwork')
DeleteLink = Action('DeleteLink')
DeleteSite = Action('DeleteSite')
DeregisterTransitGateway = Action('DeregisterTransitGateway')
DescribeGlobalNetworks = Action('DescribeGlobalNetworks')
DisassociateCustomerGateway = Action('DisassociateCustomerGateway')
DisassociateLink = Action('DisassociateLink')
GetCustomerGatewayAssociations = Action('GetCustomerGatewayAssociations')
GetDevices = Action('GetDevices')
GetLinkAssociations = Action('GetLinkAssociations')
GetLinks = Action('GetLinks')
GetSites = Action('GetSites')
GetTransitGatewayRegistrations = Action('GetTransitGatewayRegistrations')
ListTagsForResource = Action('ListTagsForResource')
RegisterTransitGateway = Action('RegisterTransitGateway')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDevice = Action('UpdateDevice')
UpdateGlobalNetwork = Action('UpdateGlobalNetwork')
UpdateLink = Action('UpdateLink')
UpdateSite = Action('UpdateSite')
