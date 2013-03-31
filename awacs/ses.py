# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon SES'
prefix = 'ses'

DeleteIdentity = Action(prefix, 'DeleteIdentity')
DeleteVerifiedEmailAddress = \
    Action(prefix, 'DeleteVerifiedEmailAddress')
GetIdentityDkimAttributes = Action(prefix, 'GetIdentityDkimAttributes')
GetIdentityNotificationAttributes = \
    Action(prefix, 'GetIdentityNotificationAttributes')
GetIdentityVerificationAttributes = \
    Action(prefix, 'GetIdentityVerificationAttributes')
GetSendQuota = Action(prefix, 'GetSendQuota')
GetSendStatistics = Action(prefix, 'GetSendStatistics')
ListIdentities = Action(prefix, 'ListIdentities')
ListVerifiedEmailAddresses = \
    Action(prefix, 'ListVerifiedEmailAddresses')
SendEmail = Action(prefix, 'SendEmail')
SendRawEmail = Action(prefix, 'SendRawEmail')
SetIdentityDkimEnabled = Action(prefix, 'SetIdentityDkimEnabled')
SetIdentityNotificationTopic = \
    Action(prefix, 'SetIdentityNotificationTopic')
SetIdentityFeedbackForwardingEnabled = \
    Action(prefix, 'SetIdentityFeedbackForwardingEnabled')
VerifyDomainDkim = Action(prefix, 'VerifyDomainDkim')
VerifyDomainIdentity = Action(prefix, 'VerifyDomainIdentity')
VerifyEmailAddress = Action(prefix, 'VerifyEmailAddress')
VerifyEmailIdentity = Action(prefix, 'VerifyEmailIdentity')
