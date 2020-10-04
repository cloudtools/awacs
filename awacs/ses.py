# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SES'
prefix = 'ses'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CloneReceiptRuleSet = Action('CloneReceiptRuleSet')
CreateConfigurationSet = Action('CreateConfigurationSet')
CreateConfigurationSetEventDestination = \
    Action('CreateConfigurationSetEventDestination')
CreateConfigurationSetTrackingOptions = \
    Action('CreateConfigurationSetTrackingOptions')
CreateCustomVerificationEmailTemplate = \
    Action('CreateCustomVerificationEmailTemplate')
CreateDedicatedIpPool = Action('CreateDedicatedIpPool')
CreateDeliverabilityTestReport = Action('CreateDeliverabilityTestReport')
CreateEmailIdentity = Action('CreateEmailIdentity')
CreateReceiptFilter = Action('CreateReceiptFilter')
CreateReceiptRule = Action('CreateReceiptRule')
CreateReceiptRuleSet = Action('CreateReceiptRuleSet')
CreateTemplate = Action('CreateTemplate')
DeleteConfigurationSet = Action('DeleteConfigurationSet')
DeleteConfigurationSetEventDestination = \
    Action('DeleteConfigurationSetEventDestination')
DeleteConfigurationSetTrackingOptions = \
    Action('DeleteConfigurationSetTrackingOptions')
DeleteCustomVerificationEmailTemplate = \
    Action('DeleteCustomVerificationEmailTemplate')
DeleteDedicatedIpPool = Action('DeleteDedicatedIpPool')
DeleteEmailIdentity = Action('DeleteEmailIdentity')
DeleteIdentity = Action('DeleteIdentity')
DeleteIdentityPolicy = Action('DeleteIdentityPolicy')
DeleteReceiptFilter = Action('DeleteReceiptFilter')
DeleteReceiptRule = Action('DeleteReceiptRule')
DeleteReceiptRuleSet = Action('DeleteReceiptRuleSet')
DeleteTemplate = Action('DeleteTemplate')
DeleteVerifiedEmailAddress = Action('DeleteVerifiedEmailAddress')
DescribeActiveReceiptRuleSet = Action('DescribeActiveReceiptRuleSet')
DescribeConfigurationSet = Action('DescribeConfigurationSet')
DescribeReceiptRule = Action('DescribeReceiptRule')
DescribeReceiptRuleSet = Action('DescribeReceiptRuleSet')
GetAccount = Action('GetAccount')
GetAccountSendingEnabled = Action('GetAccountSendingEnabled')
GetBlacklistReports = Action('GetBlacklistReports')
GetConfigurationSet = Action('GetConfigurationSet')
GetConfigurationSetEventDestinations = \
    Action('GetConfigurationSetEventDestinations')
GetCustomVerificationEmailTemplate = \
    Action('GetCustomVerificationEmailTemplate')
GetDedicatedIp = Action('GetDedicatedIp')
GetDedicatedIps = Action('GetDedicatedIps')
GetDeliverabilityDashboardOptions = \
    Action('GetDeliverabilityDashboardOptions')
GetDeliverabilityTestReport = Action('GetDeliverabilityTestReport')
GetDomainStatisticsReport = Action('GetDomainStatisticsReport')
GetEmailIdentity = Action('GetEmailIdentity')
GetIdentityDkimAttributes = Action('GetIdentityDkimAttributes')
GetIdentityMailFromDomainAttributes = \
    Action('GetIdentityMailFromDomainAttributes')
GetIdentityNotificationAttributes = \
    Action('GetIdentityNotificationAttributes')
GetIdentityPolicies = Action('GetIdentityPolicies')
GetIdentityVerificationAttributes = \
    Action('GetIdentityVerificationAttributes')
GetSendQuota = Action('GetSendQuota')
GetSendStatistics = Action('GetSendStatistics')
GetTemplate = Action('GetTemplate')
ListConfigurationSets = Action('ListConfigurationSets')
ListCustomVerificationEmailTemplates = \
    Action('ListCustomVerificationEmailTemplates')
