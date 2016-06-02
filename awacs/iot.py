# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT'
prefix = 'iot'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptCertificateTransfer = Action('AcceptCertificateTransfer')
AttachPrincipalPolicy = Action('AttachPrincipalPolicy')
AttachThingPrincipal = Action('AttachThingPrincipal')
CancelCertificateTransfer = Action('CancelCertificateTransfer')
Connect = Action('Connect')
CreateCertificateFromCsr = Action('CreateCertificateFromCsr')
CreateKeysAndCertificate = Action('CreateKeysAndCertificate')
CreatePolicy = Action('CreatePolicy')
CreatePolicyVersion = Action('CreatePolicyVersion')
CreateThing = Action('CreateThing')
CreateTopicRule = Action('CreateTopicRule')
DeleteCertificate = Action('DeleteCertificate')
DeletePolicy = Action('DeletePolicy')
DeletePolicyVersion = Action('DeletePolicyVersion')
DeleteThing = Action('DeleteThing')
DeleteThingShadow = Action('DeleteThingShadow')
DeleteTopicRule = Action('DeleteTopicRule')
DescribeCertificate = Action('DescribeCertificate')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeThing = Action('DescribeThing')
DetachPrincipalPolicy = Action('DetachPrincipalPolicy')
DetachThingPrincipal = Action('DetachThingPrincipal')
GetLoggingOptions = Action('GetLoggingOptions')
GetPolicy = Action('GetPolicy')
GetPolicyVersion = Action('GetPolicyVersion')
GetThingShadow = Action('GetThingShadow')
GetTopicRule = Action('GetTopicRule')
ListCertificates = Action('ListCertificates')
ListPolicies = Action('ListPolicies')
ListPolicyVersions = Action('ListPolicyVersions')
ListPrincipalPolicies = Action('ListPrincipalPolicies')
ListPrincipalThings = Action('ListPrincipalThings')
ListThingPrincipals = Action('ListThingPrincipals')
ListThings = Action('ListThings')
ListTopicRules = Action('ListTopicRules')
Publish = Action('Publish')
Receive = Action('Receive')
RejectCertificateTransfer = Action('RejectCertificateTransfer')
ReplaceTopicRule = Action('ReplaceTopicRule')
SetDefaultPolicyVersion = Action('SetDefaultPolicyVersion')
SetLoggingOptions = Action('SetLoggingOptions')
Subscribe = Action('Subscribe')
TransferCertificate = Action('TransferCertificate')
UpdateCertificate = Action('UpdateCertificate')
UpdateThing = Action('UpdateThing')
UpdateThingShadow = Action('UpdateThingShadow')
