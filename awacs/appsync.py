# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS AppSync"
prefix = "appsync"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateApi = Action("AssociateApi")
AssociateMergedGraphqlApi = Action("AssociateMergedGraphqlApi")
AssociateSourceGraphqlApi = Action("AssociateSourceGraphqlApi")
CreateApi = Action("CreateApi")
CreateApiCache = Action("CreateApiCache")
CreateApiKey = Action("CreateApiKey")
CreateChannelNamespace = Action("CreateChannelNamespace")
CreateDataSource = Action("CreateDataSource")
CreateDomainName = Action("CreateDomainName")
CreateFunction = Action("CreateFunction")
CreateGraphqlApi = Action("CreateGraphqlApi")
CreateResolver = Action("CreateResolver")
CreateType = Action("CreateType")
DeleteApi = Action("DeleteApi")
DeleteApiCache = Action("DeleteApiCache")
DeleteApiKey = Action("DeleteApiKey")
DeleteChannelNamespace = Action("DeleteChannelNamespace")
DeleteDataSource = Action("DeleteDataSource")
DeleteDomainName = Action("DeleteDomainName")
DeleteFunction = Action("DeleteFunction")
DeleteGraphqlApi = Action("DeleteGraphqlApi")
DeleteResolver = Action("DeleteResolver")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DeleteType = Action("DeleteType")
DisassociateApi = Action("DisassociateApi")
DisassociateMergedGraphqlApi = Action("DisassociateMergedGraphqlApi")
DisassociateSourceGraphqlApi = Action("DisassociateSourceGraphqlApi")
EvaluateCode = Action("EvaluateCode")
EvaluateMappingTemplate = Action("EvaluateMappingTemplate")
EventConnect = Action("EventConnect")
EventPublish = Action("EventPublish")
EventSubscribe = Action("EventSubscribe")
FlushApiCache = Action("FlushApiCache")
GetApi = Action("GetApi")
GetApiAssociation = Action("GetApiAssociation")
GetApiCache = Action("GetApiCache")
GetChannelNamespace = Action("GetChannelNamespace")
GetDataSource = Action("GetDataSource")
GetDataSourceIntrospection = Action("GetDataSourceIntrospection")
GetDomainName = Action("GetDomainName")
GetFunction = Action("GetFunction")
GetGraphqlApi = Action("GetGraphqlApi")
GetGraphqlApiEnvironmentVariables = Action("GetGraphqlApiEnvironmentVariables")
GetIntrospectionSchema = Action("GetIntrospectionSchema")
GetResolver = Action("GetResolver")
GetResourcePolicy = Action("GetResourcePolicy")
GetSchemaCreationStatus = Action("GetSchemaCreationStatus")
GetSourceApiAssociation = Action("GetSourceApiAssociation")
GetType = Action("GetType")
GraphQL = Action("GraphQL")
ListApiKeys = Action("ListApiKeys")
ListApis = Action("ListApis")
ListChannelNamespaces = Action("ListChannelNamespaces")
ListDataSources = Action("ListDataSources")
ListDomainNames = Action("ListDomainNames")
ListFunctions = Action("ListFunctions")
ListGraphqlApis = Action("ListGraphqlApis")
ListResolvers = Action("ListResolvers")
ListResolversByFunction = Action("ListResolversByFunction")
ListSourceApiAssociations = Action("ListSourceApiAssociations")
ListTagsForResource = Action("ListTagsForResource")
ListTypes = Action("ListTypes")
ListTypesByAssociation = Action("ListTypesByAssociation")
PutGraphqlApiEnvironmentVariables = Action("PutGraphqlApiEnvironmentVariables")
PutResourcePolicy = Action("PutResourcePolicy")
SetWebACL = Action("SetWebACL")
SourceGraphQL = Action("SourceGraphQL")
StartDataSourceIntrospection = Action("StartDataSourceIntrospection")
StartSchemaCreation = Action("StartSchemaCreation")
StartSchemaMerge = Action("StartSchemaMerge")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApi = Action("UpdateApi")
UpdateApiCache = Action("UpdateApiCache")
UpdateApiKey = Action("UpdateApiKey")
UpdateChannelNamespace = Action("UpdateChannelNamespace")
UpdateDataSource = Action("UpdateDataSource")
UpdateDomainName = Action("UpdateDomainName")
UpdateFunction = Action("UpdateFunction")
UpdateGraphqlApi = Action("UpdateGraphqlApi")
UpdateResolver = Action("UpdateResolver")
UpdateSourceApiAssociation = Action("UpdateSourceApiAssociation")
UpdateType = Action("UpdateType")
