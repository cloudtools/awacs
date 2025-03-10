# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SES"
prefix = "ses"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
BatchGetMetricData = Action("BatchGetMetricData")
CancelExportJob = Action("CancelExportJob")
CloneReceiptRuleSet = Action("CloneReceiptRuleSet")
CreateAddonInstance = Action("CreateAddonInstance")
CreateAddonSubscription = Action("CreateAddonSubscription")
CreateAddressList = Action("CreateAddressList")
CreateAddressListImportJob = Action("CreateAddressListImportJob")
CreateArchive = Action("CreateArchive")
CreateConfigurationSet = Action("CreateConfigurationSet")
CreateConfigurationSetEventDestination = Action(
    "CreateConfigurationSetEventDestination"
)
CreateConfigurationSetTrackingOptions = Action("CreateConfigurationSetTrackingOptions")
CreateContact = Action("CreateContact")
CreateContactList = Action("CreateContactList")
CreateCustomVerificationEmailTemplate = Action("CreateCustomVerificationEmailTemplate")
CreateDedicatedIpPool = Action("CreateDedicatedIpPool")
CreateDeliverabilityTestReport = Action("CreateDeliverabilityTestReport")
CreateEmailIdentity = Action("CreateEmailIdentity")
CreateEmailIdentityPolicy = Action("CreateEmailIdentityPolicy")
CreateEmailTemplate = Action("CreateEmailTemplate")
CreateExportJob = Action("CreateExportJob")
CreateImportJob = Action("CreateImportJob")
CreateIngressPoint = Action("CreateIngressPoint")
CreateMultiRegionEndpoint = Action("CreateMultiRegionEndpoint")
CreateReceiptFilter = Action("CreateReceiptFilter")
CreateReceiptRule = Action("CreateReceiptRule")
CreateReceiptRuleSet = Action("CreateReceiptRuleSet")
CreateRelay = Action("CreateRelay")
CreateRuleSet = Action("CreateRuleSet")
CreateTemplate = Action("CreateTemplate")
CreateTrafficPolicy = Action("CreateTrafficPolicy")
DeleteAddonInstance = Action("DeleteAddonInstance")
DeleteAddonSubscription = Action("DeleteAddonSubscription")
DeleteAddressList = Action("DeleteAddressList")
DeleteArchive = Action("DeleteArchive")
DeleteConfigurationSet = Action("DeleteConfigurationSet")
DeleteConfigurationSetEventDestination = Action(
    "DeleteConfigurationSetEventDestination"
)
DeleteConfigurationSetTrackingOptions = Action("DeleteConfigurationSetTrackingOptions")
DeleteContact = Action("DeleteContact")
DeleteContactList = Action("DeleteContactList")
DeleteCustomVerificationEmailTemplate = Action("DeleteCustomVerificationEmailTemplate")
DeleteDedicatedIpPool = Action("DeleteDedicatedIpPool")
DeleteEmailIdentity = Action("DeleteEmailIdentity")
DeleteEmailIdentityPolicy = Action("DeleteEmailIdentityPolicy")
DeleteEmailTemplate = Action("DeleteEmailTemplate")
DeleteIdentity = Action("DeleteIdentity")
DeleteIdentityPolicy = Action("DeleteIdentityPolicy")
DeleteIngressPoint = Action("DeleteIngressPoint")
DeleteMultiRegionEndpoint = Action("DeleteMultiRegionEndpoint")
DeleteReceiptFilter = Action("DeleteReceiptFilter")
DeleteReceiptRule = Action("DeleteReceiptRule")
DeleteReceiptRuleSet = Action("DeleteReceiptRuleSet")
DeleteRelay = Action("DeleteRelay")
DeleteRuleSet = Action("DeleteRuleSet")
DeleteSuppressedDestination = Action("DeleteSuppressedDestination")
DeleteTemplate = Action("DeleteTemplate")
DeleteTrafficPolicy = Action("DeleteTrafficPolicy")
DeleteVerifiedEmailAddress = Action("DeleteVerifiedEmailAddress")
DeregisterMemberFromAddressList = Action("DeregisterMemberFromAddressList")
DescribeActiveReceiptRuleSet = Action("DescribeActiveReceiptRuleSet")
DescribeConfigurationSet = Action("DescribeConfigurationSet")
DescribeReceiptRule = Action("DescribeReceiptRule")
DescribeReceiptRuleSet = Action("DescribeReceiptRuleSet")
GetAccount = Action("GetAccount")
GetAccountSendingEnabled = Action("GetAccountSendingEnabled")
GetAddonInstance = Action("GetAddonInstance")
GetAddonSubscription = Action("GetAddonSubscription")
GetAddressList = Action("GetAddressList")
GetAddressListImportJob = Action("GetAddressListImportJob")
GetArchive = Action("GetArchive")
GetArchiveExport = Action("GetArchiveExport")
GetArchiveMessage = Action("GetArchiveMessage")
GetArchiveMessageContent = Action("GetArchiveMessageContent")
GetArchiveSearch = Action("GetArchiveSearch")
GetArchiveSearchResults = Action("GetArchiveSearchResults")
GetBlacklistReports = Action("GetBlacklistReports")
GetConfigurationSet = Action("GetConfigurationSet")
GetConfigurationSetEventDestinations = Action("GetConfigurationSetEventDestinations")
GetContact = Action("GetContact")
GetContactList = Action("GetContactList")
GetCustomVerificationEmailTemplate = Action("GetCustomVerificationEmailTemplate")
GetDedicatedIp = Action("GetDedicatedIp")
GetDedicatedIpPool = Action("GetDedicatedIpPool")
GetDedicatedIps = Action("GetDedicatedIps")
GetDeliverabilityDashboardOptions = Action("GetDeliverabilityDashboardOptions")
GetDeliverabilityTestReport = Action("GetDeliverabilityTestReport")
GetDomainDeliverabilityCampaign = Action("GetDomainDeliverabilityCampaign")
GetDomainStatisticsReport = Action("GetDomainStatisticsReport")
GetEmailIdentity = Action("GetEmailIdentity")
GetEmailIdentityPolicies = Action("GetEmailIdentityPolicies")
GetEmailTemplate = Action("GetEmailTemplate")
GetExportJob = Action("GetExportJob")
GetIdentityDkimAttributes = Action("GetIdentityDkimAttributes")
GetIdentityMailFromDomainAttributes = Action("GetIdentityMailFromDomainAttributes")
GetIdentityNotificationAttributes = Action("GetIdentityNotificationAttributes")
GetIdentityPolicies = Action("GetIdentityPolicies")
GetIdentityVerificationAttributes = Action("GetIdentityVerificationAttributes")
GetImportJob = Action("GetImportJob")
GetIngressPoint = Action("GetIngressPoint")
GetMemberOfAddressList = Action("GetMemberOfAddressList")
GetMessageInsights = Action("GetMessageInsights")
GetMultiRegionEndpoint = Action("GetMultiRegionEndpoint")
GetRelay = Action("GetRelay")
GetRuleSet = Action("GetRuleSet")
GetSendQuota = Action("GetSendQuota")
GetSendStatistics = Action("GetSendStatistics")
GetSuppressedDestination = Action("GetSuppressedDestination")
GetTemplate = Action("GetTemplate")
GetTrafficPolicy = Action("GetTrafficPolicy")
ListAddonInstances = Action("ListAddonInstances")
ListAddonSubscriptions = Action("ListAddonSubscriptions")
ListAddressListImportJobs = Action("ListAddressListImportJobs")
ListAddressLists = Action("ListAddressLists")
ListArchiveExports = Action("ListArchiveExports")
ListArchiveSearches = Action("ListArchiveSearches")
ListArchives = Action("ListArchives")
ListConfigurationSets = Action("ListConfigurationSets")
ListContactLists = Action("ListContactLists")
ListContacts = Action("ListContacts")
ListCustomVerificationEmailTemplates = Action("ListCustomVerificationEmailTemplates")
ListDedicatedIpPools = Action("ListDedicatedIpPools")
ListDeliverabilityTestReports = Action("ListDeliverabilityTestReports")
ListDomainDeliverabilityCampaigns = Action("ListDomainDeliverabilityCampaigns")
ListEmailIdentities = Action("ListEmailIdentities")
ListEmailTemplates = Action("ListEmailTemplates")
ListExportJobs = Action("ListExportJobs")
ListIdentities = Action("ListIdentities")
ListIdentityPolicies = Action("ListIdentityPolicies")
ListImportJobs = Action("ListImportJobs")
ListIngressPoints = Action("ListIngressPoints")
ListMembersOfAddressList = Action("ListMembersOfAddressList")
ListMultiRegionEndpoints = Action("ListMultiRegionEndpoints")
ListReceiptFilters = Action("ListReceiptFilters")
ListReceiptRuleSets = Action("ListReceiptRuleSets")
ListRecommendations = Action("ListRecommendations")
ListRelays = Action("ListRelays")
ListRuleSets = Action("ListRuleSets")
ListSuppressedDestinations = Action("ListSuppressedDestinations")
ListTagsForResource = Action("ListTagsForResource")
ListTemplates = Action("ListTemplates")
ListTrafficPolicies = Action("ListTrafficPolicies")
ListVerifiedEmailAddresses = Action("ListVerifiedEmailAddresses")
PutAccountDedicatedIpWarmupAttributes = Action("PutAccountDedicatedIpWarmupAttributes")
PutAccountDetails = Action("PutAccountDetails")
PutAccountSendingAttributes = Action("PutAccountSendingAttributes")
PutAccountSuppressionAttributes = Action("PutAccountSuppressionAttributes")
PutAccountVdmAttributes = Action("PutAccountVdmAttributes")
PutConfigurationSetArchivingOptions = Action("PutConfigurationSetArchivingOptions")
PutConfigurationSetDeliveryOptions = Action("PutConfigurationSetDeliveryOptions")
PutConfigurationSetReputationOptions = Action("PutConfigurationSetReputationOptions")
PutConfigurationSetSendingOptions = Action("PutConfigurationSetSendingOptions")
PutConfigurationSetSuppressionOptions = Action("PutConfigurationSetSuppressionOptions")
PutConfigurationSetTrackingOptions = Action("PutConfigurationSetTrackingOptions")
PutConfigurationSetVdmOptions = Action("PutConfigurationSetVdmOptions")
PutDedicatedIpInPool = Action("PutDedicatedIpInPool")
PutDedicatedIpPoolScalingAttributes = Action("PutDedicatedIpPoolScalingAttributes")
PutDedicatedIpWarmupAttributes = Action("PutDedicatedIpWarmupAttributes")
PutDeliverabilityDashboardOption = Action("PutDeliverabilityDashboardOption")
PutEmailIdentityConfigurationSetAttributes = Action(
    "PutEmailIdentityConfigurationSetAttributes"
)
PutEmailIdentityDkimAttributes = Action("PutEmailIdentityDkimAttributes")
PutEmailIdentityDkimSigningAttributes = Action("PutEmailIdentityDkimSigningAttributes")
PutEmailIdentityFeedbackAttributes = Action("PutEmailIdentityFeedbackAttributes")
PutEmailIdentityMailFromAttributes = Action("PutEmailIdentityMailFromAttributes")
PutIdentityPolicy = Action("PutIdentityPolicy")
PutSuppressedDestination = Action("PutSuppressedDestination")
RegisterMemberToAddressList = Action("RegisterMemberToAddressList")
ReorderReceiptRuleSet = Action("ReorderReceiptRuleSet")
ReplicateEmailIdentityDkimSigningKey = Action("ReplicateEmailIdentityDkimSigningKey")
SendBounce = Action("SendBounce")
SendBulkEmail = Action("SendBulkEmail")
SendBulkTemplatedEmail = Action("SendBulkTemplatedEmail")
SendCustomVerificationEmail = Action("SendCustomVerificationEmail")
SendEmail = Action("SendEmail")
SendRawEmail = Action("SendRawEmail")
SendTemplatedEmail = Action("SendTemplatedEmail")
SetActiveReceiptRuleSet = Action("SetActiveReceiptRuleSet")
SetIdentityDkimEnabled = Action("SetIdentityDkimEnabled")
SetIdentityFeedbackForwardingEnabled = Action("SetIdentityFeedbackForwardingEnabled")
SetIdentityHeadersInNotificationsEnabled = Action(
    "SetIdentityHeadersInNotificationsEnabled"
)
SetIdentityMailFromDomain = Action("SetIdentityMailFromDomain")
SetIdentityNotificationTopic = Action("SetIdentityNotificationTopic")
SetReceiptRulePosition = Action("SetReceiptRulePosition")
StartAddressListImportJob = Action("StartAddressListImportJob")
StartArchiveExport = Action("StartArchiveExport")
StartArchiveSearch = Action("StartArchiveSearch")
StopAddressListImportJob = Action("StopAddressListImportJob")
StopArchiveExport = Action("StopArchiveExport")
StopArchiveSearch = Action("StopArchiveSearch")
TagResource = Action("TagResource")
TestRenderEmailTemplate = Action("TestRenderEmailTemplate")
TestRenderTemplate = Action("TestRenderTemplate")
UntagResource = Action("UntagResource")
UpdateAccountSendingEnabled = Action("UpdateAccountSendingEnabled")
UpdateArchive = Action("UpdateArchive")
UpdateConfigurationSetEventDestination = Action(
    "UpdateConfigurationSetEventDestination"
)
UpdateConfigurationSetReputationMetricsEnabled = Action(
    "UpdateConfigurationSetReputationMetricsEnabled"
)
UpdateConfigurationSetSendingEnabled = Action("UpdateConfigurationSetSendingEnabled")
UpdateConfigurationSetTrackingOptions = Action("UpdateConfigurationSetTrackingOptions")
UpdateContact = Action("UpdateContact")
UpdateContactList = Action("UpdateContactList")
UpdateCustomVerificationEmailTemplate = Action("UpdateCustomVerificationEmailTemplate")
UpdateEmailIdentityPolicy = Action("UpdateEmailIdentityPolicy")
UpdateEmailTemplate = Action("UpdateEmailTemplate")
UpdateIngressPoint = Action("UpdateIngressPoint")
UpdateReceiptRule = Action("UpdateReceiptRule")
UpdateRelay = Action("UpdateRelay")
UpdateRuleSet = Action("UpdateRuleSet")
UpdateTemplate = Action("UpdateTemplate")
UpdateTrafficPolicy = Action("UpdateTrafficPolicy")
VerifyDomainDkim = Action("VerifyDomainDkim")
VerifyDomainIdentity = Action("VerifyDomainIdentity")
VerifyEmailAddress = Action("VerifyEmailAddress")
VerifyEmailIdentity = Action("VerifyEmailIdentity")
