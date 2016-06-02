# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Simple Systems Manager'
prefix = 'ssm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAssociation = Action('CreateAssociation')
CreateAssociationBatch = Action('CreateAssociationBatch')
CreateDocument = Action('CreateDocument')
DeleteAssociation = Action('DeleteAssociation')
DeleteDocument = Action('DeleteDocument')
DescribeAssociation = Action('DescribeAssociation')
DescribeDocument = Action('DescribeDocument')
GetDocument = Action('GetDocument')
ListAssociations = Action('ListAssociations')
ListDocuments = Action('ListDocuments')
UpdateAssociationStatus = Action('UpdateAssociationStatus')
