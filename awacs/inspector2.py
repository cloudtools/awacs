# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Inspector2"
prefix = "inspector2"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateMember = Action("AssociateMember")
BatchAssociateCodeSecurityScanConfiguration = Action(
    "BatchAssociateCodeSecurityScanConfiguration"
)
BatchDisassociateCodeSecurityScanConfiguration = Action(
    "BatchDisassociateCodeSecurityScanConfiguration"
)
BatchGetAccountStatus = Action("BatchGetAccountStatus")
BatchGetCodeSnippet = Action("BatchGetCodeSnippet")
BatchGetFindingDetails = Action("BatchGetFindingDetails")
BatchGetFreeTrialInfo = Action("BatchGetFreeTrialInfo")
BatchGetMemberEc2DeepInspectionStatus = Action("BatchGetMemberEc2DeepInspectionStatus")
BatchUpdateMemberEc2DeepInspectionStatus = Action(
    "BatchUpdateMemberEc2DeepInspectionStatus"
)
CancelFindingsReport = Action("CancelFindingsReport")
CancelSbomExport = Action("CancelSbomExport")
CreateCisScanConfiguration = Action("CreateCisScanConfiguration")
CreateCodeSecurityIntegration = Action("CreateCodeSecurityIntegration")
CreateCodeSecurityScanConfiguration = Action("CreateCodeSecurityScanConfiguration")
CreateFilter = Action("CreateFilter")
CreateFindingsReport = Action("CreateFindingsReport")
CreateSbomExport = Action("CreateSbomExport")
DeleteCisScanConfiguration = Action("DeleteCisScanConfiguration")
DeleteCodeSecurityIntegration = Action("DeleteCodeSecurityIntegration")
DeleteCodeSecurityScanConfiguration = Action("DeleteCodeSecurityScanConfiguration")
DeleteFilter = Action("DeleteFilter")
DescribeOrganizationConfiguration = Action("DescribeOrganizationConfiguration")
Disable = Action("Disable")
DisableDelegatedAdminAccount = Action("DisableDelegatedAdminAccount")
DisassociateMember = Action("DisassociateMember")
Enable = Action("Enable")
EnableDelegatedAdminAccount = Action("EnableDelegatedAdminAccount")
GetCisScanReport = Action("GetCisScanReport")
GetCisScanResultDetails = Action("GetCisScanResultDetails")
GetClustersForImage = Action("GetClustersForImage")
GetCodeSecurityIntegration = Action("GetCodeSecurityIntegration")
GetCodeSecurityScan = Action("GetCodeSecurityScan")
GetCodeSecurityScanConfiguration = Action("GetCodeSecurityScanConfiguration")
GetConfiguration = Action("GetConfiguration")
GetDelegatedAdminAccount = Action("GetDelegatedAdminAccount")
GetEc2DeepInspectionConfiguration = Action("GetEc2DeepInspectionConfiguration")
GetEncryptionKey = Action("GetEncryptionKey")
GetFindingsReportStatus = Action("GetFindingsReportStatus")
GetMember = Action("GetMember")
GetSbomExport = Action("GetSbomExport")
ListAccountPermissions = Action("ListAccountPermissions")
ListCisScanConfigurations = Action("ListCisScanConfigurations")
ListCisScanResultsAggregatedByChecks = Action("ListCisScanResultsAggregatedByChecks")
ListCisScanResultsAggregatedByTargetResource = Action(
    "ListCisScanResultsAggregatedByTargetResource"
)
ListCisScans = Action("ListCisScans")
ListCodeSecurityIntegrations = Action("ListCodeSecurityIntegrations")
ListCodeSecurityScanConfigurationAssociations = Action(
    "ListCodeSecurityScanConfigurationAssociations"
)
ListCodeSecurityScanConfigurations = Action("ListCodeSecurityScanConfigurations")
ListCoverage = Action("ListCoverage")
ListCoverageStatistics = Action("ListCoverageStatistics")
ListDelegatedAdminAccounts = Action("ListDelegatedAdminAccounts")
ListFilters = Action("ListFilters")
ListFindingAggregations = Action("ListFindingAggregations")
ListFindings = Action("ListFindings")
ListMembers = Action("ListMembers")
ListTagsForResource = Action("ListTagsForResource")
ListUsageTotals = Action("ListUsageTotals")
ResetEncryptionKey = Action("ResetEncryptionKey")
SearchVulnerabilities = Action("SearchVulnerabilities")
SendCisSessionHealth = Action("SendCisSessionHealth")
SendCisSessionTelemetry = Action("SendCisSessionTelemetry")
StartCisSession = Action("StartCisSession")
StartCodeSecurityScan = Action("StartCodeSecurityScan")
StopCisSession = Action("StopCisSession")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateCisScanConfiguration = Action("UpdateCisScanConfiguration")
UpdateCodeSecurityIntegration = Action("UpdateCodeSecurityIntegration")
UpdateCodeSecurityScanConfiguration = Action("UpdateCodeSecurityScanConfiguration")
UpdateConfiguration = Action("UpdateConfiguration")
UpdateEc2DeepInspectionConfiguration = Action("UpdateEc2DeepInspectionConfiguration")
UpdateEncryptionKey = Action("UpdateEncryptionKey")
UpdateFilter = Action("UpdateFilter")
UpdateOrgEc2DeepInspectionConfiguration = Action(
    "UpdateOrgEc2DeepInspectionConfiguration"
)
UpdateOrganizationConfiguration = Action("UpdateOrganizationConfiguration")
