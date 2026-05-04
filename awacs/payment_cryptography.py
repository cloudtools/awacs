# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Payment Cryptography"
prefix = "payment-cryptography"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddKeyReplicationRegions = Action("AddKeyReplicationRegions")
AssociateMpaTeam = Action("AssociateMpaTeam")
CreateAlias = Action("CreateAlias")
CreateKey = Action("CreateKey")
DecryptData = Action("DecryptData")
DeleteAlias = Action("DeleteAlias")
DeleteKey = Action("DeleteKey")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DisableDefaultKeyReplicationRegions = Action("DisableDefaultKeyReplicationRegions")
DisassociateMpaTeam = Action("DisassociateMpaTeam")
EnableDefaultKeyReplicationRegions = Action("EnableDefaultKeyReplicationRegions")
EncryptData = Action("EncryptData")
ExportKey = Action("ExportKey")
GenerateAs2805KekValidation = Action("GenerateAs2805KekValidation")
GenerateCardValidationData = Action("GenerateCardValidationData")
GenerateMac = Action("GenerateMac")
GenerateMacEmvPinChange = Action("GenerateMacEmvPinChange")
GeneratePinData = Action("GeneratePinData")
GetAlias = Action("GetAlias")
GetCertificateSigningRequest = Action("GetCertificateSigningRequest")
GetDefaultKeyReplicationRegions = Action("GetDefaultKeyReplicationRegions")
GetKey = Action("GetKey")
GetMpaTeamAssociation = Action("GetMpaTeamAssociation")
GetParametersForExport = Action("GetParametersForExport")
GetParametersForImport = Action("GetParametersForImport")
GetPublicKeyCertificate = Action("GetPublicKeyCertificate")
GetResourcePolicy = Action("GetResourcePolicy")
ImportKey = Action("ImportKey")
ListAliases = Action("ListAliases")
ListKeys = Action("ListKeys")
ListTagsForResource = Action("ListTagsForResource")
PutResourcePolicy = Action("PutResourcePolicy")
ReEncryptData = Action("ReEncryptData")
RemoveKeyReplicationRegions = Action("RemoveKeyReplicationRegions")
RestoreKey = Action("RestoreKey")
StartKeyUsage = Action("StartKeyUsage")
StopKeyUsage = Action("StopKeyUsage")
TagResource = Action("TagResource")
TranslateKeyMaterial = Action("TranslateKeyMaterial")
TranslatePinData = Action("TranslatePinData")
UntagResource = Action("UntagResource")
UpdateAlias = Action("UpdateAlias")
VerifyAuthRequestCryptogram = Action("VerifyAuthRequestCryptogram")
VerifyCardValidationData = Action("VerifyCardValidationData")
VerifyMac = Action("VerifyMac")
VerifyPinData = Action("VerifyPinData")
