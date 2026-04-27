# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Marketplace"
prefix = "aws-marketplace"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptAgreementApprovalRequest = Action("AcceptAgreementApprovalRequest")
AcceptAgreementCancellationRequest = Action("AcceptAgreementCancellationRequest")
AcceptAgreementPaymentRequest = Action("AcceptAgreementPaymentRequest")
AcceptAgreementRequest = Action("AcceptAgreementRequest")
AssociateProductsWithPrivateMarketplace = Action(
    "AssociateProductsWithPrivateMarketplace"
)
BatchCreateBillingAdjustmentRequest = Action("BatchCreateBillingAdjustmentRequest")
BatchMeterUsage = Action("BatchMeterUsage")
CancelAgreement = Action("CancelAgreement")
CancelAgreementCancellationRequest = Action("CancelAgreementCancellationRequest")
CancelAgreementPaymentRequest = Action("CancelAgreementPaymentRequest")
CancelAgreementRequest = Action("CancelAgreementRequest")
CancelChangeSet = Action("CancelChangeSet")
CompleteTask = Action("CompleteTask")
CreateAgreementRequest = Action("CreateAgreementRequest")
CreatePrivateMarketplace = Action("CreatePrivateMarketplace")
CreatePrivateMarketplaceProfile = Action("CreatePrivateMarketplaceProfile")
CreatePrivateMarketplaceRequests = Action("CreatePrivateMarketplaceRequests")
DeleteResourcePolicy = Action("DeleteResourcePolicy")
DescribeAgreement = Action("DescribeAgreement")
DescribeAssessment = Action("DescribeAssessment")
DescribeBuilds = Action("DescribeBuilds")
DescribeChangeSet = Action("DescribeChangeSet")
DescribeEntity = Action("DescribeEntity")
DescribePrivateMarketplaceProducts = Action("DescribePrivateMarketplaceProducts")
DescribePrivateMarketplaceProfile = Action("DescribePrivateMarketplaceProfile")
DescribePrivateMarketplaceRequests = Action("DescribePrivateMarketplaceRequests")
DescribePrivateMarketplaceSettings = Action("DescribePrivateMarketplaceSettings")
DescribePrivateMarketplaceStatus = Action("DescribePrivateMarketplaceStatus")
DescribeProcurementSystemConfiguration = Action(
    "DescribeProcurementSystemConfiguration"
)
DescribeTask = Action("DescribeTask")
DisassociateProductsFromPrivateMarketplace = Action(
    "DisassociateProductsFromPrivateMarketplace"
)
GetAgreementApprovalRequest = Action("GetAgreementApprovalRequest")
GetAgreementCancellationRequest = Action("GetAgreementCancellationRequest")
GetAgreementEntitlements = Action("GetAgreementEntitlements")
GetAgreementPaymentRequest = Action("GetAgreementPaymentRequest")
GetAgreementRequest = Action("GetAgreementRequest")
GetAgreementTerms = Action("GetAgreementTerms")
GetBillingAdjustmentRequest = Action("GetBillingAdjustmentRequest")
GetBuyerDashboard = Action("GetBuyerDashboard")
GetEntitlements = Action("GetEntitlements")
GetInvoiceSubmissionTask = Action("GetInvoiceSubmissionTask")
GetListing = Action("GetListing")
GetOffer = Action("GetOffer")
GetOfferSet = Action("GetOfferSet")
GetOfferTerms = Action("GetOfferTerms")
GetProduct = Action("GetProduct")
GetResourcePolicy = Action("GetResourcePolicy")
GetSellerDashboard = Action("GetSellerDashboard")
ListAgreementApprovalRequests = Action("ListAgreementApprovalRequests")
ListAgreementCancellationRequests = Action("ListAgreementCancellationRequests")
ListAgreementCharges = Action("ListAgreementCharges")
ListAgreementInvoiceLineItems = Action("ListAgreementInvoiceLineItems")
ListAgreementPaymentRequests = Action("ListAgreementPaymentRequests")
ListAgreementRequests = Action("ListAgreementRequests")
ListAssessments = Action("ListAssessments")
ListBillingAdjustmentRequests = Action("ListBillingAdjustmentRequests")
ListBuilds = Action("ListBuilds")
ListChangeSets = Action("ListChangeSets")
ListEntities = Action("ListEntities")
ListEntitlementDetails = Action("ListEntitlementDetails")
ListFulfillmentOptions = Action("ListFulfillmentOptions")
ListInvoiceSubmissionTasks = Action("ListInvoiceSubmissionTasks")
ListPayables = Action("ListPayables")
ListPrivateListings = Action("ListPrivateListings")
ListPrivateMarketplaceProducts = Action("ListPrivateMarketplaceProducts")
ListPrivateMarketplaceRequests = Action("ListPrivateMarketplaceRequests")
ListPurchaseOptions = Action("ListPurchaseOptions")
ListTagsForResource = Action("ListTagsForResource")
ListTasks = Action("ListTasks")
MeterUsage = Action("MeterUsage")
PutDeploymentParameter = Action("PutDeploymentParameter")
PutProcurementSystemConfiguration = Action("PutProcurementSystemConfiguration")
PutResourcePolicy = Action("PutResourcePolicy")
RegisterUsage = Action("RegisterUsage")
RejectAgreementApprovalRequest = Action("RejectAgreementApprovalRequest")
RejectAgreementCancellationRequest = Action("RejectAgreementCancellationRequest")
RejectAgreementPaymentRequest = Action("RejectAgreementPaymentRequest")
ResolveCustomer = Action("ResolveCustomer")
SearchAgreements = Action("SearchAgreements")
SearchFacets = Action("SearchFacets")
SearchListings = Action("SearchListings")
SendAgreementCancellationRequest = Action("SendAgreementCancellationRequest")
SendAgreementPaymentRequest = Action("SendAgreementPaymentRequest")
StartBuild = Action("StartBuild")
StartChangeSet = Action("StartChangeSet")
StartInvoiceSubmissionTask = Action("StartInvoiceSubmissionTask")
StartPrivateMarketplace = Action("StartPrivateMarketplace")
StopPrivateMarketplace = Action("StopPrivateMarketplace")
Subscribe = Action("Subscribe")
TagResource = Action("TagResource")
Unsubscribe = Action("Unsubscribe")
UntagResource = Action("UntagResource")
UpdateAgreementApprovalRequest = Action("UpdateAgreementApprovalRequest")
UpdatePrivateMarketplaceProfile = Action("UpdatePrivateMarketplaceProfile")
UpdatePrivateMarketplaceSettings = Action("UpdatePrivateMarketplaceSettings")
UpdatePurchaseOrders = Action("UpdatePurchaseOrders")
UpdateTask = Action("UpdateTask")
ViewSubscriptions = Action("ViewSubscriptions")
