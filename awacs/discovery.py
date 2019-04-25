# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Application Discovery'
prefix = 'discovery'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateConfigurationItemsToApplication = \
    Action('AssociateConfigurationItemsToApplication')
BatchDeleteImportData = Action('BatchDeleteImportData')
CreateApplication = Action('CreateApplication')
CreateTags = Action('CreateTags')
DeleteApplications = Action('DeleteApplications')
DeleteTags = Action('DeleteTags')
DescribeAgents = Action('DescribeAgents')
DescribeConfigurations = Action('DescribeConfigurations')
DescribeContinuousExports = Action('DescribeContinuousExports')
DescribeExportConfigurations = Action('DescribeExportConfigurations')
DescribeExportTasks = Action('DescribeExportTasks')
DescribeImportTasks = Action('DescribeImportTasks')
DescribeTags = Action('DescribeTags')
DisassociateConfigurationItemsFromApplication = \
    Action('DisassociateConfigurationItemsFromApplication')
ExportConfigurations = Action('ExportConfigurations')
GetDiscoverySummary = Action('GetDiscoverySummary')
ListConfigurations = Action('ListConfigurations')
ListServerNeighbors = Action('ListServerNeighbors')
StartContinuousExport = Action('StartContinuousExport')
StartDataCollectionByAgentIds = Action('StartDataCollectionByAgentIds')
StartExportTask = Action('StartExportTask')
StartImportTask = Action('StartImportTask')
StopContinuousExport = Action('StopContinuousExport')
StopDataCollectionByAgentIds = Action('StopDataCollectionByAgentIds')
UpdateApplication = Action('UpdateApplication')
