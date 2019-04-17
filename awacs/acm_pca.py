# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Certificate Manager Private Certificate Authority'
prefix = 'acm-pca'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateCertificateAuthority = Action('CreateCertificateAuthority')
CreateCertificateAuthorityAuditReport = \
    Action('CreateCertificateAuthorityAuditReport')
DeleteCertificateAuthority = Action('DeleteCertificateAuthority')
DescribeCertificateAuthority = Action('DescribeCertificateAuthority')
DescribeCertificateAuthorityAuditReport = \
    Action('DescribeCertificateAuthorityAuditReport')
GetCertificate = Action('GetCertificate')
GetCertificateAuthorityCertificate = \
    Action('GetCertificateAuthorityCertificate')
GetCertificateAuthorityCsr = Action('GetCertificateAuthorityCsr')
ImportCertificateAuthorityCertificate = \
    Action('ImportCertificateAuthorityCertificate')
IssueCertificate = Action('IssueCertificate')
ListCertificateAuthorities = Action('ListCertificateAuthorities')
ListTags = Action('ListTags')
RestoreCertificateAuthority = Action('RestoreCertificateAuthority')
RevokeCertificate = Action('RevokeCertificate')
TagCertificateAuthority = Action('TagCertificateAuthority')
UntagCertificateAuthority = Action('UntagCertificateAuthority')
UpdateCertificateAuthority = Action('UpdateCertificateAuthority')
