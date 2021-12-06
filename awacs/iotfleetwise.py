# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT FleetWise"
prefix = "iotfleetwise"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateVehicle = Action("AssociateVehicle")
CreateCampaign = Action("CreateCampaign")
CreateDecoderManifest = Action("CreateDecoderManifest")
CreateFleet = Action("CreateFleet")
CreateModelManifest = Action("CreateModelManifest")
CreateSignalCatalog = Action("CreateSignalCatalog")
CreateVehicle = Action("CreateVehicle")
DeleteCampaign = Action("DeleteCampaign")
DeleteDecoderManifest = Action("DeleteDecoderManifest")
DeleteFleet = Action("DeleteFleet")
DeleteModelManifest = Action("DeleteModelManifest")
DeleteSignalCatalog = Action("DeleteSignalCatalog")
DeleteVehicle = Action("DeleteVehicle")
DisassociateVehicle = Action("DisassociateVehicle")
GetCampaign = Action("GetCampaign")
GetDecoderManifest = Action("GetDecoderManifest")
GetFleet = Action("GetFleet")
GetModelManifest = Action("GetModelManifest")
GetRegisterAccountStatus = Action("GetRegisterAccountStatus")
GetSignalCatalog = Action("GetSignalCatalog")
GetVehicle = Action("GetVehicle")
GetVehicleStatus = Action("GetVehicleStatus")
ImportDecoderManifest = Action("ImportDecoderManifest")
ImportSignalCatalog = Action("ImportSignalCatalog")
ListCampaigns = Action("ListCampaigns")
ListDecoderManifestNetworkInterfaces = Action("ListDecoderManifestNetworkInterfaces")
ListDecoderManifestSignals = Action("ListDecoderManifestSignals")
ListDecoderManifests = Action("ListDecoderManifests")
ListFleets = Action("ListFleets")
ListFleetsForVehicle = Action("ListFleetsForVehicle")
ListModelManifestNodes = Action("ListModelManifestNodes")
ListModelManifests = Action("ListModelManifests")
ListSignalCatalogNodes = Action("ListSignalCatalogNodes")
ListSignalCatalogs = Action("ListSignalCatalogs")
ListVehicles = Action("ListVehicles")
ListVehiclesInFleet = Action("ListVehiclesInFleet")
RegisterAccount = Action("RegisterAccount")
UpdateCampaign = Action("UpdateCampaign")
UpdateDecoderManifest = Action("UpdateDecoderManifest")
UpdateFleet = Action("UpdateFleet")
UpdateModelManifest = Action("UpdateModelManifest")
UpdateSignalCatalog = Action("UpdateSignalCatalog")
UpdateVehicle = Action("UpdateVehicle")
