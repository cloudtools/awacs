# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Directory Service"
prefix = "ds"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptSharedDirectory = Action("AcceptSharedDirectory")
AccessDSData = Action("AccessDSData")
AddIpRoutes = Action("AddIpRoutes")
AddRegion = Action("AddRegion")
AddTagsToResource = Action("AddTagsToResource")
AuthorizeApplication = Action("AuthorizeApplication")
CancelSchemaExtension = Action("CancelSchemaExtension")
CheckAlias = Action("CheckAlias")
ConnectDirectory = Action("ConnectDirectory")
CreateAlias = Action("CreateAlias")
CreateComputer = Action("CreateComputer")
CreateConditionalForwarder = Action("CreateConditionalForwarder")
CreateDirectory = Action("CreateDirectory")
CreateHybridAD = Action("CreateHybridAD")
CreateIdentityPoolDirectory = Action("CreateIdentityPoolDirectory")
CreateLogSubscription = Action("CreateLogSubscription")
CreateMicrosoftAD = Action("CreateMicrosoftAD")
CreateSnapshot = Action("CreateSnapshot")
CreateTrust = Action("CreateTrust")
DeleteADAssessment = Action("DeleteADAssessment")
DeleteConditionalForwarder = Action("DeleteConditionalForwarder")
DeleteDirectory = Action("DeleteDirectory")
DeleteLogSubscription = Action("DeleteLogSubscription")
DeleteSnapshot = Action("DeleteSnapshot")
DeleteTrust = Action("DeleteTrust")
DeregisterCertificate = Action("DeregisterCertificate")
DeregisterEventTopic = Action("DeregisterEventTopic")
DescribeADAssessment = Action("DescribeADAssessment")
DescribeCAEnrollmentPolicy = Action("DescribeCAEnrollmentPolicy")
DescribeCertificate = Action("DescribeCertificate")
DescribeClientAuthenticationSettings = Action("DescribeClientAuthenticationSettings")
DescribeConditionalForwarders = Action("DescribeConditionalForwarders")
DescribeDirectories = Action("DescribeDirectories")
DescribeDirectoryDataAccess = Action("DescribeDirectoryDataAccess")
DescribeDomainControllers = Action("DescribeDomainControllers")
DescribeEventTopics = Action("DescribeEventTopics")
DescribeHybridADUpdate = Action("DescribeHybridADUpdate")
DescribeLDAPSSettings = Action("DescribeLDAPSSettings")
DescribeRegions = Action("DescribeRegions")
DescribeSettings = Action("DescribeSettings")
DescribeSharedDirectories = Action("DescribeSharedDirectories")
DescribeSnapshots = Action("DescribeSnapshots")
DescribeTrusts = Action("DescribeTrusts")
DescribeUpdateDirectory = Action("DescribeUpdateDirectory")
DisableCAEnrollmentPolicy = Action("DisableCAEnrollmentPolicy")
DisableClientAuthentication = Action("DisableClientAuthentication")
DisableDirectoryDataAccess = Action("DisableDirectoryDataAccess")
DisableLDAPS = Action("DisableLDAPS")
DisableRadius = Action("DisableRadius")
DisableRoleAccess = Action("DisableRoleAccess")
DisableSso = Action("DisableSso")
EnableCAEnrollmentPolicy = Action("EnableCAEnrollmentPolicy")
EnableClientAuthentication = Action("EnableClientAuthentication")
EnableDirectoryDataAccess = Action("EnableDirectoryDataAccess")
EnableLDAPS = Action("EnableLDAPS")
EnableRadius = Action("EnableRadius")
EnableRoleAccess = Action("EnableRoleAccess")
EnableSso = Action("EnableSso")
GetAuthorizedApplicationDetails = Action("GetAuthorizedApplicationDetails")
GetDirectoryLimits = Action("GetDirectoryLimits")
GetSnapshotLimits = Action("GetSnapshotLimits")
ListADAssessments = Action("ListADAssessments")
ListAuthorizedApplications = Action("ListAuthorizedApplications")
ListCertificates = Action("ListCertificates")
ListIpRoutes = Action("ListIpRoutes")
ListLogSubscriptions = Action("ListLogSubscriptions")
ListSchemaExtensions = Action("ListSchemaExtensions")
ListTagsForResource = Action("ListTagsForResource")
RegisterCertificate = Action("RegisterCertificate")
RegisterEventTopic = Action("RegisterEventTopic")
RejectSharedDirectory = Action("RejectSharedDirectory")
RemoveIpRoutes = Action("RemoveIpRoutes")
RemoveRegion = Action("RemoveRegion")
RemoveTagsFromResource = Action("RemoveTagsFromResource")
ResetUserPassword = Action("ResetUserPassword")
RestoreFromSnapshot = Action("RestoreFromSnapshot")
ShareDirectory = Action("ShareDirectory")
StartADAssessment = Action("StartADAssessment")
StartSchemaExtension = Action("StartSchemaExtension")
UnauthorizeApplication = Action("UnauthorizeApplication")
UnshareDirectory = Action("UnshareDirectory")
UpdateAuthorizedApplication = Action("UpdateAuthorizedApplication")
UpdateConditionalForwarder = Action("UpdateConditionalForwarder")
UpdateDirectory = Action("UpdateDirectory")
UpdateDirectorySetup = Action("UpdateDirectorySetup")
UpdateHybridAD = Action("UpdateHybridAD")
UpdateNumberOfDomainControllers = Action("UpdateNumberOfDomainControllers")
UpdateRadius = Action("UpdateRadius")
UpdateSettings = Action("UpdateSettings")
UpdateTrust = Action("UpdateTrust")
VerifyTrust = Action("VerifyTrust")
