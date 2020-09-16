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
CreateInstanceProfile = Action('CreateInstanceProfile')
CreateNetworkProfile = Action('CreateNetworkProfile')
CreateProject = Action('CreateProject')
CreateRemoteAccessSession = Action('CreateRemoteAccessSession')
CreateTestGridProject = Action('CreateTestGridProject')
CreateTestGridUrl = Action('CreateTestGridUrl')
CreateUpload = Action('CreateUpload')
CreateVPCEConfiguration = Action('CreateVPCEConfiguration')
DeleteDevicePool = Action('DeleteDevicePool')
DeleteInstanceProfile = Action('DeleteInstanceProfile')
DeleteNetworkProfile = Action('DeleteNetworkProfile')
DeleteProject = Action('DeleteProject')
DeleteRemoteAccessSession = Action('DeleteRemoteAccessSession')
DeleteRun = Action('DeleteRun')
DeleteTestGridProject = Action('DeleteTestGridProject')
DeleteUpload = Action('DeleteUpload')
DeleteVPCEConfiguration = Action('DeleteVPCEConfiguration')
GetAccountSettings = Action('GetAccountSettings')
GetDevice = Action('GetDevice')
GetDeviceInstance = Action('GetDeviceInstance')
GetDevicePool = Action('GetDevicePool')
GetDevicePoolCompatibility = Action('GetDevicePoolCompatibility')
GetInstanceProfile = Action('GetInstanceProfile')
GetJob = Action('GetJob')
GetNetworkProfile = Action('GetNetworkProfile')
GetOfferingStatus = Action('GetOfferingStatus')
GetProject = Action('GetProject')
GetRemoteAccessSession = Action('GetRemoteAccessSession')
GetRun = Action('GetRun')
GetSuite = Action('GetSuite')
GetTest = Action('GetTest')
GetTestGridProject = Action('GetTestGridProject')
GetTestGridSession = Action('GetTestGridSession')
GetUpload = Action('GetUpload')
GetVPCEConfiguration = Action('GetVPCEConfiguration')
InstallToRemoteAccessSession = Action('InstallToRemoteAccessSession')
ListArtifacts = Action('ListArtifacts')
ListDeviceInstances = Action('ListDeviceInstances')
ListDevicePools = Action('ListDevicePools')
ListDevices = Action('ListDevices')
ListInstanceProfiles = Action('ListInstanceProfiles')
ListJobs = Action('ListJobs')
ListNetworkProfiles = Action('ListNetworkProfiles')
ListOfferingPromotions = Action('ListOfferingPromotions')
ListOfferingTransactions = Action('ListOfferingTransactions')
ListOfferings = Action('ListOfferings')
ListProjects = Action('ListProjects')
ListRemoteAccessSessions = Action('ListRemoteAccessSessions')
ListRuns = Action('ListRuns')
ListSamples = Action('ListSamples')
ListSuites = Action('ListSuites')
ListTagsForResource = Action('ListTagsForResource')
ListTestGridProjects = Action('ListTestGridProjects')
ListTestGridSessionActions = Action('ListTestGridSessionActions')
ListTestGridSessionArtifacts = Action('ListTestGridSessionArtifacts')
ListTestGridSessions = Action('ListTestGridSessions')
ListTests = Action('ListTests')
ListUniqueProblems = Action('ListUniqueProblems')
ListUploads = Action('ListUploads')
ListVPCEConfigurations = Action('ListVPCEConfigurations')
PurchaseOffering = Action('PurchaseOffering')
RenewOffering = Action('RenewOffering')
ScheduleRun = Action('ScheduleRun')
StopJob = Action('StopJob')
StopRemoteAccessSession = Action('StopRemoteAccessSession')
StopRun = Action('StopRun')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDeviceInstance = Action('UpdateDeviceInstance')
UpdateDevicePool = Action('UpdateDevicePool')
UpdateInstanceProfile = Action('UpdateInstanceProfile')
UpdateNetworkProfile = Action('UpdateNetworkProfile')
UpdateProject = Action('UpdateProject')
UpdateTestGridProject = Action('UpdateTestGridProject')
UpdateUpload = Action('UpdateUpload')
UpdateVPCEConfiguration = Action('UpdateVPCEConfiguration')
