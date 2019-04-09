# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Certificate Manager'
prefix = 'acm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddTagsToCertificate = Action('AddTagsToCertificate')
DeleteCertificate = Action('DeleteCertificate')
DescribeCertificate = Action('DescribeCertificate')
ExportCertificate = Action('ExportCertificate')
GetCertificate = Action('GetCertificate')
ImportCertificate = Action('ImportCertificate')
ListCertificates = Action('ListCertificates')
ListTagsForCertificate = Action('ListTagsForCertificate')
RemoveTagsFromCertificate = Action('RemoveTagsFromCertificate')
RenewCertificate = Action('RenewCertificate')
RequestCertificate = Action('RequestCertificate')
ResendValidationEmail = Action('ResendValidationEmail')
UpdateCertificateOptions = Action('UpdateCertificateOptions')
