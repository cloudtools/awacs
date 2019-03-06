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
DeleteReplicationJob = Action('DeleteReplicationJob')
DeleteServerCatalog = Action('DeleteServerCatalog')
DisassociateConnectors = Action('DisassociateConnectors')
GenerateChangeSet = Action('GenerateChangeSet')
GenerateTemplate = Action('GenerateTemplate')
GetApp = Action('GetApp')
GetAppLaunchConfiguration = Action('GetAppLaunchConfiguration')
GetAppReplicationConfiguration = Action('GetAppReplicationConfiguration')
GetConnectors = Action('GetConnectors')
GetReplicationJobs = Action('GetReplicationJobs')
GetReplicationRuns = Action('GetReplicationRuns')
GetServers = Action('GetServers')
ImportServerCatalog = Action('ImportServerCatalog')
LaunchApp = Action('LaunchApp')
ListApps = Action('ListApps')
PutAppLaunchConfiguration = Action('PutAppLaunchConfiguration')
PutAppReplicationConfiguration = Action('PutAppReplicationConfiguration')
StartAppReplication = Action('StartAppReplication')
StartOnDemandReplicationRun = Action('StartOnDemandReplicationRun')
StopAppReplication = Action('StopAppReplication')
TerminateApp = Action('TerminateApp')
UpdateApp = Action('UpdateApp')
UpdateReplicationJob = Action('UpdateReplicationJob')
