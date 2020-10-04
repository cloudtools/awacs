# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Ground Station'
prefix = 'groundstation'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelContact = Action('CancelContact')
CreateConfig = Action('CreateConfig')
CreateDataflowEndpointGroup = Action('CreateDataflowEndpointGroup')
CreateMissionProfile = Action('CreateMissionProfile')
DeleteConfig = Action('DeleteConfig')
DeleteDataflowEndpointGroup = Action('DeleteDataflowEndpointGroup')
DeleteMissionProfile = Action('DeleteMissionProfile')
DescribeContact = Action('DescribeContact')
GetConfig = Action('GetConfig')
GetDataflowEndpointGroup = Action('GetDataflowEndpointGroup')
GetMinuteUsage = Action('GetMinuteUsage')
GetMissionProfile = Action('GetMissionProfile')
GetSatellite = Action('GetSatellite')
ListConfigs = Action('ListConfigs')
ListContacts = Action('ListContacts')
ListDataflowEndpointGroups = Action('ListDataflowEndpointGroups')
ListGroundStations = Action('ListGroundStations')
ListMissionProfiles = Action('ListMissionProfiles')
ListSatellites = Action('ListSatellites')
ListTagsForResource = Action('ListTagsForResource')
ReserveContact = Action('ReserveContact')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateConfig = Action('UpdateConfig')
UpdateMissionProfile = Action('UpdateMissionProfile')
