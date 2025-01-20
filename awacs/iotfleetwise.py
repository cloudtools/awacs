# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IoT FleetWise"
prefix = "iotfleetwise"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateVehicle = Action("AssociateVehicle")
AssociateVehicleFleet = Action("AssociateVehicleFleet")
BatchCreateVehicle = Action("BatchCreateVehicle")
BatchUpdateVehicle = Action("BatchUpdateVehicle")
CreateCampaign = Action("CreateCampaign")
CreateDecoderManifest = Action("CreateDecoderManifest")
CreateFleet = Action("CreateFleet")
CreateModelManifest = Action("CreateModelManifest")
CreateSignalCatalog = Action("CreateSignalCatalog")
CreateStateTemplate = Action("CreateStateTemplate")
CreateVehicle = Action("CreateVehicle")
DeleteCampaign = Action("DeleteCampaign")
DeleteDecoderManifest = Action("DeleteDecoderManifest")
DeleteFleet = Action("DeleteFleet")
DeleteModelManifest = Action("DeleteModelManifest")
DeleteSignalCatalog = Action("DeleteSignalCatalog")
DeleteStateTemplate = Action("DeleteStateTemplate")
DeleteVehicle = Action("DeleteVehicle")
DisassociateVehicle = Action("DisassociateVehicle")
DisassociateVehicleFleet = Action("DisassociateVehicleFleet")
GenerateCommandPayload = Action("GenerateCommandPayload")
GetCampaign = Action("GetCampaign")
GetDecoderManifest = Action("GetDecoderManifest")
GetEncryptionConfiguration = Action("GetEncryptionConfiguration")
GetFleet = Action("GetFleet")
GetLoggingOptions = Action("GetLoggingOptions")
GetModelManifest = Action("GetModelManifest")
GetRegisterAccountStatus = Action("GetRegisterAccountStatus")
GetSignalCatalog = Action("GetSignalCatalog")
GetStateTemplate = Action("GetStateTemplate")
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
ListStateTemplates = Action("ListStateTemplates")
ListTagsForResource = Action("ListTagsForResource")
ListVehicles = Action("ListVehicles")
ListVehiclesInFleet = Action("ListVehiclesInFleet")
PutEncryptionConfiguration = Action("PutEncryptionConfiguration")
PutLoggingOptions = Action("PutLoggingOptions")
RegisterAccount = Action("RegisterAccount")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCampaign = Action("UpdateCampaign")
UpdateDecoderManifest = Action("UpdateDecoderManifest")
UpdateFleet = Action("UpdateFleet")
UpdateModelManifest = Action("UpdateModelManifest")
UpdateSignalCatalog = Action("UpdateSignalCatalog")
UpdateStateTemplate = Action("UpdateStateTemplate")
UpdateVehicle = Action("UpdateVehicle")
