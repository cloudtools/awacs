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


AssociateAssets = Action('AssociateAssets')
AssociateGatewaySink = Action('AssociateGatewaySink')
AssociateGatewaySource = Action('AssociateGatewaySource')
AssociateViewEntities = Action('AssociateViewEntities')
BatchAssociateProjectAssets = Action('BatchAssociateProjectAssets')
BatchDisassociateProjectAssets = Action('BatchDisassociateProjectAssets')
BatchPutAssetPropertyValue = Action('BatchPutAssetPropertyValue')
CreateAccessPolicy = Action('CreateAccessPolicy')
CreateAsset = Action('CreateAsset')
CreateAssetModel = Action('CreateAssetModel')
CreateAssetTemplate = Action('CreateAssetTemplate')
CreateDashboard = Action('CreateDashboard')
CreateGateway = Action('CreateGateway')
CreateGroup = Action('CreateGroup')
CreateMeasurementDataStore = Action('CreateMeasurementDataStore')
CreateMetricType = Action('CreateMetricType')
CreatePortal = Action('CreatePortal')
CreateProject = Action('CreateProject')
CreateView = Action('CreateView')
DeleteAccessPolicy = Action('DeleteAccessPolicy')
DeleteAsset = Action('DeleteAsset')
DeleteAssetModel = Action('DeleteAssetModel')
DeleteAssetTemplate = Action('DeleteAssetTemplate')
DeleteDashboard = Action('DeleteDashboard')
DeleteGateway = Action('DeleteGateway')
DeleteGroup = Action('DeleteGroup')
DeleteMeasurementDataStore = Action('DeleteMeasurementDataStore')
DeleteMetricType = Action('DeleteMetricType')
DeletePortal = Action('DeletePortal')
DeleteProject = Action('DeleteProject')
DeleteView = Action('DeleteView')
DeregisterViewEntities = Action('DeregisterViewEntities')
DescribeAccessPolicy = Action('DescribeAccessPolicy')
DescribeAsset = Action('DescribeAsset')
DescribeAssetModel = Action('DescribeAssetModel')
DescribeAssetProperty = Action('DescribeAssetProperty')
DescribeAssetTemplates = Action('DescribeAssetTemplates')
DescribeAssets = Action('DescribeAssets')
DescribeDashboard = Action('DescribeDashboard')
DescribeGateway = Action('DescribeGateway')
DescribeGatewayCapabilityConfiguration = \
    Action('DescribeGatewayCapabilityConfiguration')
DescribeGateways = Action('DescribeGateways')
DescribeGroups = Action('DescribeGroups')
DescribeLoggingOptions = Action('DescribeLoggingOptions')
DescribeMeasurementDataStores = Action('DescribeMeasurementDataStores')
DescribeMetricTypes = Action('DescribeMetricTypes')
DescribePortal = Action('DescribePortal')
DescribeProject = Action('DescribeProject')
DescribeViews = Action('DescribeViews')
DisassociateAssets = Action('DisassociateAssets')
DisassociateGatewaySink = Action('DisassociateGatewaySink')
DisassociateGatewaySource = Action('DisassociateGatewaySource')
DisassociateViewEntities = Action('DisassociateViewEntities')
GetAssetPropertyAggregates = Action('GetAssetPropertyAggregates')
GetAssetPropertyValue = Action('GetAssetPropertyValue')
GetAssetPropertyValueHistory = Action('GetAssetPropertyValueHistory')
GetMeasurementData = Action('GetMeasurementData')
GetMetricData = Action('GetMetricData')
ListAccessPolicies = Action('ListAccessPolicies')
ListAssetModels = Action('ListAssetModels')
ListAssetTemplates = Action('ListAssetTemplates')
ListAssets = Action('ListAssets')
ListAssociatedAssets = Action('ListAssociatedAssets')
ListDashboards = Action('ListDashboards')
ListGateways = Action('ListGateways')
ListGroups = Action('ListGroups')
ListMeasurementDataStores = Action('ListMeasurementDataStores')
ListMeasurementDataStreams = Action('ListMeasurementDataStreams')
ListMetricTypes = Action('ListMetricTypes')
ListPortals = Action('ListPortals')
ListProjectAssets = Action('ListProjectAssets')
ListProjects = Action('ListProjects')
ListTagsForResource = Action('ListTagsForResource')
ListViewEntities = Action('ListViewEntities')
ListViews = Action('ListViews')
PutLoggingOptions = Action('PutLoggingOptions')
RegisterViewEntities = Action('RegisterViewEntities')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAccessPolicy = Action('UpdateAccessPolicy')
UpdateAsset = Action('UpdateAsset')
UpdateAssetModel = Action('UpdateAssetModel')
UpdateAssetProperty = Action('UpdateAssetProperty')
UpdateAssetTemplate = Action('UpdateAssetTemplate')
UpdateDashboard = Action('UpdateDashboard')
UpdateGateway = Action('UpdateGateway')
UpdateGatewayCapabilityConfiguration = \
    Action('UpdateGatewayCapabilityConfiguration')
UpdateGroup = Action('UpdateGroup')
UpdateMeasurementDataStore = Action('UpdateMeasurementDataStore')
UpdatePortal = Action('UpdatePortal')
UpdateProject = Action('UpdateProject')
UpdateView = Action('UpdateView')
