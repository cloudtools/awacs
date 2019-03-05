# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS AppSync'
prefix = 'appsync'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApiKey = Action('CreateApiKey')
CreateDataSource = Action('CreateDataSource')
CreateFunction = Action('CreateFunction')
CreateGraphqlApi = Action('CreateGraphqlApi')
CreateResolver = Action('CreateResolver')
CreateType = Action('CreateType')
DeleteApiKey = Action('DeleteApiKey')
DeleteDataSource = Action('DeleteDataSource')
DeleteFunction = Action('DeleteFunction')
DeleteGraphqlApi = Action('DeleteGraphqlApi')
DeleteResolver = Action('DeleteResolver')
DeleteType = Action('DeleteType')
GetDataSource = Action('GetDataSource')
GetFunction = Action('GetFunction')
GetGraphqlApi = Action('GetGraphqlApi')
GetIntrospectionSchema = Action('GetIntrospectionSchema')
GetResolver = Action('GetResolver')
GetSchemaCreationStatus = Action('GetSchemaCreationStatus')
GetType = Action('GetType')
GraphQL = Action('GraphQL')
ListApiKeys = Action('ListApiKeys')
ListDataSources = Action('ListDataSources')
ListFunctions = Action('ListFunctions')
ListGraphqlApis = Action('ListGraphqlApis')
ListResolvers = Action('ListResolvers')
ListTypes = Action('ListTypes')
StartSchemaCreation = Action('StartSchemaCreation')
UpdateApiKey = Action('UpdateApiKey')
UpdateDataSource = Action('UpdateDataSource')
UpdateFunction = Action('UpdateFunction')
UpdateGraphqlApi = Action('UpdateGraphqlApi')
UpdateResolver = Action('UpdateResolver')
UpdateType = Action('UpdateType')
