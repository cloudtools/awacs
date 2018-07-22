# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaConvert'
prefix = 'mediaconvert'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelJob = Action('CancelJob')
CreateJob = Action('CreateJob')
CreateJobTemplate = Action('CreateJobTemplate')
CreatePreset = Action('CreatePreset')
CreateQueue = Action('CreateQueue')
DeleteJobTemplate = Action('DeleteJobTemplate')
DeletePreset = Action('DeletePreset')
DeleteQueue = Action('DeleteQueue')
DescribeEndpoint = Action('DescribeEndpoint')
GetJob = Action('GetJob')
GetJobTemplate = Action('GetJobTemplate')
GetPreset = Action('GetPreset')
GetQueue = Action('GetQueue')
ListJobTemplates = Action('ListJobTemplates')
ListJobs = Action('ListJobs')
ListPresets = Action('ListPresets')
ListQueues = Action('ListQueues')
UpdateJobTemplate = Action('UpdateJobTemplate')
UpdatePreset = Action('UpdatePreset')
UpdateQueue = Action('UpdateQueue')
