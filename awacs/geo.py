# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Location'
prefix = 'geo'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateTrackerConsumer = Action('AssociateTrackerConsumer')
BatchDeleteGeofence = Action('BatchDeleteGeofence')
BatchEvaluateGeofences = Action('BatchEvaluateGeofences')
BatchGetDevicePosition = Action('BatchGetDevicePosition')
BatchPutGeofence = Action('BatchPutGeofence')
BatchUpdateDevicePosition = Action('BatchUpdateDevicePosition')
CreateGeofenceCollection = Action('CreateGeofenceCollection')
CreateMap = Action('CreateMap')
CreatePlaceIndex = Action('CreatePlaceIndex')
CreateTracker = Action('CreateTracker')
DeleteGeofenceCollection = Action('DeleteGeofenceCollection')
DeleteMap = Action('DeleteMap')
DeletePlaceIndex = Action('DeletePlaceIndex')
DeleteTracker = Action('DeleteTracker')
DescribeGeofenceCollection = Action('DescribeGeofenceCollection')
DescribeMap = Action('DescribeMap')
DescribePlaceIndex = Action('DescribePlaceIndex')
DescribeTracker = Action('DescribeTracker')
DisassociateTrackerConsumer = Action('DisassociateTrackerConsumer')
GetDevicePosition = Action('GetDevicePosition')
GetDevicePositionHistory = Action('GetDevicePositionHistory')
GetGeofence = Action('GetGeofence')
GetMapGlyphs = Action('GetMapGlyphs')
GetMapSprites = Action('GetMapSprites')
GetMapStyleDescriptor = Action('GetMapStyleDescriptor')
GetMapTile = Action('GetMapTile')
GetMapTileJson = Action('GetMapTileJson')
ListGeofenceCollections = Action('ListGeofenceCollections')
ListGeofences = Action('ListGeofences')
ListMaps = Action('ListMaps')
ListPlaceIndexes = Action('ListPlaceIndexes')
ListTrackerConsumers = Action('ListTrackerConsumers')
ListTrackers = Action('ListTrackers')
PutGeofence = Action('PutGeofence')
SearchPlaceIndexForPosition = Action('SearchPlaceIndexForPosition')
SearchPlaceIndexForText = Action('SearchPlaceIndexForText')
UpdateGeofenceCollection = Action('UpdateGeofenceCollection')
UpdateTracker = Action('UpdateTracker')
