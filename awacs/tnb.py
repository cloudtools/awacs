# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Telco Network Builder"
prefix = "tnb"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelSolNetworkOperation = Action("CancelSolNetworkOperation")
CreateSolFunctionPackage = Action("CreateSolFunctionPackage")
CreateSolNetworkInstance = Action("CreateSolNetworkInstance")
CreateSolNetworkPackage = Action("CreateSolNetworkPackage")
DeleteSolFunctionPackage = Action("DeleteSolFunctionPackage")
DeleteSolNetworkInstance = Action("DeleteSolNetworkInstance")
DeleteSolNetworkPackage = Action("DeleteSolNetworkPackage")
GetSolFunctionInstance = Action("GetSolFunctionInstance")
GetSolFunctionPackage = Action("GetSolFunctionPackage")
GetSolFunctionPackageContent = Action("GetSolFunctionPackageContent")
GetSolFunctionPackageDescriptor = Action("GetSolFunctionPackageDescriptor")
GetSolNetworkInstance = Action("GetSolNetworkInstance")
GetSolNetworkOperation = Action("GetSolNetworkOperation")
GetSolNetworkPackage = Action("GetSolNetworkPackage")
GetSolNetworkPackageContent = Action("GetSolNetworkPackageContent")
GetSolNetworkPackageDescriptor = Action("GetSolNetworkPackageDescriptor")
InstantiateSolNetworkInstance = Action("InstantiateSolNetworkInstance")
ListSolFunctionInstances = Action("ListSolFunctionInstances")
ListSolFunctionPackages = Action("ListSolFunctionPackages")
ListSolNetworkInstances = Action("ListSolNetworkInstances")
ListSolNetworkOperations = Action("ListSolNetworkOperations")
ListSolNetworkPackages = Action("ListSolNetworkPackages")
ListTagsForResource = Action("ListTagsForResource")
PutSolFunctionPackageContent = Action("PutSolFunctionPackageContent")
PutSolNetworkPackageContent = Action("PutSolNetworkPackageContent")
TagResource = Action("TagResource")
TerminateSolNetworkInstance = Action("TerminateSolNetworkInstance")
UntagResource = Action("UntagResource")
UpdateSolFunctionPackage = Action("UpdateSolFunctionPackage")
UpdateSolNetworkInstance = Action("UpdateSolNetworkInstance")
UpdateSolNetworkPackage = Action("UpdateSolNetworkPackage")
ValidateSolFunctionPackageContent = Action("ValidateSolFunctionPackageContent")
ValidateSolNetworkPackageContent = Action("ValidateSolNetworkPackageContent")
