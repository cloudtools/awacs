# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic Transcoder'
prefix = 'elastictranscoder'


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
CreatePipeline = Action('CreatePipeline')
CreatePreset = Action('CreatePreset')
DeletePipeline = Action('DeletePipeline')
DeletePreset = Action('DeletePreset')
ListJobsByPipeline = Action('ListJobsByPipeline')
ListJobsByStatus = Action('ListJobsByStatus')
ListPipelines = Action('ListPipelines')
ListPresets = Action('ListPresets')
ReadJob = Action('ReadJob')
ReadPipeline = Action('ReadPipeline')
ReadPreset = Action('ReadPreset')
TestRole = Action('TestRole')
UpdatePipeline = Action('UpdatePipeline')
UpdatePipelineNotifications = Action('UpdatePipelineNotifications')
UpdatePipelineStatus = Action('UpdatePipelineStatus')
