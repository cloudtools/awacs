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


CreateCampaign = Action('CreateCampaign')
CreateImportJob = Action('CreateImportJob')
CreateSegment = Action('CreateSegment')
DeleteAdmChannel = Action('DeleteAdmChannel')
DeleteApnsChannel = Action('DeleteApnsChannel')
DeleteApnsSandboxChannel = Action('DeleteApnsSandboxChannel')
DeleteCampaign = Action('DeleteCampaign')
DeleteGcmChannel = Action('DeleteGcmChannel')
DeleteSegment = Action('DeleteSegment')
GetAdmChannel = Action('GetAdmChannel')
GetApnsChannel = Action('GetApnsChannel')
GetApnsSandboxChannel = Action('GetApnsSandboxChannel')
GetApplicationSettings = Action('GetApplicationSettings')
GetCampaign = Action('GetCampaign')
GetCampaignActivities = Action('GetCampaignActivities')
GetCampaignVersion = Action('GetCampaignVersion')
GetCampaignVersions = Action('GetCampaignVersions')
GetCampaigns = Action('GetCampaigns')
GetEndpoint = Action('GetEndpoint')
GetGcmChannel = Action('GetGcmChannel')
GetImportJob = Action('GetImportJob')
GetImportJobs = Action('GetImportJobs')
GetReports = Action('GetReports')
GetSegment = Action('GetSegment')
GetSegmentImportJobs = Action('GetSegmentImportJobs')
GetSegmentVersion = Action('GetSegmentVersion')
GetSegmentVersions = Action('GetSegmentVersions')
GetSegments = Action('GetSegments')
UpdateAdmChannel = Action('UpdateAdmChannel')
UpdateApnsChannel = Action('UpdateApnsChannel')
UpdateApnsSandboxChannel = Action('UpdateApnsSandboxChannel')
UpdateApplicationSettings = Action('UpdateApplicationSettings')
UpdateCampaign = Action('UpdateCampaign')
UpdateEndpoint = Action('UpdateEndpoint')
UpdateEndpointsBatch = Action('UpdateEndpointsBatch')
UpdateGcmChannel = Action('UpdateGcmChannel')
UpdateSegment = Action('UpdateSegment')
