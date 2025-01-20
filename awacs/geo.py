# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Location"
prefix = "geo"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
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
CalculateRouteMatrix = Action("CalculateRouteMatrix")
CreateGeofenceCollection = Action("CreateGeofenceCollection")
CreateKey = Action("CreateKey")
CreateMap = Action("CreateMap")
CreatePlaceIndex = Action("CreatePlaceIndex")
CreateRouteCalculator = Action("CreateRouteCalculator")
CreateTracker = Action("CreateTracker")
DeleteGeofenceCollection = Action("DeleteGeofenceCollection")
DeleteKey = Action("DeleteKey")
DeleteMap = Action("DeleteMap")
DeletePlaceIndex = Action("DeletePlaceIndex")
DeleteRouteCalculator = Action("DeleteRouteCalculator")
DeleteTracker = Action("DeleteTracker")
DescribeGeofenceCollection = Action("DescribeGeofenceCollection")
DescribeKey = Action("DescribeKey")
DescribeMap = Action("DescribeMap")
DescribePlaceIndex = Action("DescribePlaceIndex")
DescribeRouteCalculator = Action("DescribeRouteCalculator")
DescribeTracker = Action("DescribeTracker")
DisassociateTrackerConsumer = Action("DisassociateTrackerConsumer")
ForecastGeofenceEvents = Action("ForecastGeofenceEvents")
GetDevicePosition = Action("GetDevicePosition")
GetDevicePositionHistory = Action("GetDevicePositionHistory")
GetGeofence = Action("GetGeofence")
GetMapGlyphs = Action("GetMapGlyphs")
GetMapSprites = Action("GetMapSprites")
GetMapStyleDescriptor = Action("GetMapStyleDescriptor")
GetMapTile = Action("GetMapTile")
GetMapTileJson = Action("GetMapTileJson")
GetPlace = Action("GetPlace")
ListDevicePositions = Action("ListDevicePositions")
ListGeofenceCollections = Action("ListGeofenceCollections")
ListGeofences = Action("ListGeofences")
ListKeys = Action("ListKeys")
ListMaps = Action("ListMaps")
ListPlaceIndexes = Action("ListPlaceIndexes")
ListRouteCalculators = Action("ListRouteCalculators")
ListTagsForResource = Action("ListTagsForResource")
ListTrackerConsumers = Action("ListTrackerConsumers")
ListTrackers = Action("ListTrackers")
PutGeofence = Action("PutGeofence")
SearchPlaceIndexForPosition = Action("SearchPlaceIndexForPosition")
SearchPlaceIndexForSuggestions = Action("SearchPlaceIndexForSuggestions")
SearchPlaceIndexForText = Action("SearchPlaceIndexForText")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGeofenceCollection = Action("UpdateGeofenceCollection")
UpdateKey = Action("UpdateKey")
UpdateMap = Action("UpdateMap")
UpdatePlaceIndex = Action("UpdatePlaceIndex")
UpdateRouteCalculator = Action("UpdateRouteCalculator")
UpdateTracker = Action("UpdateTracker")
VerifyDevicePosition = Action("VerifyDevicePosition")
