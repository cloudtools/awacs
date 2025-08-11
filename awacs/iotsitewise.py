# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT SiteWise"
prefix = "iotsitewise"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateAssets = Action("AssociateAssets")
AssociateGatewaySink = Action("AssociateGatewaySink")
AssociateGatewaySource = Action("AssociateGatewaySource")
AssociateTimeSeriesToAssetProperty = Action("AssociateTimeSeriesToAssetProperty")
AssociateViewEntities = Action("AssociateViewEntities")
BatchAssociateProjectAssets = Action("BatchAssociateProjectAssets")
BatchDisassociateProjectAssets = Action("BatchDisassociateProjectAssets")
BatchGetAssetPropertyAggregates = Action("BatchGetAssetPropertyAggregates")
BatchGetAssetPropertyValue = Action("BatchGetAssetPropertyValue")
BatchGetAssetPropertyValueHistory = Action("BatchGetAssetPropertyValueHistory")
BatchPutAssetPropertyValue = Action("BatchPutAssetPropertyValue")
CreateAccessPolicy = Action("CreateAccessPolicy")
CreateAsset = Action("CreateAsset")
CreateAssetModel = Action("CreateAssetModel")
CreateAssetModelCompositeModel = Action("CreateAssetModelCompositeModel")
CreateAssetTemplate = Action("CreateAssetTemplate")
CreateBulkImportJob = Action("CreateBulkImportJob")
CreateComputationModel = Action("CreateComputationModel")
CreateDashboard = Action("CreateDashboard")
CreateDataset = Action("CreateDataset")
CreateGateway = Action("CreateGateway")
CreateGroup = Action("CreateGroup")
CreateMeasurementDataStore = Action("CreateMeasurementDataStore")
CreateMetricType = Action("CreateMetricType")
CreatePortal = Action("CreatePortal")
CreateProject = Action("CreateProject")
CreateView = Action("CreateView")
DeleteAccessPolicy = Action("DeleteAccessPolicy")
DeleteAsset = Action("DeleteAsset")
DeleteAssetModel = Action("DeleteAssetModel")
DeleteAssetModelCompositeModel = Action("DeleteAssetModelCompositeModel")
DeleteAssetModelInterfaceRelationship = Action("DeleteAssetModelInterfaceRelationship")
DeleteAssetTemplate = Action("DeleteAssetTemplate")
DeleteComputationModel = Action("DeleteComputationModel")
DeleteDashboard = Action("DeleteDashboard")
DeleteDataset = Action("DeleteDataset")
DeleteGateway = Action("DeleteGateway")
DeleteGroup = Action("DeleteGroup")
DeleteMeasurementDataStore = Action("DeleteMeasurementDataStore")
DeleteMetricType = Action("DeleteMetricType")
DeletePortal = Action("DeletePortal")
DeleteProject = Action("DeleteProject")
DeleteTimeSeries = Action("DeleteTimeSeries")
DeleteView = Action("DeleteView")
DeregisterViewEntities = Action("DeregisterViewEntities")
DescribeAccessPolicy = Action("DescribeAccessPolicy")
DescribeAction = Action("DescribeAction")
DescribeAsset = Action("DescribeAsset")
DescribeAssetCompositeModel = Action("DescribeAssetCompositeModel")
DescribeAssetModel = Action("DescribeAssetModel")
DescribeAssetModelCompositeModel = Action("DescribeAssetModelCompositeModel")
DescribeAssetModelInterfaceRelationship = Action(
    "DescribeAssetModelInterfaceRelationship"
)
DescribeAssetProperty = Action("DescribeAssetProperty")
DescribeAssetTemplates = Action("DescribeAssetTemplates")
DescribeAssets = Action("DescribeAssets")
DescribeBulkImportJob = Action("DescribeBulkImportJob")
DescribeComputationModel = Action("DescribeComputationModel")
DescribeComputationModelExecutionSummary = Action(
    "DescribeComputationModelExecutionSummary"
)
DescribeDashboard = Action("DescribeDashboard")
DescribeDataset = Action("DescribeDataset")
DescribeDefaultEncryptionConfiguration = Action(
    "DescribeDefaultEncryptionConfiguration"
)
DescribeExecution = Action("DescribeExecution")
DescribeGateway = Action("DescribeGateway")
DescribeGatewayCapabilityConfiguration = Action(
    "DescribeGatewayCapabilityConfiguration"
)
DescribeGateways = Action("DescribeGateways")
DescribeGroups = Action("DescribeGroups")
DescribeLoggingOptions = Action("DescribeLoggingOptions")
DescribeMeasurementDataStores = Action("DescribeMeasurementDataStores")
DescribeMetricTypes = Action("DescribeMetricTypes")
DescribePortal = Action("DescribePortal")
DescribeProject = Action("DescribeProject")
DescribeStorageConfiguration = Action("DescribeStorageConfiguration")
DescribeTimeSeries = Action("DescribeTimeSeries")
DescribeViews = Action("DescribeViews")
DisassociateAssets = Action("DisassociateAssets")
DisassociateGatewaySink = Action("DisassociateGatewaySink")
DisassociateGatewaySource = Action("DisassociateGatewaySource")
DisassociateTimeSeriesFromAssetProperty = Action(
    "DisassociateTimeSeriesFromAssetProperty"
)
DisassociateViewEntities = Action("DisassociateViewEntities")
EnableSiteWiseIntegration = Action("EnableSiteWiseIntegration")
ExecuteAction = Action("ExecuteAction")
ExecuteQuery = Action("ExecuteQuery")
GetAssetPropertyAggregates = Action("GetAssetPropertyAggregates")
GetAssetPropertyValue = Action("GetAssetPropertyValue")
GetAssetPropertyValueHistory = Action("GetAssetPropertyValueHistory")
GetInterpolatedAssetPropertyValues = Action("GetInterpolatedAssetPropertyValues")
GetMeasurementData = Action("GetMeasurementData")
GetMetricData = Action("GetMetricData")
InvokeAssistant = Action("InvokeAssistant")
ListAccessPolicies = Action("ListAccessPolicies")
ListActions = Action("ListActions")
ListAssetModelCompositeModels = Action("ListAssetModelCompositeModels")
ListAssetModelProperties = Action("ListAssetModelProperties")
ListAssetModels = Action("ListAssetModels")
ListAssetProperties = Action("ListAssetProperties")
ListAssetRelationships = Action("ListAssetRelationships")
ListAssetTemplates = Action("ListAssetTemplates")
ListAssets = Action("ListAssets")
ListAssociatedAssets = Action("ListAssociatedAssets")
ListBulkImportJobs = Action("ListBulkImportJobs")
ListCompositionRelationships = Action("ListCompositionRelationships")
ListComputationModelDataBindingUsages = Action("ListComputationModelDataBindingUsages")
ListComputationModelResolveToResources = Action(
    "ListComputationModelResolveToResources"
)
ListComputationModels = Action("ListComputationModels")
ListDashboards = Action("ListDashboards")
ListDatasets = Action("ListDatasets")
ListExecutions = Action("ListExecutions")
ListGateways = Action("ListGateways")
ListGroups = Action("ListGroups")
ListInterfaceRelationships = Action("ListInterfaceRelationships")
ListMeasurementDataStores = Action("ListMeasurementDataStores")
ListMeasurementDataStreams = Action("ListMeasurementDataStreams")
ListMetricTypes = Action("ListMetricTypes")
ListPortals = Action("ListPortals")
ListProjectAssets = Action("ListProjectAssets")
ListProjects = Action("ListProjects")
ListTagsForResource = Action("ListTagsForResource")
ListTimeSeries = Action("ListTimeSeries")
ListViewEntities = Action("ListViewEntities")
ListViews = Action("ListViews")
PutAssetModelInterfaceRelationship = Action("PutAssetModelInterfaceRelationship")
PutDefaultEncryptionConfiguration = Action("PutDefaultEncryptionConfiguration")
PutLoggingOptions = Action("PutLoggingOptions")
PutStorageConfiguration = Action("PutStorageConfiguration")
RegisterViewEntities = Action("RegisterViewEntities")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessPolicy = Action("UpdateAccessPolicy")
UpdateAsset = Action("UpdateAsset")
UpdateAssetModel = Action("UpdateAssetModel")
UpdateAssetModelCompositeModel = Action("UpdateAssetModelCompositeModel")
UpdateAssetModelPropertyRouting = Action("UpdateAssetModelPropertyRouting")
UpdateAssetProperty = Action("UpdateAssetProperty")
UpdateAssetTemplate = Action("UpdateAssetTemplate")
UpdateComputationModel = Action("UpdateComputationModel")
UpdateDashboard = Action("UpdateDashboard")
UpdateDataset = Action("UpdateDataset")
UpdateGateway = Action("UpdateGateway")
UpdateGatewayCapabilityConfiguration = Action("UpdateGatewayCapabilityConfiguration")
UpdateGroup = Action("UpdateGroup")
UpdateMeasurementDataStore = Action("UpdateMeasurementDataStore")
UpdatePortal = Action("UpdatePortal")
UpdateProject = Action("UpdateProject")
UpdateView = Action("UpdateView")
