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
CreateThingType = Action('CreateThingType')
CreateTopicRule = Action('CreateTopicRule')
DeleteCACertificate = Action('DeleteCACertificate')
DeleteCertificate = Action('DeleteCertificate')
DeletePolicy = Action('DeletePolicy')
DeletePolicyVersion = Action('DeletePolicyVersion')
DeleteRegistrationCode = Action('DeleteRegistrationCode')
DeleteThing = Action('DeleteThing')
DeleteThingShadow = Action('DeleteThingShadow')
DeleteThingType = Action('DeleteThingType')
DeleteTopicRule = Action('DeleteTopicRule')
DeprecateThingType = Action('DeprecateThingType')
DescribeCaCertificate = Action('DescribeCaCertificate')
DescribeCertificate = Action('DescribeCertificate')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeThing = Action('DescribeThing')
DescribeThingType = Action('DescribeThingType')
DetachPrincipalPolicy = Action('DetachPrincipalPolicy')
DetachThingPrincipal = Action('DetachThingPrincipal')
DisableTopicRule = Action('DisableTopicRule')
EnableTopicRule = Action('EnableTopicRule')
GetLoggingOptions = Action('GetLoggingOptions')
GetPolicy = Action('GetPolicy')
GetPolicyVersion = Action('GetPolicyVersion')
GetRegistrationCode = Action('GetRegistrationCode')
GetThingShadow = Action('GetThingShadow')
GetTopicRule = Action('GetTopicRule')
ListCaCertificates = Action('ListCaCertificates')
ListCertificates = Action('ListCertificates')
ListCertificatesByCa = Action('ListCertificatesByCa')
ListOutgoingCertificates = Action('ListOutgoingCertificates')
ListPolicies = Action('ListPolicies')
ListPolicyPrincipals = Action('ListPolicyPrincipals')
ListPolicyVersions = Action('ListPolicyVersions')
ListPrincipalPolicies = Action('ListPrincipalPolicies')
ListPrincipalThings = Action('ListPrincipalThings')
ListThingPrincipals = Action('ListThingPrincipals')
ListThingTypes = Action('ListThingTypes')
ListThings = Action('ListThings')
ListTopicRules = Action('ListTopicRules')
Publish = Action('Publish')
Receive = Action('Receive')
RegisterCACertificate = Action('RegisterCACertificate')
RegisterCertificate = Action('RegisterCertificate')
RejectCertificateTransfer = Action('RejectCertificateTransfer')
ReplaceTopicRule = Action('ReplaceTopicRule')
SetDefaultPolicyVersion = Action('SetDefaultPolicyVersion')
SetLoggingOptions = Action('SetLoggingOptions')
Subscribe = Action('Subscribe')
TransferCertificate = Action('TransferCertificate')
UpdateCACertificate = Action('UpdateCACertificate')
UpdateCertificate = Action('UpdateCertificate')
UpdateThing = Action('UpdateThing')
UpdateThingShadow = Action('UpdateThingShadow')
