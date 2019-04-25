# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Athena'
prefix = 'athena'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetNamedQuery = Action('BatchGetNamedQuery')
BatchGetQueryExecution = Action('BatchGetQueryExecution')
CancelQueryExecution = Action('CancelQueryExecution')
CreateNamedQuery = Action('CreateNamedQuery')
CreateWorkGroup = Action('CreateWorkGroup')
DeleteNamedQuery = Action('DeleteNamedQuery')
DeleteWorkGroup = Action('DeleteWorkGroup')
GetCatalogs = Action('GetCatalogs')
GetExecutionEngine = Action('GetExecutionEngine')
GetExecutionEngines = Action('GetExecutionEngines')
GetNamedQuery = Action('GetNamedQuery')
GetNamespace = Action('GetNamespace')
GetNamespaces = Action('GetNamespaces')
GetQueryExecution = Action('GetQueryExecution')
GetQueryExecutions = Action('GetQueryExecutions')
GetQueryResults = Action('GetQueryResults')
GetQueryResultsStream = Action('GetQueryResultsStream')
GetTable = Action('GetTable')
GetTables = Action('GetTables')
GetWorkGroup = Action('GetWorkGroup')
ListNamedQueries = Action('ListNamedQueries')
ListQueryExecutions = Action('ListQueryExecutions')
ListTagsForResource = Action('ListTagsForResource')
ListWorkGroups = Action('ListWorkGroups')
RunQuery = Action('RunQuery')
StartQueryExecution = Action('StartQueryExecution')
StopQueryExecution = Action('StopQueryExecution')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateWorkGroup = Action('UpdateWorkGroup')
