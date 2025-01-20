# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Lambda"
prefix = "lambda"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddLayerVersionPermission = Action("AddLayerVersionPermission")
AddPermission = Action("AddPermission")
CreateAlias = Action("CreateAlias")
CreateCodeSigningConfig = Action("CreateCodeSigningConfig")
CreateEventSourceMapping = Action("CreateEventSourceMapping")
CreateFunction = Action("CreateFunction")
CreateFunctionUrlConfig = Action("CreateFunctionUrlConfig")
DeleteAlias = Action("DeleteAlias")
DeleteCodeSigningConfig = Action("DeleteCodeSigningConfig")
DeleteEventSourceMapping = Action("DeleteEventSourceMapping")
DeleteFunction = Action("DeleteFunction")
DeleteFunctionCodeSigningConfig = Action("DeleteFunctionCodeSigningConfig")
DeleteFunctionConcurrency = Action("DeleteFunctionConcurrency")
DeleteFunctionEventInvokeConfig = Action("DeleteFunctionEventInvokeConfig")
DeleteFunctionUrlConfig = Action("DeleteFunctionUrlConfig")
DeleteLayerVersion = Action("DeleteLayerVersion")
DeleteProvisionedConcurrencyConfig = Action("DeleteProvisionedConcurrencyConfig")
DisableReplication = Action("DisableReplication")
EnableReplication = Action("EnableReplication")
GetAccountSettings = Action("GetAccountSettings")
GetAlias = Action("GetAlias")
GetCodeSigningConfig = Action("GetCodeSigningConfig")
GetEventSourceMapping = Action("GetEventSourceMapping")
GetFunction = Action("GetFunction")
GetFunctionCodeSigningConfig = Action("GetFunctionCodeSigningConfig")
GetFunctionConcurrency = Action("GetFunctionConcurrency")
GetFunctionConfiguration = Action("GetFunctionConfiguration")
GetFunctionEventInvokeConfig = Action("GetFunctionEventInvokeConfig")
GetFunctionRecursionConfig = Action("GetFunctionRecursionConfig")
GetFunctionUrlConfig = Action("GetFunctionUrlConfig")
GetLayerVersion = Action("GetLayerVersion")
GetLayerVersionByArn = Action("GetLayerVersionByArn")
GetLayerVersionPolicy = Action("GetLayerVersionPolicy")
GetPolicy = Action("GetPolicy")
GetProvisionedConcurrencyConfig = Action("GetProvisionedConcurrencyConfig")
GetRuntimeManagementConfig = Action("GetRuntimeManagementConfig")
InvokeAsync = Action("InvokeAsync")
InvokeFunction = Action("InvokeFunction")
InvokeFunctionUrl = Action("InvokeFunctionUrl")
ListAliases = Action("ListAliases")
ListCodeSigningConfigs = Action("ListCodeSigningConfigs")
ListEventSourceMappings = Action("ListEventSourceMappings")
ListFunctionEventInvokeConfigs = Action("ListFunctionEventInvokeConfigs")
ListFunctionUrlConfigs = Action("ListFunctionUrlConfigs")
ListFunctions = Action("ListFunctions")
ListFunctionsByCodeSigningConfig = Action("ListFunctionsByCodeSigningConfig")
ListLayerVersions = Action("ListLayerVersions")
ListLayers = Action("ListLayers")
ListProvisionedConcurrencyConfigs = Action("ListProvisionedConcurrencyConfigs")
ListTags = Action("ListTags")
ListVersionsByFunction = Action("ListVersionsByFunction")
PublishLayerVersion = Action("PublishLayerVersion")
PublishVersion = Action("PublishVersion")
PutFunctionCodeSigningConfig = Action("PutFunctionCodeSigningConfig")
PutFunctionConcurrency = Action("PutFunctionConcurrency")
PutFunctionEventInvokeConfig = Action("PutFunctionEventInvokeConfig")
PutFunctionRecursionConfig = Action("PutFunctionRecursionConfig")
PutProvisionedConcurrencyConfig = Action("PutProvisionedConcurrencyConfig")
PutRuntimeManagementConfig = Action("PutRuntimeManagementConfig")
RemoveLayerVersionPermission = Action("RemoveLayerVersionPermission")
RemovePermission = Action("RemovePermission")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAlias = Action("UpdateAlias")
UpdateCodeSigningConfig = Action("UpdateCodeSigningConfig")
UpdateEventSourceMapping = Action("UpdateEventSourceMapping")
UpdateFunctionCode = Action("UpdateFunctionCode")
UpdateFunctionCodeSigningConfig = Action("UpdateFunctionCodeSigningConfig")
UpdateFunctionConfiguration = Action("UpdateFunctionConfiguration")
UpdateFunctionEventInvokeConfig = Action("UpdateFunctionEventInvokeConfig")
UpdateFunctionUrlConfig = Action("UpdateFunctionUrlConfig")
