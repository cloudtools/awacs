# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Glue'
prefix = 'glue'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchCreatePartition = Action('BatchCreatePartition')
BatchDeleteConnection = Action('BatchDeleteConnection')
BatchDeletePartition = Action('BatchDeletePartition')
BatchDeleteTable = Action('BatchDeleteTable')
BatchGetPartition = Action('BatchGetPartition')
CreateClassifier = Action('CreateClassifier')
CreateConnection = Action('CreateConnection')
CreateCrawler = Action('CreateCrawler')
CreateDatabase = Action('CreateDatabase')
CreateDevEndpoint = Action('CreateDevEndpoint')
CreateJob = Action('CreateJob')
CreatePartition = Action('CreatePartition')
CreateScript = Action('CreateScript')
CreateSecurityConfiguration = Action('CreateSecurityConfiguration')
CreateTable = Action('CreateTable')
CreateTrigger = Action('CreateTrigger')
CreateUserDefinedFunction = Action('CreateUserDefinedFunction')
DeleteClassifier = Action('DeleteClassifier')
DeleteConnection = Action('DeleteConnection')
DeleteCrawler = Action('DeleteCrawler')
DeleteDatabase = Action('DeleteDatabase')
DeleteDevEndpoint = Action('DeleteDevEndpoint')
DeleteJob = Action('DeleteJob')
DeletePartition = Action('DeletePartition')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteSecurityConfiguration = Action('DeleteSecurityConfiguration')
DeleteTable = Action('DeleteTable')
DeleteTrigger = Action('DeleteTrigger')
DeleteUserDefinedFunction = Action('DeleteUserDefinedFunction')
GetCatalogImportStatus = Action('GetCatalogImportStatus')
GetClassifier = Action('GetClassifier')
GetClassifiers = Action('GetClassifiers')
GetConnection = Action('GetConnection')
GetConnections = Action('GetConnections')
GetCrawler = Action('GetCrawler')
GetCrawlerMetrics = Action('GetCrawlerMetrics')
GetCrawlers = Action('GetCrawlers')
GetDataCatalogEncryptionSettings = \
    Action('GetDataCatalogEncryptionSettings')
GetDatabase = Action('GetDatabase')
GetDatabases = Action('GetDatabases')
GetDataflowGraph = Action('GetDataflowGraph')
GetDevEndpoint = Action('GetDevEndpoint')
GetDevEndpoints = Action('GetDevEndpoints')
GetJob = Action('GetJob')
GetJobRun = Action('GetJobRun')
GetJobRuns = Action('GetJobRuns')
GetJobs = Action('GetJobs')
GetMapping = Action('GetMapping')
GetPartition = Action('GetPartition')
GetPartitions = Action('GetPartitions')
GetPlan = Action('GetPlan')
GetResourcePolicy = Action('GetResourcePolicy')
GetSecurityConfiguration = Action('GetSecurityConfiguration')
GetSecurityConfigurations = Action('GetSecurityConfigurations')
GetTable = Action('GetTable')
GetTableVersions = Action('GetTableVersions')
GetTables = Action('GetTables')
GetTrigger = Action('GetTrigger')
GetTriggers = Action('GetTriggers')
GetUserDefinedFunction = Action('GetUserDefinedFunction')
GetUserDefinedFunctions = Action('GetUserDefinedFunctions')
ImportCatalogToGlue = Action('ImportCatalogToGlue')
PutDataCatalogEncryptionSettings = \
    Action('PutDataCatalogEncryptionSettings')
PutResourcePolicy = Action('PutResourcePolicy')
ResetJobBookmark = Action('ResetJobBookmark')
StartCrawler = Action('StartCrawler')
StartCrawlerSchedule = Action('StartCrawlerSchedule')
StartJobRun = Action('StartJobRun')
StartTrigger = Action('StartTrigger')
StopCrawler = Action('StopCrawler')
StopCrawlerSchedule = Action('StopCrawlerSchedule')
StopTrigger = Action('StopTrigger')
UpdateClassifier = Action('UpdateClassifier')
UpdateConnection = Action('UpdateConnection')
UpdateCrawler = Action('UpdateCrawler')
UpdateDatabase = Action('UpdateDatabase')
UpdateDevEndpoint = Action('UpdateDevEndpoint')
UpdateJob = Action('UpdateJob')
UpdatePartition = Action('UpdatePartition')
UpdateTable = Action('UpdateTable')
UpdateTrigger = Action('UpdateTrigger')
UpdateUserDefinedFunction = Action('UpdateUserDefinedFunction')