ListDedicatedIpPools = Action('ListDedicatedIpPools')
ListDeliverabilityTestReports = Action('ListDeliverabilityTestReports')
ListEmailIdentities = Action('ListEmailIdentities')
ListIdentities = Action('ListIdentities')
ListIdentityPolicies = Action('ListIdentityPolicies')
ListReceiptFilters = Action('ListReceiptFilters')
ListReceiptRuleSets = Action('ListReceiptRuleSets')
ListTagsForResource = Action('ListTagsForResource')
ListTemplates = Action('ListTemplates')
ListVerifiedEmailAddresses = Action('ListVerifiedEmailAddresses')
PutAccountDedicatedIpWarmupAttributes = \
    Action('PutAccountDedicatedIpWarmupAttributes')
PutAccountSendingAttributes = Action('PutAccountSendingAttributes')
PutConfigurationSetDeliveryOptions = \
    Action('PutConfigurationSetDeliveryOptions')
PutConfigurationSetReputationOptions = \
    Action('PutConfigurationSetReputationOptions')
PutConfigurationSetSendingOptions = \
    Action('PutConfigurationSetSendingOptions')
PutConfigurationSetTrackingOptions = \
    Action('PutConfigurationSetTrackingOptions')
PutDedicatedIpInPool = Action('PutDedicatedIpInPool')
PutDedicatedIpWarmupAttributes = Action('PutDedicatedIpWarmupAttributes')
PutDeliverabilityDashboardOption = \
    Action('PutDeliverabilityDashboardOption')
PutEmailIdentityDkimAttributes = Action('PutEmailIdentityDkimAttributes')
PutEmailIdentityFeedbackAttributes = \
    Action('PutEmailIdentityFeedbackAttributes')
PutEmailIdentityMailFromAttributes = \
    Action('PutEmailIdentityMailFromAttributes')
PutIdentityPolicy = Action('PutIdentityPolicy')
ReorderReceiptRuleSet = Action('ReorderReceiptRuleSet')
SendBounce = Action('SendBounce')
SendBulkTemplatedEmail = Action('SendBulkTemplatedEmail')
SendCustomVerificationEmail = Action('SendCustomVerificationEmail')
SendEmail = Action('SendEmail')
SendRawEmail = Action('SendRawEmail')
SendTemplatedEmail = Action('SendTemplatedEmail')
SetActiveReceiptRuleSet = Action('SetActiveReceiptRuleSet')
SetIdentityDkimEnabled = Action('SetIdentityDkimEnabled')
SetIdentityFeedbackForwardingEnabled = \
    Action('SetIdentityFeedbackForwardingEnabled')
SetIdentityHeadersInNotificationsEnabled = \
    Action('SetIdentityHeadersInNotificationsEnabled')
SetIdentityMailFromDomain = Action('SetIdentityMailFromDomain')
SetIdentityNotificationTopic = Action('SetIdentityNotificationTopic')
SetReceiptRulePosition = Action('SetReceiptRulePosition')
TagResource = Action('TagResource')
TestRenderTemplate = Action('TestRenderTemplate')
UntagResource = Action('UntagResource')
UpdateAccountSendingEnabled = Action('UpdateAccountSendingEnabled')
UpdateConfigurationSetEventDestination = \
    Action('UpdateConfigurationSetEventDestination')
UpdateConfigurationSetReputationMetricsEnabled = \
    Action('UpdateConfigurationSetReputationMetricsEnabled')
UpdateConfigurationSetSendingEnabled = \
    Action('UpdateConfigurationSetSendingEnabled')
UpdateConfigurationSetTrackingOptions = \
    Action('UpdateConfigurationSetTrackingOptions')
UpdateCustomVerificationEmailTemplate = \
    Action('UpdateCustomVerificationEmailTemplate')
UpdateReceiptRule = Action('UpdateReceiptRule')
UpdateTemplate = Action('UpdateTemplate')
VerifyDomainDkim = Action('VerifyDomainDkim')
VerifyDomainIdentity = Action('VerifyDomainIdentity')
VerifyEmailAddress = Action('VerifyEmailAddress')
VerifyEmailIdentity = Action('VerifyEmailIdentity')
