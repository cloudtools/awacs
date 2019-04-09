# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Pinpoint'
prefix = 'mobiletargeting'


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
CreateCampaign = Action('CreateCampaign')
CreateExportJob = Action('CreateExportJob')
CreateImportJob = Action('CreateImportJob')
CreateSegment = Action('CreateSegment')
DeleteAdmChannel = Action('DeleteAdmChannel')
DeleteApnsChannel = Action('DeleteApnsChannel')
DeleteApnsSandboxChannel = Action('DeleteApnsSandboxChannel')
DeleteApnsVoipChannel = Action('DeleteApnsVoipChannel')
DeleteApnsVoipSandboxChannel = Action('DeleteApnsVoipSandboxChannel')
DeleteApp = Action('DeleteApp')
DeleteBaiduChannel = Action('DeleteBaiduChannel')
DeleteCampaign = Action('DeleteCampaign')
DeleteEmailChannel = Action('DeleteEmailChannel')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEventStream = Action('DeleteEventStream')
DeleteGcmChannel = Action('DeleteGcmChannel')
DeleteSegment = Action('DeleteSegment')
DeleteSmsChannel = Action('DeleteSmsChannel')
DeleteUserEndpoints = Action('DeleteUserEndpoints')
DeleteVoiceChannel = Action('DeleteVoiceChannel')
GetAdmChannel = Action('GetAdmChannel')
GetApnsChannel = Action('GetApnsChannel')
GetApnsSandboxChannel = Action('GetApnsSandboxChannel')
GetApnsVoipChannel = Action('GetApnsVoipChannel')
GetApnsVoipSandboxChannel = Action('GetApnsVoipSandboxChannel')
GetApp = Action('GetApp')
GetApplicationSettings = Action('GetApplicationSettings')
GetApps = Action('GetApps')
GetBaiduChannel = Action('GetBaiduChannel')
GetCampaign = Action('GetCampaign')
GetCampaignActivities = Action('GetCampaignActivities')
GetCampaignVersion = Action('GetCampaignVersion')
GetCampaignVersions = Action('GetCampaignVersions')
GetCampaigns = Action('GetCampaigns')
GetChannels = Action('GetChannels')
GetEmailChannel = Action('GetEmailChannel')
GetEndpoint = Action('GetEndpoint')
GetEventStream = Action('GetEventStream')
GetExportJob = Action('GetExportJob')
GetExportJobs = Action('GetExportJobs')
GetGcmChannel = Action('GetGcmChannel')
GetImportJob = Action('GetImportJob')
GetImportJobs = Action('GetImportJobs')
GetReports = Action('GetReports')
GetSegment = Action('GetSegment')
GetSegmentExportJobs = Action('GetSegmentExportJobs')
GetSegmentImportJobs = Action('GetSegmentImportJobs')
GetSegmentVersion = Action('GetSegmentVersion')
GetSegmentVersions = Action('GetSegmentVersions')
GetSegments = Action('GetSegments')
GetSmsChannel = Action('GetSmsChannel')
GetUserEndpoints = Action('GetUserEndpoints')
GetVoiceChannel = Action('GetVoiceChannel')
ListTagsForResource = Action('ListTagsForResource')
PhoneNumberValidate = Action('PhoneNumberValidate')
PutEventStream = Action('PutEventStream')
PutEvents = Action('PutEvents')
RemoveAttributes = Action('RemoveAttributes')
SendMessages = Action('SendMessages')
SendUsersMessages = Action('SendUsersMessages')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAdmChannel = Action('UpdateAdmChannel')
UpdateApnsChannel = Action('UpdateApnsChannel')
UpdateApnsSandboxChannel = Action('UpdateApnsSandboxChannel')
UpdateApnsVoipChannel = Action('UpdateApnsVoipChannel')
UpdateApnsVoipSandboxChannel = Action('UpdateApnsVoipSandboxChannel')
UpdateApplicationSettings = Action('UpdateApplicationSettings')
UpdateBaiduChannel = Action('UpdateBaiduChannel')
UpdateCampaign = Action('UpdateCampaign')
UpdateEmailChannel = Action('UpdateEmailChannel')
UpdateEndpoint = Action('UpdateEndpoint')
UpdateEndpointsBatch = Action('UpdateEndpointsBatch')
UpdateGcmChannel = Action('UpdateGcmChannel')
UpdateSegment = Action('UpdateSegment')
UpdateSmsChannel = Action('UpdateSmsChannel')
UpdateVoiceChannel = Action('UpdateVoiceChannel')
