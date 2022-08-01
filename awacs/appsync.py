# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS AppSync"
prefix = "appsync"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateApi = Action("AssociateApi")
CreateApiCache = Action("CreateApiCache")
CreateApiKey = Action("CreateApiKey")
CreateDataSource = Action("CreateDataSource")
CreateDomainName = Action("CreateDomainName")
CreateFunction = Action("CreateFunction")
CreateGraphqlApi = Action("CreateGraphqlApi")
CreateResolver = Action("CreateResolver")
CreateType = Action("CreateType")
DeleteApiCache = Action("DeleteApiCache")
DeleteApiKey = Action("DeleteApiKey")
DeleteDataSource = Action("DeleteDataSource")
DeleteDomainName = Action("DeleteDomainName")
DeleteFunction = Action("DeleteFunction")
DeleteGraphqlApi = Action("DeleteGraphqlApi")
DeleteResolver = Action("DeleteResolver")
DeleteType = Action("DeleteType")
DisassociateApi = Action("DisassociateApi")
EvaluateMappingTemplate = Action("EvaluateMappingTemplate")
FlushApiCache = Action("FlushApiCache")
GetApiAssociation = Action("GetApiAssociation")
GetApiCache = Action("GetApiCache")
GetDataSource = Action("GetDataSource")
GetDomainName = Action("GetDomainName")
GetFunction = Action("GetFunction")
GetGraphqlApi = Action("GetGraphqlApi")
GetIntrospectionSchema = Action("GetIntrospectionSchema")
GetResolver = Action("GetResolver")
GetSchemaCreationStatus = Action("GetSchemaCreationStatus")
GetType = Action("GetType")
GraphQL = Action("GraphQL")
ListApiKeys = Action("ListApiKeys")
ListDataSources = Action("ListDataSources")
ListDomainNames = Action("ListDomainNames")
ListFunctions = Action("ListFunctions")
ListGraphqlApis = Action("ListGraphqlApis")
ListResolvers = Action("ListResolvers")
ListResolversByFunction = Action("ListResolversByFunction")
ListTagsForResource = Action("ListTagsForResource")
ListTypes = Action("ListTypes")
SetWebACL = Action("SetWebACL")
StartSchemaCreation = Action("StartSchemaCreation")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApiCache = Action("UpdateApiCache")
UpdateApiKey = Action("UpdateApiKey")
UpdateDataSource = Action("UpdateDataSource")
UpdateDomainName = Action("UpdateDomainName")
UpdateFunction = Action("UpdateFunction")
UpdateGraphqlApi = Action("UpdateGraphqlApi")
UpdateResolver = Action("UpdateResolver")
UpdateType = Action("UpdateType")
