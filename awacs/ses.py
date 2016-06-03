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
CreateReceiptFilter = Action('CreateReceiptFilter')
CreateReceiptRule = Action('CreateReceiptRule')
CreateReceiptRuleSet = Action('CreateReceiptRuleSet')
DeleteIdentity = Action('DeleteIdentity')
DeleteIdentityPolicy = Action('DeleteIdentityPolicy')
DeleteReceiptFilter = Action('DeleteReceiptFilter')
DeleteReceiptRule = Action('DeleteReceiptRule')
DeleteReceiptRuleSet = Action('DeleteReceiptRuleSet')
DeleteVerifiedEmailAddress = Action('DeleteVerifiedEmailAddress')
DescribeActiveReceiptRuleSet = Action('DescribeActiveReceiptRuleSet')
DescribeReceiptRule = Action('DescribeReceiptRule')
DescribeReceiptRuleSet = Action('DescribeReceiptRuleSet')
GetIdentityDkimAttributes = Action('GetIdentityDkimAttributes')
GetIdentityNotificationAttributes = \
    Action('GetIdentityNotificationAttributes')
GetIdentityPolicies = Action('GetIdentityPolicies')
GetIdentityVerificationAttributes = \
    Action('GetIdentityVerificationAttributes')
GetSendQuota = Action('GetSendQuota')
GetSendStatistics = Action('GetSendStatistics')
ListIdentities = Action('ListIdentities')
ListIdentityPolicies = Action('ListIdentityPolicies')
ListReceiptFilters = Action('ListReceiptFilters')
ListReceiptRuleSets = Action('ListReceiptRuleSets')
ListVerifiedEmailAddresses = Action('ListVerifiedEmailAddresses')
PutIdentityPolicy = Action('PutIdentityPolicy')
ReorderReceiptRuleSet = Action('ReorderReceiptRuleSet')
SendBounce = Action('SendBounce')
SendEmail = Action('SendEmail')
SendRawEmail = Action('SendRawEmail')
SetActiveReceiptRuleSet = Action('SetActiveReceiptRuleSet')
SetIdentityDkimEnabled = Action('SetIdentityDkimEnabled')
SetIdentityNotificationTopic = Action('SetIdentityNotificationTopic')
SetIdentityFeedbackForwardingEnabled = \
    Action('SetIdentityFeedbackForwardingEnabled')
SetReceiptRulePosition = Action('SetReceiptRulePosition')
UpdateReceiptRule = Action('UpdateReceiptRule')
VerifyDomainDkim = Action('VerifyDomainDkim')
VerifyDomainIdentity = Action('VerifyDomainIdentity')
VerifyEmailAddress = Action('VerifyEmailAddress')
VerifyEmailIdentity = Action('VerifyEmailIdentity')
