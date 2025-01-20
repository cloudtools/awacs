# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Entity Resolution"
prefix = "entityresolution"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddPolicyStatement = Action("AddPolicyStatement")
BatchDeleteUniqueId = Action("BatchDeleteUniqueId")
CreateIdMappingWorkflow = Action("CreateIdMappingWorkflow")
CreateIdNamespace = Action("CreateIdNamespace")
CreateMatchingWorkflow = Action("CreateMatchingWorkflow")
CreateSchemaMapping = Action("CreateSchemaMapping")
DeleteIdMappingWorkflow = Action("DeleteIdMappingWorkflow")
DeleteIdNamespace = Action("DeleteIdNamespace")
DeleteMatchingWorkflow = Action("DeleteMatchingWorkflow")
DeletePolicyStatement = Action("DeletePolicyStatement")
DeleteSchemaMapping = Action("DeleteSchemaMapping")
GetIdMappingJob = Action("GetIdMappingJob")
GetIdMappingWorkflow = Action("GetIdMappingWorkflow")
GetIdNamespace = Action("GetIdNamespace")
GetMatchId = Action("GetMatchId")
GetMatchingJob = Action("GetMatchingJob")
GetMatchingWorkflow = Action("GetMatchingWorkflow")
GetPolicy = Action("GetPolicy")
GetProviderService = Action("GetProviderService")
GetSchemaMapping = Action("GetSchemaMapping")
ListIdMappingJobs = Action("ListIdMappingJobs")
ListIdMappingWorkflows = Action("ListIdMappingWorkflows")
ListIdNamespaces = Action("ListIdNamespaces")
ListMatchingJobs = Action("ListMatchingJobs")
ListMatchingWorkflows = Action("ListMatchingWorkflows")
ListProviderServices = Action("ListProviderServices")
ListSchemaMappings = Action("ListSchemaMappings")
ListTagsForResource = Action("ListTagsForResource")
PutPolicy = Action("PutPolicy")
StartIdMappingJob = Action("StartIdMappingJob")
StartMatchingJob = Action("StartMatchingJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateIdMappingWorkflow = Action("UpdateIdMappingWorkflow")
UpdateIdNamespace = Action("UpdateIdNamespace")
UpdateMatchingWorkflow = Action("UpdateMatchingWorkflow")
UpdateSchemaMapping = Action("UpdateSchemaMapping")
UseIdNamespace = Action("UseIdNamespace")
UseWorkflow = Action("UseWorkflow")
