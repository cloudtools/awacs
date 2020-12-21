# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT Core for LoRaWAN'
prefix = 'iotwireless'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateAwsAccountWithPartnerAccount = \
    Action('AssociateAwsAccountWithPartnerAccount')
AssociateWirelessDeviceWithThing = \
    Action('AssociateWirelessDeviceWithThing')
AssociateWirelessGatewayWithCertificate = \
    Action('AssociateWirelessGatewayWithCertificate')
AssociateWirelessGatewayWithThing = \
    Action('AssociateWirelessGatewayWithThing')
CreateDestination = Action('CreateDestination')
CreateDeviceProfile = Action('CreateDeviceProfile')
CreateServiceProfile = Action('CreateServiceProfile')
CreateWirelessDevice = Action('CreateWirelessDevice')
CreateWirelessGateway = Action('CreateWirelessGateway')
CreateWirelessGatewayTask = Action('CreateWirelessGatewayTask')
CreateWirelessGatewayTaskDefinition = \
    Action('CreateWirelessGatewayTaskDefinition')
DeleteDestination = Action('DeleteDestination')
DeleteDeviceProfile = Action('DeleteDeviceProfile')
DeleteServiceProfile = Action('DeleteServiceProfile')
DeleteWirelessDevice = Action('DeleteWirelessDevice')
DeleteWirelessGateway = Action('DeleteWirelessGateway')
DeleteWirelessGatewayTask = Action('DeleteWirelessGatewayTask')
DeleteWirelessGatewayTaskDefinition = \
    Action('DeleteWirelessGatewayTaskDefinition')
DisassociateAwsAccountFromPartnerAccount = \
    Action('DisassociateAwsAccountFromPartnerAccount')
DisassociateWirelessDeviceFromThing = \
    Action('DisassociateWirelessDeviceFromThing')
DisassociateWirelessGatewayFromCertificate = \
    Action('DisassociateWirelessGatewayFromCertificate')
DisassociateWirelessGatewayFromThing = \
    Action('DisassociateWirelessGatewayFromThing')
GetDestination = Action('GetDestination')
GetDeviceProfile = Action('GetDeviceProfile')
GetPartnerAccount = Action('GetPartnerAccount')
GetServiceEndpoint = Action('GetServiceEndpoint')
GetServiceProfile = Action('GetServiceProfile')
GetWirelessDevice = Action('GetWirelessDevice')
GetWirelessDeviceStatistics = Action('GetWirelessDeviceStatistics')
GetWirelessGateway = Action('GetWirelessGateway')
GetWirelessGatewayCertificate = Action('GetWirelessGatewayCertificate')
GetWirelessGatewayFirmwareInformation = \
    Action('GetWirelessGatewayFirmwareInformation')
GetWirelessGatewayStatistics = Action('GetWirelessGatewayStatistics')
GetWirelessGatewayTask = Action('GetWirelessGatewayTask')
GetWirelessGatewayTaskDefinition = \
    Action('GetWirelessGatewayTaskDefinition')
ListDestinations = Action('ListDestinations')
ListDeviceProfiles = Action('ListDeviceProfiles')
ListPartnerAccounts = Action('ListPartnerAccounts')
ListServiceProfiles = Action('ListServiceProfiles')
ListTagsForResource = Action('ListTagsForResource')
ListWirelessDevices = Action('ListWirelessDevices')
ListWirelessGatewayTaskDefinitions = \
    Action('ListWirelessGatewayTaskDefinitions')
ListWirelessGateways = Action('ListWirelessGateways')
SendDataToWirelessDevice = Action('SendDataToWirelessDevice')
TagResource = Action('TagResource')
TestWirelessDevice = Action('TestWirelessDevice')
UntagResource = Action('UntagResource')
UpdateDestination = Action('UpdateDestination')
UpdatePartnerAccount = Action('UpdatePartnerAccount')
UpdateWirelessDevice = Action('UpdateWirelessDevice')
UpdateWirelessGateway = Action('UpdateWirelessGateway')
