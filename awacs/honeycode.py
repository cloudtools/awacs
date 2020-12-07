# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Honeycode'
prefix = 'honeycode'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ApproveTeamAssociation = Action('ApproveTeamAssociation')
BatchCreateTableRows = Action('BatchCreateTableRows')
BatchDeleteTableRows = Action('BatchDeleteTableRows')
BatchUpdateTableRows = Action('BatchUpdateTableRows')
BatchUpsertTableRows = Action('BatchUpsertTableRows')
CreateTenant = Action('CreateTenant')
DescribeTableDataImportJob = Action('DescribeTableDataImportJob')
GetScreenData = Action('GetScreenData')
InvokeScreenAutomation = Action('InvokeScreenAutomation')
ListTableColumns = Action('ListTableColumns')
ListTableRows = Action('ListTableRows')
ListTables = Action('ListTables')
ListTeamAssociations = Action('ListTeamAssociations')
ListTenants = Action('ListTenants')
QueryTableRows = Action('QueryTableRows')
RejectTeamAssociation = Action('RejectTeamAssociation')
StartTableDataImportJob = Action('StartTableDataImportJob')
