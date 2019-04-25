# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT SiteWise'
prefix = 'iotsitewise'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateGatewaySink = Action('AssociateGatewaySink')
AssociateGatewaySource = Action('AssociateGatewaySource')
AssociateViewEntities = Action('AssociateViewEntities')
CreateAsset = Action('CreateAsset')
CreateAssetTemplate = Action('CreateAssetTemplate')
CreateGateway = Action('CreateGateway')
CreateGroup = Action('CreateGroup')
CreateMeasurementDataStore = Action('CreateMeasurementDataStore')
CreateMetricType = Action('CreateMetricType')
CreateView = Action('CreateView')
DeleteAsset = Action('DeleteAsset')
DeleteAssetTemplate = Action('DeleteAssetTemplate')
DeleteGateway = Action('DeleteGateway')
DeleteGroup = Action('DeleteGroup')
DeleteMeasurementDataStore = Action('DeleteMeasurementDataStore')
DeleteMetricType = Action('DeleteMetricType')
DeleteView = Action('DeleteView')
DeregisterViewEntities = Action('DeregisterViewEntities')
DescribeAssetTemplates = Action('DescribeAssetTemplates')
DescribeAssets = Action('DescribeAssets')
DescribeGateways = Action('DescribeGateways')
DescribeGroups = Action('DescribeGroups')
DescribeMeasurementDataStores = Action('DescribeMeasurementDataStores')
DescribeMetricTypes = Action('DescribeMetricTypes')
DescribeViews = Action('DescribeViews')
DisassociateGatewaySink = Action('DisassociateGatewaySink')
DisassociateGatewaySource = Action('DisassociateGatewaySource')
DisassociateViewEntities = Action('DisassociateViewEntities')
GetMeasurementData = Action('GetMeasurementData')
GetMetricData = Action('GetMetricData')
ListAssetTemplates = Action('ListAssetTemplates')
ListAssets = Action('ListAssets')
ListGateways = Action('ListGateways')
ListGroups = Action('ListGroups')
ListMeasurementDataStores = Action('ListMeasurementDataStores')
ListMeasurementDataStreams = Action('ListMeasurementDataStreams')
ListMetricTypes = Action('ListMetricTypes')
ListViewEntities = Action('ListViewEntities')
ListViews = Action('ListViews')
RegisterViewEntities = Action('RegisterViewEntities')
UpdateAsset = Action('UpdateAsset')
UpdateAssetTemplate = Action('UpdateAssetTemplate')
UpdateGateway = Action('UpdateGateway')
UpdateGroup = Action('UpdateGroup')
UpdateMeasurementDataStore = Action('UpdateMeasurementDataStore')
UpdateView = Action('UpdateView')
