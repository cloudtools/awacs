# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeBuild'
prefix = 'codebuild'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchDeleteBuilds = Action('BatchDeleteBuilds')
BatchGetBuildBatches = Action('BatchGetBuildBatches')
BatchGetBuilds = Action('BatchGetBuilds')
BatchGetProjects = Action('BatchGetProjects')
BatchGetReportGroups = Action('BatchGetReportGroups')
BatchGetReports = Action('BatchGetReports')
BatchPutCodeCoverages = Action('BatchPutCodeCoverages')
BatchPutTestCases = Action('BatchPutTestCases')
CreateProject = Action('CreateProject')
CreateReport = Action('CreateReport')
CreateReportGroup = Action('CreateReportGroup')
CreateWebhook = Action('CreateWebhook')
DeleteBuildBatch = Action('DeleteBuildBatch')
DeleteOAuthToken = Action('DeleteOAuthToken')
DeleteProject = Action('DeleteProject')
DeleteReport = Action('DeleteReport')
DeleteReportGroup = Action('DeleteReportGroup')
DeleteResourcePolicy = Action('DeleteResourcePolicy')
DeleteSourceCredentials = Action('DeleteSourceCredentials')
DeleteWebhook = Action('DeleteWebhook')
DescribeCodeCoverages = Action('DescribeCodeCoverages')
DescribeTestCases = Action('DescribeTestCases')
GetResourcePolicy = Action('GetResourcePolicy')
ImportSourceCredentials = Action('ImportSourceCredentials')
InvalidateProjectCache = Action('InvalidateProjectCache')
ListBuildBatches = Action('ListBuildBatches')
ListBuildBatchesForProject = Action('ListBuildBatchesForProject')
ListBuilds = Action('ListBuilds')
ListBuildsForProject = Action('ListBuildsForProject')
ListConnectedOAuthAccounts = Action('ListConnectedOAuthAccounts')
ListCuratedEnvironmentImages = Action('ListCuratedEnvironmentImages')
ListProjects = Action('ListProjects')
ListReportGroups = Action('ListReportGroups')
ListReports = Action('ListReports')
ListReportsForReportGroup = Action('ListReportsForReportGroup')
ListRepositories = Action('ListRepositories')
ListSharedProjects = Action('ListSharedProjects')
ListSharedReportGroups = Action('ListSharedReportGroups')
ListSourceCredentials = Action('ListSourceCredentials')
PersistOAuthToken = Action('PersistOAuthToken')
PutResourcePolicy = Action('PutResourcePolicy')
RetryBuild = Action('RetryBuild')
RetryBuildBatch = Action('RetryBuildBatch')
StartBuild = Action('StartBuild')
StartBuildBatch = Action('StartBuildBatch')
StopBuild = Action('StopBuild')
StopBuildBatch = Action('StopBuildBatch')
UpdateProject = Action('UpdateProject')
UpdateReport = Action('UpdateReport')
UpdateReportGroup = Action('UpdateReportGroup')
UpdateWebhook = Action('UpdateWebhook')
