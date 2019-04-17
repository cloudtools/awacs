# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon WorkLink'
prefix = 'worklink'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateWebsiteCertificateAuthority = \
    Action('AssociateWebsiteCertificateAuthority')
CreateFleet = Action('CreateFleet')
DeleteFleet = Action('DeleteFleet')
DescribeCompanyNetworkConfiguration = \
    Action('DescribeCompanyNetworkConfiguration')
DescribeDevice = Action('DescribeDevice')
DescribeDevicePolicyConfiguration = \
    Action('DescribeDevicePolicyConfiguration')
DescribeFleetMetadata = Action('DescribeFleetMetadata')
DescribeIdentityProviderConfiguration = \
    Action('DescribeIdentityProviderConfiguration')
DescribeWebsiteCertificateAuthority = \
    Action('DescribeWebsiteCertificateAuthority')
DisassociateWebsiteCertificateAuthority = \
    Action('DisassociateWebsiteCertificateAuthority')
ListDevices = Action('ListDevices')
ListFleets = Action('ListFleets')
ListWebsiteCertificateAuthorities = \
    Action('ListWebsiteCertificateAuthorities')
SignOutUser = Action('SignOutUser')
UpdateCompanyNetworkConfiguration = \
    Action('UpdateCompanyNetworkConfiguration')
UpdateDevicePolicyConfiguration = \
    Action('UpdateDevicePolicyConfiguration')
UpdateFleetMetadata = Action('UpdateFleetMetadata')
UpdateIdentityProviderConfiguration = \
    Action('UpdateIdentityProviderConfiguration')
