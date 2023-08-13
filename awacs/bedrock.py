# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Bedrock"
prefix = "bedrock"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAgent = Action("CreateAgent")
CreateAgentActionGroup = Action("CreateAgentActionGroup")
CreateAgentAlias = Action("CreateAgentAlias")
CreateAgentDraftSnapshot = Action("CreateAgentDraftSnapshot")
CreateModelCustomizationJob = Action("CreateModelCustomizationJob")
DeleteCustomModel = Action("DeleteCustomModel")
DeletePrompt = Action("DeletePrompt")
GetAgent = Action("GetAgent")
GetAgentActionGroup = Action("GetAgentActionGroup")
GetAgentAlias = Action("GetAgentAlias")
GetAgentVersion = Action("GetAgentVersion")
GetCustomModel = Action("GetCustomModel")
GetModelCustomizationJob = Action("GetModelCustomizationJob")
GetPrompt = Action("GetPrompt")
InvokeAgent = Action("InvokeAgent")
InvokeModel = Action("InvokeModel")
InvokeModelWithResponseStream = Action("InvokeModelWithResponseStream")
ListAgentActionGroups = Action("ListAgentActionGroups")
ListAgentAliases = Action("ListAgentAliases")
ListAgentVersions = Action("ListAgentVersions")
ListAgents = Action("ListAgents")
ListCustomModels = Action("ListCustomModels")
ListFoundationModels = Action("ListFoundationModels")
ListModelCustomizationJobs = Action("ListModelCustomizationJobs")
ListPrompts = Action("ListPrompts")
ListTagsForResource = Action("ListTagsForResource")
StopModelCustomizationJob = Action("StopModelCustomizationJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAgent = Action("UpdateAgent")
UpdateAgentActionGroup = Action("UpdateAgentActionGroup")
UpdateAgentAlias = Action("UpdateAgentAlias")
UpdatePrompt = Action("UpdatePrompt")
