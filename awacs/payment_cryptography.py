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


CreateAlias = Action("CreateAlias")
CreateKey = Action("CreateKey")
DecryptData = Action("DecryptData")
DeleteAlias = Action("DeleteAlias")
DeleteKey = Action("DeleteKey")
EncryptData = Action("EncryptData")
ExportKey = Action("ExportKey")
GenerateCardValidationData = Action("GenerateCardValidationData")
GenerateMac = Action("GenerateMac")
GenerateMacEmvPinChange = Action("GenerateMacEmvPinChange")
GeneratePinData = Action("GeneratePinData")
GetAlias = Action("GetAlias")
GetKey = Action("GetKey")
GetParametersForExport = Action("GetParametersForExport")
GetParametersForImport = Action("GetParametersForImport")
GetPublicKeyCertificate = Action("GetPublicKeyCertificate")
ImportKey = Action("ImportKey")
ListAliases = Action("ListAliases")
ListKeys = Action("ListKeys")
ListTagsForResource = Action("ListTagsForResource")
ReEncryptData = Action("ReEncryptData")
RestoreKey = Action("RestoreKey")
StartKeyUsage = Action("StartKeyUsage")
StopKeyUsage = Action("StopKeyUsage")
TagResource = Action("TagResource")
TranslatePinData = Action("TranslatePinData")
UntagResource = Action("UntagResource")
UpdateAlias = Action("UpdateAlias")
VerifyAuthRequestCryptogram = Action("VerifyAuthRequestCryptogram")
VerifyCardValidationData = Action("VerifyCardValidationData")
VerifyMac = Action("VerifyMac")
VerifyPinData = Action("VerifyPinData")
