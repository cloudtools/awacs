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
CreateProject = Action('CreateProject')
CreateUpload = Action('CreateUpload')
GetDevice = Action('GetDevice')
GetDevicePool = Action('GetDevicePool')
GetDevicePoolCompatibility = Action('GetDevicePoolCompatibility')
GetJob = Action('GetJob')
GetProject = Action('GetProject')
GetRun = Action('GetRun')
GetSuite = Action('GetSuite')
GetTest = Action('GetTest')
GetUpload = Action('GetUpload')
ListArtifacts = Action('ListArtifacts')
ListDevicePools = Action('ListDevicePools')
ListDevices = Action('ListDevices')
ListJobs = Action('ListJobs')
ListProjects = Action('ListProjects')
ListRuns = Action('ListRuns')
ListSamples = Action('ListSamples')
ListSuites = Action('ListSuites')
ListTests = Action('ListTests')
ListUniqueProblems = Action('ListUniqueProblems')
ListUploads = Action('ListUploads')
ScheduleRun = Action('ScheduleRun')
