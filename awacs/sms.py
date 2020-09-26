# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Server Migration Service'
prefix = 'sms'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApp = Action('CreateApp')
CreateReplicationJob = Action('CreateReplicationJob')
DeleteApp = Action('DeleteApp')
DeleteAppLaunchConfiguration = Action('DeleteAppLaunchConfiguration')
DeleteAppReplicationConfiguration = \
    Action('DeleteAppReplicationConfiguration')
DeleteAppValidationConfiguration = \
    Action('DeleteAppValidationConfiguration')
DeleteReplicationJob = Action('DeleteReplicationJob')
DeleteServerCatalog = Action('DeleteServerCatalog')
DisassociateConnector = Action('DisassociateConnector')
DisassociateConnectors = Action('DisassociateConnectors')
GenerateChangeSet = Action('GenerateChangeSet')
GenerateTemplate = Action('GenerateTemplate')
GetApp = Action('GetApp')
GetAppLaunchConfiguration = Action('GetAppLaunchConfiguration')
GetAppReplicationConfiguration = Action('GetAppReplicationConfiguration')
GetAppValidationConfiguration = Action('GetAppValidationConfiguration')
GetAppValidationOutput = Action('GetAppValidationOutput')
GetConnectors = Action('GetConnectors')
GetMessages = Action('GetMessages')
GetReplicationJobs = Action('GetReplicationJobs')
GetReplicationRuns = Action('GetReplicationRuns')
GetServers = Action('GetServers')
ImportAppCatalog = Action('ImportAppCatalog')
ImportServerCatalog = Action('ImportServerCatalog')
LaunchApp = Action('LaunchApp')
ListApps = Action('ListApps')
NotifyAppValidationOutput = Action('NotifyAppValidationOutput')
PutAppLaunchConfiguration = Action('PutAppLaunchConfiguration')
PutAppReplicationConfiguration = Action('PutAppReplicationConfiguration')
PutAppValidationConfiguration = Action('PutAppValidationConfiguration')
SendMessage = Action('SendMessage')
StartAppReplication = Action('StartAppReplication')
StartOnDemandAppReplication = Action('StartOnDemandAppReplication')
StartOnDemandReplicationRun = Action('StartOnDemandReplicationRun')
StopAppReplication = Action('StopAppReplication')
TerminateApp = Action('TerminateApp')
UpdateApp = Action('UpdateApp')
UpdateReplicationJob = Action('UpdateReplicationJob')
