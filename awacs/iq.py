# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS IQ"
prefix = "iq"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptCall = Action("AcceptCall")
ApprovePaymentRequest = Action("ApprovePaymentRequest")
ApproveProposal = Action("ApproveProposal")
ArchiveConversation = Action("ArchiveConversation")
CompleteProposal = Action("CompleteProposal")
CreateConversation = Action("CreateConversation")
CreateExpert = Action("CreateExpert")
CreateListing = Action("CreateListing")
CreateMilestoneProposal = Action("CreateMilestoneProposal")
CreatePaymentRequest = Action("CreatePaymentRequest")
CreateProject = Action("CreateProject")
CreateRequest = Action("CreateRequest")
CreateScheduledProposal = Action("CreateScheduledProposal")
CreateSeller = Action("CreateSeller")
CreateUpfrontProposal = Action("CreateUpfrontProposal")
DeclineCall = Action("DeclineCall")
DeleteAttachment = Action("DeleteAttachment")
DisableIndividualPublicProfile = Action("DisableIndividualPublicProfile")
DownloadAttachment = Action("DownloadAttachment")
EnableIndividualPublicProfile = Action("EnableIndividualPublicProfile")
EndCall = Action("EndCall")
GetBuyer = Action("GetBuyer")
GetCall = Action("GetCall")
GetChatInfo = Action("GetChatInfo")
GetChatMessages = Action("GetChatMessages")
GetChatToken = Action("GetChatToken")
GetCompanyChatMessages = Action("GetCompanyChatMessages")
GetCompanyProfile = Action("GetCompanyProfile")
GetConversation = Action("GetConversation")
GetExpert = Action("GetExpert")
GetListing = Action("GetListing")
GetMarketplaceSeller = Action("GetMarketplaceSeller")
GetPaymentRequest = Action("GetPaymentRequest")
GetProposal = Action("GetProposal")
GetRequest = Action("GetRequest")
GetReview = Action("GetReview")
HideRequest = Action("HideRequest")
InitiateCall = Action("InitiateCall")
LinkAwsCertification = Action("LinkAwsCertification")
ListAttachments = Action("ListAttachments")
ListConversations = Action("ListConversations")
ListExpertAccessLogs = Action("ListExpertAccessLogs")
ListListings = Action("ListListings")
ListPaymentRequests = Action("ListPaymentRequests")
ListProposals = Action("ListProposals")
ListRequests = Action("ListRequests")
ListReviews = Action("ListReviews")
MarkChatMessageRead = Action("MarkChatMessageRead")
RejectPaymentRequest = Action("RejectPaymentRequest")
RejectProposal = Action("RejectProposal")
SendCompanyChatMessage = Action("SendCompanyChatMessage")
SendIndividualChatMessage = Action("SendIndividualChatMessage")
UnarchiveConversation = Action("UnarchiveConversation")
UnlinkAwsCertification = Action("UnlinkAwsCertification")
UpdateCompanyProfile = Action("UpdateCompanyProfile")
UpdateConversationMembers = Action("UpdateConversationMembers")
UpdateExpert = Action("UpdateExpert")
UpdateListing = Action("UpdateListing")
UpdateRequest = Action("UpdateRequest")
UploadAttachment = Action("UploadAttachment")
WithdrawPaymentRequest = Action("WithdrawPaymentRequest")
WithdrawProposal = Action("WithdrawProposal")
WriteReview = Action("WriteReview")
