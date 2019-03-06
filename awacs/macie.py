# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Macie'
prefix = 'macie'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateMemberAccount = Action('AssociateMemberAccount')
AssociateS3Resources = Action('AssociateS3Resources')
DisassociateMemberAccount = Action('DisassociateMemberAccount')
DisassociateS3Resources = Action('DisassociateS3Resources')
ListMemberAccounts = Action('ListMemberAccounts')
ListS3Resources = Action('ListS3Resources')
UpdateS3Resources = Action('UpdateS3Resources')
