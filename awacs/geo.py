# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Location"
prefix = "geo"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateTrackerConsumer = Action("AssociateTrackerConsumer")
BatchDeleteDevicePositionHistory = Action("BatchDeleteDevicePositionHistory")
BatchDeleteGeofence = Action("BatchDeleteGeofence")
BatchEvaluateGeofences = Action("BatchEvaluateGeofences")
BatchGetDevicePosition = Action("BatchGetDevicePosition")
BatchPutGeofence = Action("BatchPutGeofence")
BatchUpdateDevicePosition = Action("BatchUpdateDevicePosition")
CalculateRoute = Action("CalculateRoute")
CreateGeofenceCollection = Action("CreateGeofenceCollection")
CreateMap = Action("CreateMap")
CreatePlaceIndex = Action("CreatePlaceIndex")
CreateRouteCalculator = Action("CreateRouteCalculator")
CreateTracker = Action("CreateTracker")
DeleteGeofenceCollection = Action("DeleteGeofenceCollection")
DeleteMap = Action("DeleteMap")
DeletePlaceIndex = Action("DeletePlaceIndex")
DeleteRouteCalculator = Action("DeleteRouteCalculator")
DeleteTracker = Action("DeleteTracker")
DescribeGeofenceCollection = Action("DescribeGeofenceCollection")
DescribeMap = Action("DescribeMap")
DescribePlaceIndex = Action("DescribePlaceIndex")
DescribeRouteCalculator = Action("DescribeRouteCalculator")
DescribeTracker = Action("DescribeTracker")
DisassociateTrackerConsumer = Action("DisassociateTrackerConsumer")
GetDevicePosition = Action("GetDevicePosition")
GetDevicePositionHistory = Action("GetDevicePositionHistory")
GetGeofence = Action("GetGeofence")
GetMapGlyphs = Action("GetMapGlyphs")
GetMapSprites = Action("GetMapSprites")
GetMapStyleDescriptor = Action("GetMapStyleDescriptor")
GetMapTile = Action("GetMapTile")
GetMapTileJson = Action("GetMapTileJson")
ListDevicePositions = Action("ListDevicePositions")
ListGeofenceCollections = Action("ListGeofenceCollections")
ListGeofences = Action("ListGeofences")
ListMaps = Action("ListMaps")
ListPlaceIndexes = Action("ListPlaceIndexes")
ListRouteCalculators = Action("ListRouteCalculators")
ListTagsForResource = Action("ListTagsForResource")
ListTrackerConsumers = Action("ListTrackerConsumers")
ListTrackers = Action("ListTrackers")
PutGeofence = Action("PutGeofence")
SearchPlaceIndexForPosition = Action("SearchPlaceIndexForPosition")
SearchPlaceIndexForText = Action("SearchPlaceIndexForText")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGeofenceCollection = Action("UpdateGeofenceCollection")
UpdateTracker = Action("UpdateTracker")
