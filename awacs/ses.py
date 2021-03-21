# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon SES"
prefix = "ses"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CloneReceiptRuleSet = Action("CloneReceiptRuleSet")
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
CreateImportJob = Action("CreateImportJob")
CreateReceiptFilter = Action("CreateReceiptFilter")
CreateReceiptRule = Action("CreateReceiptRule")
CreateReceiptRuleSet = Action("CreateReceiptRuleSet")
CreateTemplate = Action("CreateTemplate")
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
DeleteReceiptFilter = Action("DeleteReceiptFilter")
DeleteReceiptRule = Action("DeleteReceiptRule")
DeleteReceiptRuleSet = Action("DeleteReceiptRuleSet")
DeleteSuppressedDestination = Action("DeleteSuppressedDestination")
DeleteTemplate = Action("DeleteTemplate")
DeleteVerifiedEmailAddress = Action("DeleteVerifiedEmailAddress")
DescribeActiveReceiptRuleSet = Action("DescribeActiveReceiptRuleSet")
DescribeConfigurationSet = Action("DescribeConfigurationSet")
DescribeReceiptRule = Action("DescribeReceiptRule")
DescribeReceiptRuleSet = Action("DescribeReceiptRuleSet")
GetAccount = Action("GetAccount")
GetAccountSendingEnabled = Action("GetAccountSendingEnabled")
GetBlacklistReports = Action("GetBlacklistReports")
GetConfigurationSet = Action("GetConfigurationSet")
GetConfigurationSetEventDestinations = Action("GetConfigurationSetEventDestinations")
GetContact = Action("GetContact")
GetContactList = Action("GetContactList")
GetCustomVerificationEmailTemplate = Action("GetCustomVerificationEmailTemplate")
GetDedicatedIp = Action("GetDedicatedIp")
GetDedicatedIps = Action("GetDedicatedIps")
GetDeliverabilityDashboardOptions = Action("GetDeliverabilityDashboardOptions")
GetDeliverabilityTestReport = Action("GetDeliverabilityTestReport")
GetDomainDeliverabilityCampaign = Action("GetDomainDeliverabilityCampaign")
GetDomainStatisticsReport = Action("GetDomainStatisticsReport")
GetEmailIdentity = Action("GetEmailIdentity")
GetEmailIdentityPolicies = Action("GetEmailIdentityPolicies")
GetEmailTemplate = Action("GetEmailTemplate")
GetIdentityDkimAttributes = Action("GetIdentityDkimAttributes")
GetIdentityMailFromDomainAttributes = Action("GetIdentityMailFromDomainAttributes")
GetIdentityNotificationAttributes = Action("GetIdentityNotificationAttributes")
GetIdentityPolicies = Action("GetIdentityPolicies")
GetIdentityVerificationAttributes = Action("GetIdentityVerificationAttributes")
GetImportJob = Action("GetImportJob")
GetSendQuota = Action("GetSendQuota")
GetSendStatistics = Action("GetSendStatistics")
GetSuppressedDestination = Action("GetSuppressedDestination")
GetTemplate = Action("GetTemplate")
ListConfigurationSets = Action("ListConfigurationSets")
ListContactLists = Action("ListContactLists")
ListContacts = Action("ListContacts")
ListCustomVerificationEmailTemplates = Action("ListCustomVerificationEmailTemplates")
ListDedicatedIpPools = Action("ListDedicatedIpPools")
ListDeliverabilityTestReports = Action("ListDeliverabilityTestReports")
ListDomainDeliverabilityCampaigns = Action("ListDomainDeliverabilityCampaigns")
ListEmailIdentities = Action("ListEmailIdentities")
ListEmailTemplates = Action("ListEmailTemplates")
ListIdentities = Action("ListIdentities")
ListIdentityPolicies = Action("ListIdentityPolicies")
ListImportJobs = Action("ListImportJobs")
ListReceiptFilters = Action("ListReceiptFilters")
ListReceiptRuleSets = Action("ListReceiptRuleSets")
ListSuppressedDestinations = Action("ListSuppressedDestinations")
ListTagsForResource = Action("ListTagsForResource")
ListTemplates = Action("ListTemplates")
ListVerifiedEmailAddresses = Action("ListVerifiedEmailAddresses")
PutAccountDedicatedIpWarmupAttributes = Action("PutAccountDedicatedIpWarmupAttributes")
PutAccountDetails = Action("PutAccountDetails")
PutAccountSendingAttributes = Action("PutAccountSendingAttributes")
PutAccountSuppressionAttributes = Action("PutAccountSuppressionAttributes")
PutConfigurationSetDeliveryOptions = Action("PutConfigurationSetDeliveryOptions")
PutConfigurationSetReputationOptions = Action("PutConfigurationSetReputationOptions")
PutConfigurationSetSendingOptions = Action("PutConfigurationSetSendingOptions")
PutConfigurationSetSuppressionOptions = Action("PutConfigurationSetSuppressionOptions")
PutConfigurationSetTrackingOptions = Action("PutConfigurationSetTrackingOptions")
PutDedicatedIpInPool = Action("PutDedicatedIpInPool")
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
ReorderReceiptRuleSet = Action("ReorderReceiptRuleSet")
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
TagResource = Action("TagResource")
TestRenderEmailTemplate = Action("TestRenderEmailTemplate")
TestRenderTemplate = Action("TestRenderTemplate")
UntagResource = Action("UntagResource")
UpdateAccountSendingEnabled = Action("UpdateAccountSendingEnabled")
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
UpdateReceiptRule = Action("UpdateReceiptRule")
UpdateTemplate = Action("UpdateTemplate")
VerifyDomainDkim = Action("VerifyDomainDkim")
VerifyDomainIdentity = Action("VerifyDomainIdentity")
VerifyEmailAddress = Action("VerifyEmailAddress")
VerifyEmailIdentity = Action("VerifyEmailIdentity")
