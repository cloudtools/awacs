# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Elastic Transcoder'
prefix = 'elastictranscoder'

CancelJob = Action(prefix, 'CancelJob')
CreateJob = Action(prefix, 'CreateJob')
CreatePipeline = Action(prefix, 'CreatePipeline')
CreatePreset = Action(prefix, 'CreatePreset')
DeletePipeline = Action(prefix, 'DeletePipeline')
DeletePreset = Action(prefix, 'DeletePreset')
ListJobsByPipeline = Action(prefix, 'ListJobsByPipeline')
ListJobsByStatus = Action(prefix, 'ListJobsByStatus')
ListPipelines = Action(prefix, 'ListPipelines')
ListPresets = Action(prefix, 'ListPresets')
ReadJob = Action(prefix, 'ReadJob')
ReadPipeline = Action(prefix, 'ReadPipeline')
ReadPreset = Action(prefix, 'ReadPreset')
TestRole = Action(prefix, 'TestRole')
UpdatePipeline = Action(prefix, 'UpdatePipeline')
UpdatePipelineNotifications = \
    Action(prefix, 'UpdatePipelineNotifications')
UpdatePipelineStatus = Action(prefix, 'UpdatePipelineStatus')
