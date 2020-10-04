# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Marketplace'
prefix = 'aws-marketplace'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptAgreementApprovalRequest = Action('AcceptAgreementApprovalRequest')
AssociateProductsWithPrivateMarketplace = \
    Action('AssociateProductsWithPrivateMarketplace')
BatchMeterUsage = Action('BatchMeterUsage')
CancelAgreementRequest = Action('CancelAgreementRequest')
CancelChangeSet = Action('CancelChangeSet')
CompleteTask = Action('CompleteTask')
CreatePrivateMarketplace = Action('CreatePrivateMarketplace')
CreatePrivateMarketplaceProfile = \
    Action('CreatePrivateMarketplaceProfile')
CreatePrivateMarketplaceRequests = \
    Action('CreatePrivateMarketplaceRequests')
DescribeAgreement = Action('DescribeAgreement')
DescribeBuilds = Action('DescribeBuilds')
DescribeChangeSet = Action('DescribeChangeSet')
DescribeEntity = Action('DescribeEntity')
DescribePrivateMarketplaceProducts = \
    Action('DescribePrivateMarketplaceProducts')
DescribePrivateMarketplaceProfile = \
    Action('DescribePrivateMarketplaceProfile')
DescribePrivateMarketplaceRequests = \
    Action('DescribePrivateMarketplaceRequests')
DescribePrivateMarketplaceSettings = \
    Action('DescribePrivateMarketplaceSettings')
DescribePrivateMarketplaceStatus = \
    Action('DescribePrivateMarketplaceStatus')
DescribeProcurementSystemConfiguration = \
    Action('DescribeProcurementSystemConfiguration')
DescribeTask = Action('DescribeTask')
DisassociateProductsFromPrivateMarketplace = \
    Action('DisassociateProductsFromPrivateMarketplace')
GetAgreementApprovalRequest = Action('GetAgreementApprovalRequest')
GetAgreementRequest = Action('GetAgreementRequest')
GetAgreementTerms = Action('GetAgreementTerms')
GetEntitlements = Action('GetEntitlements')
ListAgreementApprovalRequests = Action('ListAgreementApprovalRequests')
ListAgreementRequests = Action('ListAgreementRequests')
ListBuilds = Action('ListBuilds')
ListChangeSets = Action('ListChangeSets')
ListEntities = Action('ListEntities')
ListPrivateMarketplaceProducts = Action('ListPrivateMarketplaceProducts')
ListPrivateMarketplaceRequests = Action('ListPrivateMarketplaceRequests')
ListTasks = Action('ListTasks')
MeterUsage = Action('MeterUsage')
PutProcurementSystemConfiguration = \
    Action('PutProcurementSystemConfiguration')
RegisterUsage = Action('RegisterUsage')
RejectAgreementApprovalRequest = Action('RejectAgreementApprovalRequest')
ResolveCustomer = Action('ResolveCustomer')
SearchAgreements = Action('SearchAgreements')
StartBuild = Action('StartBuild')
StartChangeSet = Action('StartChangeSet')
StartPrivateMarketplace = Action('StartPrivateMarketplace')
StopPrivateMarketplace = Action('StopPrivateMarketplace')
Subscribe = Action('Subscribe')
Unsubscribe = Action('Unsubscribe')
UpdateAgreementApprovalRequest = Action('UpdateAgreementApprovalRequest')
UpdatePrivateMarketplaceProfile = \
    Action('UpdatePrivateMarketplaceProfile')
UpdatePrivateMarketplaceSettings = \
    Action('UpdatePrivateMarketplaceSettings')
UpdateTask = Action('UpdateTask')
ViewSubscriptions = Action('ViewSubscriptions')
