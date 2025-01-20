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
AllowVendedLogDeliveryForResource = Action("AllowVendedLogDeliveryForResource")
AssociatePermission = Action("AssociatePermission")
BatchDeleteDocument = Action("BatchDeleteDocument")
BatchPutDocument = Action("BatchPutDocument")
CancelSubscription = Action("CancelSubscription")
Chat = Action("Chat")
ChatSync = Action("ChatSync")
CreateApplication = Action("CreateApplication")
CreateDataAccessor = Action("CreateDataAccessor")
CreateDataSource = Action("CreateDataSource")
CreateIndex = Action("CreateIndex")
CreateIntegration = Action("CreateIntegration")
CreateLicense = Action("CreateLicense")
CreatePlugin = Action("CreatePlugin")
CreateRetriever = Action("CreateRetriever")
CreateSubscription = Action("CreateSubscription")
CreateUser = Action("CreateUser")
CreateWebExperience = Action("CreateWebExperience")
DeleteApplication = Action("DeleteApplication")
DeleteChatControlsConfiguration = Action("DeleteChatControlsConfiguration")
DeleteConversation = Action("DeleteConversation")
DeleteDataAccessor = Action("DeleteDataAccessor")
DeleteDataSource = Action("DeleteDataSource")
DeleteGroup = Action("DeleteGroup")
DeleteIndex = Action("DeleteIndex")
DeleteIntegration = Action("DeleteIntegration")
DeletePlugin = Action("DeletePlugin")
DeleteRetriever = Action("DeleteRetriever")
DeleteUser = Action("DeleteUser")
DeleteWebExperience = Action("DeleteWebExperience")
DisableAclOnDataSource = Action("DisableAclOnDataSource")
DisassociatePermission = Action("DisassociatePermission")
GetApplication = Action("GetApplication")
GetChatControlsConfiguration = Action("GetChatControlsConfiguration")
GetDataAccessor = Action("GetDataAccessor")
GetDataSource = Action("GetDataSource")
GetGroup = Action("GetGroup")
GetIndex = Action("GetIndex")
GetIntegration = Action("GetIntegration")
GetLicense = Action("GetLicense")
GetMedia = Action("GetMedia")
GetPlugin = Action("GetPlugin")
GetPolicy = Action("GetPolicy")
GetRetriever = Action("GetRetriever")
GetUser = Action("GetUser")
GetWebExperience = Action("GetWebExperience")
ListApplications = Action("ListApplications")
ListAttachments = Action("ListAttachments")
ListConversations = Action("ListConversations")
ListDataAccessors = Action("ListDataAccessors")
ListDataSourceSyncJobs = Action("ListDataSourceSyncJobs")
ListDataSources = Action("ListDataSources")
ListDocuments = Action("ListDocuments")
ListGroups = Action("ListGroups")
ListIndices = Action("ListIndices")
ListIntegrations = Action("ListIntegrations")
ListMessages = Action("ListMessages")
ListPluginActions = Action("ListPluginActions")
ListPluginTypeActions = Action("ListPluginTypeActions")
ListPluginTypeMetadata = Action("ListPluginTypeMetadata")
ListPlugins = Action("ListPlugins")
ListRetrievers = Action("ListRetrievers")
ListSubscriptions = Action("ListSubscriptions")
ListTagsForResource = Action("ListTagsForResource")
ListUserLicenses = Action("ListUserLicenses")
ListWebExperiences = Action("ListWebExperiences")
PutFeedback = Action("PutFeedback")
PutGroup = Action("PutGroup")
PutResourcePolicy = Action("PutResourcePolicy")
RemoveUserLicenses = Action("RemoveUserLicenses")
SearchRelevantContent = Action("SearchRelevantContent")
StartDataSourceSyncJob = Action("StartDataSourceSyncJob")
StartDeployment = Action("StartDeployment")
StopDataSourceSyncJob = Action("StopDataSourceSyncJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplication = Action("UpdateApplication")
UpdateChatControlsConfiguration = Action("UpdateChatControlsConfiguration")
UpdateDataAccessor = Action("UpdateDataAccessor")
UpdateDataSource = Action("UpdateDataSource")
UpdateIndex = Action("UpdateIndex")
UpdateIntegration = Action("UpdateIntegration")
UpdatePlugin = Action("UpdatePlugin")
UpdateRetriever = Action("UpdateRetriever")
UpdateSubscription = Action("UpdateSubscription")
UpdateUser = Action("UpdateUser")
UpdateWebExperience = Action("UpdateWebExperience")
