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


CreateIdMappingWorkflow = Action("CreateIdMappingWorkflow")
CreateMatchingWorkflow = Action("CreateMatchingWorkflow")
CreateSchemaMapping = Action("CreateSchemaMapping")
DeleteIdMappingWorkflow = Action("DeleteIdMappingWorkflow")
DeleteMatchingWorkflow = Action("DeleteMatchingWorkflow")
DeleteSchemaMapping = Action("DeleteSchemaMapping")
GetIdMappingJob = Action("GetIdMappingJob")
GetIdMappingWorkflow = Action("GetIdMappingWorkflow")
GetMatchId = Action("GetMatchId")
GetMatchingJob = Action("GetMatchingJob")
GetMatchingWorkflow = Action("GetMatchingWorkflow")
GetProviderService = Action("GetProviderService")
GetSchemaMapping = Action("GetSchemaMapping")
ListIdMappingJobs = Action("ListIdMappingJobs")
ListIdMappingWorkflows = Action("ListIdMappingWorkflows")
ListMatchingJobs = Action("ListMatchingJobs")
ListMatchingWorkflows = Action("ListMatchingWorkflows")
ListProviderServices = Action("ListProviderServices")
ListSchemaMappings = Action("ListSchemaMappings")
ListTagsForResource = Action("ListTagsForResource")
StartIdMappingJob = Action("StartIdMappingJob")
StartMatchingJob = Action("StartMatchingJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateIdMappingWorkflow = Action("UpdateIdMappingWorkflow")
UpdateMatchingWorkflow = Action("UpdateMatchingWorkflow")
UpdateSchemaMapping = Action("UpdateSchemaMapping")
