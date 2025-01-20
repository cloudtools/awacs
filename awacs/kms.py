# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Key Management Service"
prefix = "kms"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelKeyDeletion = Action("CancelKeyDeletion")
ConnectCustomKeyStore = Action("ConnectCustomKeyStore")
CreateAlias = Action("CreateAlias")
CreateCustomKeyStore = Action("CreateCustomKeyStore")
CreateGrant = Action("CreateGrant")
CreateKey = Action("CreateKey")
Decrypt = Action("Decrypt")
DeleteAlias = Action("DeleteAlias")
DeleteCustomKeyStore = Action("DeleteCustomKeyStore")
DeleteImportedKeyMaterial = Action("DeleteImportedKeyMaterial")
DeriveSharedSecret = Action("DeriveSharedSecret")
DescribeCustomKeyStores = Action("DescribeCustomKeyStores")
DescribeKey = Action("DescribeKey")
DisableKey = Action("DisableKey")
DisableKeyRotation = Action("DisableKeyRotation")
DisconnectCustomKeyStore = Action("DisconnectCustomKeyStore")
EnableKey = Action("EnableKey")
EnableKeyRotation = Action("EnableKeyRotation")
Encrypt = Action("Encrypt")
GenerateDataKey = Action("GenerateDataKey")
GenerateDataKeyPair = Action("GenerateDataKeyPair")
GenerateDataKeyPairWithoutPlaintext = Action("GenerateDataKeyPairWithoutPlaintext")
GenerateDataKeyWithoutPlaintext = Action("GenerateDataKeyWithoutPlaintext")
GenerateMac = Action("GenerateMac")
GenerateRandom = Action("GenerateRandom")
GetKeyPolicy = Action("GetKeyPolicy")
GetKeyRotationStatus = Action("GetKeyRotationStatus")
GetParametersForImport = Action("GetParametersForImport")
GetPublicKey = Action("GetPublicKey")
ImportKeyMaterial = Action("ImportKeyMaterial")
ListAliases = Action("ListAliases")
ListGrants = Action("ListGrants")
ListKeyPolicies = Action("ListKeyPolicies")
ListKeyRotations = Action("ListKeyRotations")
ListKeys = Action("ListKeys")
ListResourceTags = Action("ListResourceTags")
ListRetirableGrants = Action("ListRetirableGrants")
PutKeyPolicy = Action("PutKeyPolicy")
ReEncrypt = Action("ReEncrypt")
ReEncryptFrom = Action("ReEncryptFrom")
ReEncryptTo = Action("ReEncryptTo")
ReplicateKey = Action("ReplicateKey")
RetireGrant = Action("RetireGrant")
RevokeGrant = Action("RevokeGrant")
RotateKeyOnDemand = Action("RotateKeyOnDemand")
ScheduleKeyDeletion = Action("ScheduleKeyDeletion")
Sign = Action("Sign")
SynchronizeMultiRegionKey = Action("SynchronizeMultiRegionKey")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAlias = Action("UpdateAlias")
UpdateCustomKeyStore = Action("UpdateCustomKeyStore")
UpdateKeyDescription = Action("UpdateKeyDescription")
UpdatePrimaryRegion = Action("UpdatePrimaryRegion")
Verify = Action("Verify")
VerifyMac = Action("VerifyMac")
