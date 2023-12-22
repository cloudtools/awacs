# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Q Business"
prefix = "qbusiness"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddUserLicenses = Action("AddUserLicenses")
BatchDeleteDocument = Action("BatchDeleteDocument")
BatchPutDocument = Action("BatchPutDocument")
Chat = Action("Chat")
ChatSync = Action("ChatSync")
CreateApplication = Action("CreateApplication")
CreateDataSource = Action("CreateDataSource")
CreateIndex = Action("CreateIndex")
CreateLicense = Action("CreateLicense")
CreatePlugin = Action("CreatePlugin")
CreateRetriever = Action("CreateRetriever")
CreateUser = Action("CreateUser")
CreateWebExperience = Action("CreateWebExperience")
DeleteApplication = Action("DeleteApplication")
DeleteChatControlsConfiguration = Action("DeleteChatControlsConfiguration")
DeleteConversation = Action("DeleteConversation")
DeleteDataSource = Action("DeleteDataSource")
DeleteGroup = Action("DeleteGroup")
DeleteIndex = Action("DeleteIndex")
DeletePlugin = Action("DeletePlugin")
DeleteRetriever = Action("DeleteRetriever")
DeleteUser = Action("DeleteUser")
DeleteWebExperience = Action("DeleteWebExperience")
GetApplication = Action("GetApplication")
GetChatControlsConfiguration = Action("GetChatControlsConfiguration")
GetDataSource = Action("GetDataSource")
GetGroup = Action("GetGroup")
GetIndex = Action("GetIndex")
GetLicense = Action("GetLicense")
GetPlugin = Action("GetPlugin")
GetRetriever = Action("GetRetriever")
GetUser = Action("GetUser")
GetWebExperience = Action("GetWebExperience")
ListApplications = Action("ListApplications")
ListConversations = Action("ListConversations")
ListDataSourceSyncJobs = Action("ListDataSourceSyncJobs")
ListDataSources = Action("ListDataSources")
ListDocuments = Action("ListDocuments")
ListGroups = Action("ListGroups")
ListIndices = Action("ListIndices")
ListMessages = Action("ListMessages")
ListPlugins = Action("ListPlugins")
ListRetrievers = Action("ListRetrievers")
ListTagsForResource = Action("ListTagsForResource")
ListUserLicenses = Action("ListUserLicenses")
ListWebExperiences = Action("ListWebExperiences")
PutFeedback = Action("PutFeedback")
PutGroup = Action("PutGroup")
RemoveUserLicenses = Action("RemoveUserLicenses")
StartDataSourceSyncJob = Action("StartDataSourceSyncJob")
StopDataSourceSyncJob = Action("StopDataSourceSyncJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateChatControlsConfiguration = Action("UpdateChatControlsConfiguration")
UpdateDataSource = Action("UpdateDataSource")
UpdateIndex = Action("UpdateIndex")
UpdatePlugin = Action("UpdatePlugin")
UpdateRetriever = Action("UpdateRetriever")
UpdateUser = Action("UpdateUser")
UpdateWebExperience = Action("UpdateWebExperience")
