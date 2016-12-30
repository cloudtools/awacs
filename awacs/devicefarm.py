# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Device Farm'
prefix = 'devicefarm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDevicePool = Action('CreateDevicePool')
CreateNetworkProfile = Action('CreateNetworkProfile')
CreateProject = Action('CreateProject')
CreateRemoteAccessSession = Action('CreateRemoteAccessSession')
CreateUpload = Action('CreateUpload')
DeleteDevicePool = Action('DeleteDevicePool')
DeleteNetworkProfile = Action('DeleteNetworkProfile')
DeleteProject = Action('DeleteProject')
DeleteRemoteAccessSession = Action('DeleteRemoteAccessSession')
DeleteRun = Action('DeleteRun')
DeleteUpload = Action('DeleteUpload')
GetAccountSettings = Action('GetAccountSettings')
GetDevice = Action('GetDevice')
GetDevicePool = Action('GetDevicePool')
GetDevicePoolCompatibility = Action('GetDevicePoolCompatibility')
GetJob = Action('GetJob')
GetNetworkProfile = Action('GetNetworkProfile')
GetOfferingStatus = Action('GetOfferingStatus')
GetProject = Action('GetProject')
GetRemoteAccessSession = Action('GetRemoteAccessSession')
GetRun = Action('GetRun')
GetSuite = Action('GetSuite')
GetTest = Action('GetTest')
GetUpload = Action('GetUpload')
InstallToRemoteAccessSession = Action('InstallToRemoteAccessSession')
ListArtifacts = Action('ListArtifacts')
ListDevicePools = Action('ListDevicePools')
ListDevices = Action('ListDevices')
ListJobs = Action('ListJobs')
ListNetworkProfiles = Action('ListNetworkProfiles')
ListOfferingTransactions = Action('ListOfferingTransactions')
ListOfferings = Action('ListOfferings')
ListProjects = Action('ListProjects')
ListRemoteAccessSessions = Action('ListRemoteAccessSessions')
ListRuns = Action('ListRuns')
ListSamples = Action('ListSamples')
ListSuites = Action('ListSuites')
ListTests = Action('ListTests')
ListUniqueProblems = Action('ListUniqueProblems')
ListUploads = Action('ListUploads')
PurchaseOffering = Action('PurchaseOffering')
RenewOffering = Action('RenewOffering')
ScheduleRun = Action('ScheduleRun')
StopRemoteAccessSession = Action('StopRemoteAccessSession')
StopRun = Action('StopRun')
UpdateDevicePool = Action('UpdateDevicePool')
UpdateNetworkProfile = Action('UpdateNetworkProfile')
UpdateProject = Action('UpdateProject')
