# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Redshift Data API'
prefix = 'redshift-data'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelStatement = Action('CancelStatement')
DescribeStatement = Action('DescribeStatement')
DescribeTable = Action('DescribeTable')
ExecuteStatement = Action('ExecuteStatement')
GetStatementResult = Action('GetStatementResult')
ListDatabases = Action('ListDatabases')
ListSchemas = Action('ListSchemas')
ListStatements = Action('ListStatements')
ListTables = Action('ListTables')
