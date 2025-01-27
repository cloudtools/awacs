# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Connect"
prefix = "connect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


ActivateEvaluationForm = Action("ActivateEvaluationForm")
AdminGetEmergencyAccessToken = Action("AdminGetEmergencyAccessToken")
AssociateAnalyticsDataSet = Action("AssociateAnalyticsDataSet")
AssociateApprovedOrigin = Action("AssociateApprovedOrigin")
AssociateBot = Action("AssociateBot")
AssociateCustomerProfilesDomain = Action("AssociateCustomerProfilesDomain")
AssociateDefaultVocabulary = Action("AssociateDefaultVocabulary")
AssociateFlow = Action("AssociateFlow")
AssociateInstanceStorageConfig = Action("AssociateInstanceStorageConfig")
AssociateLambdaFunction = Action("AssociateLambdaFunction")
AssociateLexBot = Action("AssociateLexBot")
AssociatePhoneNumberContactFlow = Action("AssociatePhoneNumberContactFlow")
AssociateQueueQuickConnects = Action("AssociateQueueQuickConnects")
AssociateRoutingProfileQueues = Action("AssociateRoutingProfileQueues")
AssociateSecurityKey = Action("AssociateSecurityKey")
AssociateTrafficDistributionGroupUser = Action("AssociateTrafficDistributionGroupUser")
AssociateUserProficiencies = Action("AssociateUserProficiencies")
BatchAssociateAnalyticsDataSet = Action("BatchAssociateAnalyticsDataSet")
BatchDisassociateAnalyticsDataSet = Action("BatchDisassociateAnalyticsDataSet")
BatchGetAttachedFileMetadata = Action("BatchGetAttachedFileMetadata")
BatchGetFlowAssociation = Action("BatchGetFlowAssociation")
BatchPutContact = Action("BatchPutContact")
ClaimPhoneNumber = Action("ClaimPhoneNumber")
CompleteAttachedFileUpload = Action("CompleteAttachedFileUpload")
CreateAgentStatus = Action("CreateAgentStatus")
CreateAuthenticationProfile = Action("CreateAuthenticationProfile")
CreateContactFlow = Action("CreateContactFlow")
CreateContactFlowModule = Action("CreateContactFlowModule")
CreateContactFlowVersion = Action("CreateContactFlowVersion")
CreateEmailAddress = Action("CreateEmailAddress")
CreateEvaluationForm = Action("CreateEvaluationForm")
CreateHoursOfOperation = Action("CreateHoursOfOperation")
CreateHoursOfOperationOverride = Action("CreateHoursOfOperationOverride")
CreateInstance = Action("CreateInstance")
CreateIntegrationAssociation = Action("CreateIntegrationAssociation")
CreateParticipant = Action("CreateParticipant")
CreatePersistentContactAssociation = Action("CreatePersistentContactAssociation")
CreatePredefinedAttribute = Action("CreatePredefinedAttribute")
CreatePrompt = Action("CreatePrompt")
CreatePushNotificationRegistration = Action("CreatePushNotificationRegistration")
CreateQueue = Action("CreateQueue")
CreateQuickConnect = Action("CreateQuickConnect")
CreateRoutingProfile = Action("CreateRoutingProfile")
CreateRule = Action("CreateRule")
CreateSecurityProfile = Action("CreateSecurityProfile")
CreateTaskTemplate = Action("CreateTaskTemplate")
CreateTrafficDistributionGroup = Action("CreateTrafficDistributionGroup")
CreateUseCase = Action("CreateUseCase")
CreateUser = Action("CreateUser")
CreateUserHierarchyGroup = Action("CreateUserHierarchyGroup")
CreateView = Action("CreateView")
CreateViewVersion = Action("CreateViewVersion")
CreateVocabulary = Action("CreateVocabulary")
DeactivateEvaluationForm = Action("DeactivateEvaluationForm")
DeleteAttachedFile = Action("DeleteAttachedFile")
DeleteContactEvaluation = Action("DeleteContactEvaluation")
DeleteContactFlow = Action("DeleteContactFlow")
DeleteContactFlowModule = Action("DeleteContactFlowModule")
DeleteContactFlowVersion = Action("DeleteContactFlowVersion")
DeleteEmailAddress = Action("DeleteEmailAddress")
DeleteEvaluationForm = Action("DeleteEvaluationForm")
DeleteHoursOfOperation = Action("DeleteHoursOfOperation")
DeleteHoursOfOperationOverride = Action("DeleteHoursOfOperationOverride")
DeleteInstance = Action("DeleteInstance")
DeleteIntegrationAssociation = Action("DeleteIntegrationAssociation")
DeletePredefinedAttribute = Action("DeletePredefinedAttribute")
DeletePrompt = Action("DeletePrompt")
DeletePushNotificationRegistration = Action("DeletePushNotificationRegistration")
DeleteQueue = Action("DeleteQueue")
DeleteQuickConnect = Action("DeleteQuickConnect")
DeleteRoutingProfile = Action("DeleteRoutingProfile")
DeleteRule = Action("DeleteRule")
DeleteSecurityProfile = Action("DeleteSecurityProfile")
DeleteTaskTemplate = Action("DeleteTaskTemplate")
DeleteTrafficDistributionGroup = Action("DeleteTrafficDistributionGroup")
DeleteUseCase = Action("DeleteUseCase")
DeleteUser = Action("DeleteUser")
DeleteUserHierarchyGroup = Action("DeleteUserHierarchyGroup")
DeleteView = Action("DeleteView")
DeleteViewVersion = Action("DeleteViewVersion")
DeleteVocabulary = Action("DeleteVocabulary")
DescribeAgentStatus = Action("DescribeAgentStatus")
DescribeAuthenticationProfile = Action("DescribeAuthenticationProfile")
DescribeContact = Action("DescribeContact")
DescribeContactEvaluation = Action("DescribeContactEvaluation")
DescribeContactFlow = Action("DescribeContactFlow")
DescribeContactFlowModule = Action("DescribeContactFlowModule")
DescribeEmailAddress = Action("DescribeEmailAddress")
DescribeEvaluationForm = Action("DescribeEvaluationForm")
DescribeForecastingPlanningSchedulingIntegration = Action(
    "DescribeForecastingPlanningSchedulingIntegration"
)
DescribeHoursOfOperation = Action("DescribeHoursOfOperation")
DescribeHoursOfOperationOverride = Action("DescribeHoursOfOperationOverride")
DescribeInstance = Action("DescribeInstance")
DescribeInstanceAttribute = Action("DescribeInstanceAttribute")
DescribeInstanceStorageConfig = Action("DescribeInstanceStorageConfig")
DescribePhoneNumber = Action("DescribePhoneNumber")
DescribePredefinedAttribute = Action("DescribePredefinedAttribute")
DescribePrompt = Action("DescribePrompt")
DescribeQueue = Action("DescribeQueue")
DescribeQuickConnect = Action("DescribeQuickConnect")
DescribeRoutingProfile = Action("DescribeRoutingProfile")
DescribeRule = Action("DescribeRule")
DescribeSecurityProfile = Action("DescribeSecurityProfile")
DescribeTrafficDistributionGroup = Action("DescribeTrafficDistributionGroup")
DescribeUser = Action("DescribeUser")
DescribeUserHierarchyGroup = Action("DescribeUserHierarchyGroup")
DescribeUserHierarchyStructure = Action("DescribeUserHierarchyStructure")
DescribeView = Action("DescribeView")
DescribeVocabulary = Action("DescribeVocabulary")
DestroyInstance = Action("DestroyInstance")
DisassociateAnalyticsDataSet = Action("DisassociateAnalyticsDataSet")
DisassociateApprovedOrigin = Action("DisassociateApprovedOrigin")
DisassociateBot = Action("DisassociateBot")
DisassociateCustomerProfilesDomain = Action("DisassociateCustomerProfilesDomain")
DisassociateFlow = Action("DisassociateFlow")
DisassociateInstanceStorageConfig = Action("DisassociateInstanceStorageConfig")
DisassociateLambdaFunction = Action("DisassociateLambdaFunction")
DisassociateLexBot = Action("DisassociateLexBot")
DisassociatePhoneNumberContactFlow = Action("DisassociatePhoneNumberContactFlow")
DisassociateQueueQuickConnects = Action("DisassociateQueueQuickConnects")
DisassociateRoutingProfileQueues = Action("DisassociateRoutingProfileQueues")
DisassociateSecurityKey = Action("DisassociateSecurityKey")
DisassociateTrafficDistributionGroupUser = Action(
    "DisassociateTrafficDistributionGroupUser"
)
DisassociateUserProficiencies = Action("DisassociateUserProficiencies")
DismissUserContact = Action("DismissUserContact")
GetAttachedFile = Action("GetAttachedFile")
GetContactAttributes = Action("GetContactAttributes")
GetCurrentMetricData = Action("GetCurrentMetricData")
GetCurrentUserData = Action("GetCurrentUserData")
GetEffectiveHoursOfOperations = Action("GetEffectiveHoursOfOperations")
GetFederationToken = Action("GetFederationToken")
GetFederationTokens = Action("GetFederationTokens")
GetFlowAssociation = Action("GetFlowAssociation")
GetMetricData = Action("GetMetricData")
GetMetricDataV2 = Action("GetMetricDataV2")
GetPromptFile = Action("GetPromptFile")
GetTaskTemplate = Action("GetTaskTemplate")
GetTrafficDistribution = Action("GetTrafficDistribution")
ImportPhoneNumber = Action("ImportPhoneNumber")
ListAgentStatuses = Action("ListAgentStatuses")
ListAnalyticsDataAssociations = Action("ListAnalyticsDataAssociations")
ListApprovedOrigins = Action("ListApprovedOrigins")
ListAssociatedContacts = Action("ListAssociatedContacts")
ListAuthenticationProfiles = Action("ListAuthenticationProfiles")
ListBots = Action("ListBots")
ListContactEvaluations = Action("ListContactEvaluations")
ListContactFlowModules = Action("ListContactFlowModules")
ListContactFlowVersions = Action("ListContactFlowVersions")
ListContactFlows = Action("ListContactFlows")
ListContactReferences = Action("ListContactReferences")
ListDefaultVocabularies = Action("ListDefaultVocabularies")
ListEvaluationFormVersions = Action("ListEvaluationFormVersions")
ListEvaluationForms = Action("ListEvaluationForms")
ListFlowAssociations = Action("ListFlowAssociations")
ListHoursOfOperationOverrides = Action("ListHoursOfOperationOverrides")
ListHoursOfOperations = Action("ListHoursOfOperations")
ListInstanceAttributes = Action("ListInstanceAttributes")
ListInstanceStorageConfigs = Action("ListInstanceStorageConfigs")
ListInstances = Action("ListInstances")
ListIntegrationAssociations = Action("ListIntegrationAssociations")
ListLambdaFunctions = Action("ListLambdaFunctions")
ListLexBots = Action("ListLexBots")
ListPhoneNumbers = Action("ListPhoneNumbers")
ListPhoneNumbersV2 = Action("ListPhoneNumbersV2")
ListPredefinedAttributes = Action("ListPredefinedAttributes")
ListPrompts = Action("ListPrompts")
ListQueueQuickConnects = Action("ListQueueQuickConnects")
ListQueues = Action("ListQueues")
ListQuickConnects = Action("ListQuickConnects")
ListRealtimeContactAnalysisSegments = Action("ListRealtimeContactAnalysisSegments")
ListRealtimeContactAnalysisSegmentsV2 = Action("ListRealtimeContactAnalysisSegmentsV2")
ListRoutingProfileQueues = Action("ListRoutingProfileQueues")
ListRoutingProfiles = Action("ListRoutingProfiles")
ListRule = Action("ListRule")
ListRules = Action("ListRules")
ListSecurityKeys = Action("ListSecurityKeys")
ListSecurityProfileApplications = Action("ListSecurityProfileApplications")
ListSecurityProfilePermissions = Action("ListSecurityProfilePermissions")
ListSecurityProfiles = Action("ListSecurityProfiles")
ListTagsForResource = Action("ListTagsForResource")
ListTaskTemplates = Action("ListTaskTemplates")
ListTrafficDistributionGroupUsers = Action("ListTrafficDistributionGroupUsers")
ListTrafficDistributionGroups = Action("ListTrafficDistributionGroups")
ListUseCases = Action("ListUseCases")
ListUserHierarchyGroups = Action("ListUserHierarchyGroups")
ListUserProficiencies = Action("ListUserProficiencies")
ListUsers = Action("ListUsers")
ListViewVersions = Action("ListViewVersions")
ListViews = Action("ListViews")
ModifyInstance = Action("ModifyInstance")
MonitorContact = Action("MonitorContact")
PauseContact = Action("PauseContact")
PutUserStatus = Action("PutUserStatus")
ReleasePhoneNumber = Action("ReleasePhoneNumber")
ReplicateInstance = Action("ReplicateInstance")
ResumeContact = Action("ResumeContact")
ResumeContactRecording = Action("ResumeContactRecording")
SearchAgentStatuses = Action("SearchAgentStatuses")
SearchAvailablePhoneNumbers = Action("SearchAvailablePhoneNumbers")
SearchContactFlowModules = Action("SearchContactFlowModules")
SearchContactFlows = Action("SearchContactFlows")
SearchContacts = Action("SearchContacts")
SearchEmailAddresses = Action("SearchEmailAddresses")
SearchHoursOfOperationOverrides = Action("SearchHoursOfOperationOverrides")
SearchHoursOfOperations = Action("SearchHoursOfOperations")
SearchPredefinedAttributes = Action("SearchPredefinedAttributes")
SearchPrompts = Action("SearchPrompts")
SearchQueues = Action("SearchQueues")
SearchQuickConnects = Action("SearchQuickConnects")
SearchResourceTags = Action("SearchResourceTags")
SearchRoutingProfiles = Action("SearchRoutingProfiles")
SearchSecurityProfiles = Action("SearchSecurityProfiles")
SearchUserHierarchyGroups = Action("SearchUserHierarchyGroups")
SearchUsers = Action("SearchUsers")
SearchVocabularies = Action("SearchVocabularies")
SendChatIntegrationEvent = Action("SendChatIntegrationEvent")
SendIntegrationEvent = Action("SendIntegrationEvent")
SendOutboundEmail = Action("SendOutboundEmail")
StartAttachedFileUpload = Action("StartAttachedFileUpload")
StartChatContact = Action("StartChatContact")
StartContactEvaluation = Action("StartContactEvaluation")
StartContactRecording = Action("StartContactRecording")
StartContactStreaming = Action("StartContactStreaming")
StartEmailContact = Action("StartEmailContact")
StartForecastingPlanningSchedulingIntegration = Action(
    "StartForecastingPlanningSchedulingIntegration"
)
StartOutboundChatContact = Action("StartOutboundChatContact")
StartOutboundEmailContact = Action("StartOutboundEmailContact")
StartOutboundVoiceContact = Action("StartOutboundVoiceContact")
StartScreenSharing = Action("StartScreenSharing")
StartTaskContact = Action("StartTaskContact")
StartWebRTCContact = Action("StartWebRTCContact")
StopContact = Action("StopContact")
StopContactRecording = Action("StopContactRecording")
StopContactStreaming = Action("StopContactStreaming")
StopForecastingPlanningSchedulingIntegration = Action(
    "StopForecastingPlanningSchedulingIntegration"
)
SubmitContactEvaluation = Action("SubmitContactEvaluation")
SuspendContactRecording = Action("SuspendContactRecording")
TagContact = Action("TagContact")
TagResource = Action("TagResource")
TransferContact = Action("TransferContact")
UntagContact = Action("UntagContact")
UntagResource = Action("UntagResource")
UpdateAgentStatus = Action("UpdateAgentStatus")
UpdateAuthenticationProfile = Action("UpdateAuthenticationProfile")
UpdateContact = Action("UpdateContact")
UpdateContactAttributes = Action("UpdateContactAttributes")
UpdateContactEvaluation = Action("UpdateContactEvaluation")
UpdateContactFlowContent = Action("UpdateContactFlowContent")
UpdateContactFlowMetadata = Action("UpdateContactFlowMetadata")
UpdateContactFlowModuleContent = Action("UpdateContactFlowModuleContent")
UpdateContactFlowModuleMetadata = Action("UpdateContactFlowModuleMetadata")
UpdateContactFlowName = Action("UpdateContactFlowName")
UpdateContactRoutingData = Action("UpdateContactRoutingData")
UpdateContactSchedule = Action("UpdateContactSchedule")
UpdateEmailAddressMetadata = Action("UpdateEmailAddressMetadata")
UpdateEvaluationForm = Action("UpdateEvaluationForm")
UpdateHoursOfOperation = Action("UpdateHoursOfOperation")
UpdateHoursOfOperationOverride = Action("UpdateHoursOfOperationOverride")
UpdateInstanceAttribute = Action("UpdateInstanceAttribute")
UpdateInstanceStorageConfig = Action("UpdateInstanceStorageConfig")
UpdateParticipantAuthentication = Action("UpdateParticipantAuthentication")
UpdateParticipantRoleConfig = Action("UpdateParticipantRoleConfig")
UpdatePhoneNumber = Action("UpdatePhoneNumber")
UpdatePhoneNumberMetadata = Action("UpdatePhoneNumberMetadata")
UpdatePredefinedAttribute = Action("UpdatePredefinedAttribute")
UpdatePrompt = Action("UpdatePrompt")
UpdateQueueHoursOfOperation = Action("UpdateQueueHoursOfOperation")
UpdateQueueMaxContacts = Action("UpdateQueueMaxContacts")
UpdateQueueName = Action("UpdateQueueName")
UpdateQueueOutboundCallerConfig = Action("UpdateQueueOutboundCallerConfig")
UpdateQueueOutboundEmailConfig = Action("UpdateQueueOutboundEmailConfig")
UpdateQueueStatus = Action("UpdateQueueStatus")
UpdateQuickConnectConfig = Action("UpdateQuickConnectConfig")
UpdateQuickConnectName = Action("UpdateQuickConnectName")
UpdateRoutingProfileAgentAvailabilityTimer = Action(
    "UpdateRoutingProfileAgentAvailabilityTimer"
)
UpdateRoutingProfileConcurrency = Action("UpdateRoutingProfileConcurrency")
UpdateRoutingProfileDefaultOutboundQueue = Action(
    "UpdateRoutingProfileDefaultOutboundQueue"
)
UpdateRoutingProfileName = Action("UpdateRoutingProfileName")
UpdateRoutingProfileQueues = Action("UpdateRoutingProfileQueues")
UpdateRule = Action("UpdateRule")
UpdateSecurityProfile = Action("UpdateSecurityProfile")
UpdateTaskTemplate = Action("UpdateTaskTemplate")
UpdateTrafficDistribution = Action("UpdateTrafficDistribution")
UpdateUserHierarchy = Action("UpdateUserHierarchy")
UpdateUserHierarchyGroupName = Action("UpdateUserHierarchyGroupName")
UpdateUserHierarchyStructure = Action("UpdateUserHierarchyStructure")
UpdateUserIdentityInfo = Action("UpdateUserIdentityInfo")
UpdateUserPhoneConfig = Action("UpdateUserPhoneConfig")
UpdateUserProficiencies = Action("UpdateUserProficiencies")
UpdateUserRoutingProfile = Action("UpdateUserRoutingProfile")
UpdateUserSecurityProfiles = Action("UpdateUserSecurityProfiles")
UpdateViewContent = Action("UpdateViewContent")
UpdateViewMetadata = Action("UpdateViewMetadata")
UpdatedescribeContent = Action("UpdatedescribeContent")
