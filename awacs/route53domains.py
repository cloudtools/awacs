# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Route 53 Domains"
prefix = "route53domains"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AcceptDomainTransferFromAnotherAwsAccount = Action(
    "AcceptDomainTransferFromAnotherAwsAccount"
)
CancelDomainTransferToAnotherAwsAccount = Action(
    "CancelDomainTransferToAnotherAwsAccount"
)
CheckDomainAvailability = Action("CheckDomainAvailability")
CheckDomainTransferability = Action("CheckDomainTransferability")
DeleteTagsForDomain = Action("DeleteTagsForDomain")
DisableDomainAutoRenew = Action("DisableDomainAutoRenew")
DisableDomainTransferLock = Action("DisableDomainTransferLock")
EnableDomainAutoRenew = Action("EnableDomainAutoRenew")
EnableDomainTransferLock = Action("EnableDomainTransferLock")
GetContactReachabilityStatus = Action("GetContactReachabilityStatus")
GetDomainDetail = Action("GetDomainDetail")
GetDomainSuggestions = Action("GetDomainSuggestions")
GetOperationDetail = Action("GetOperationDetail")
ListDomains = Action("ListDomains")
ListOperations = Action("ListOperations")
ListTagsForDomain = Action("ListTagsForDomain")
RegisterDomain = Action("RegisterDomain")
RejectDomainTransferFromAnotherAwsAccount = Action(
    "RejectDomainTransferFromAnotherAwsAccount"
)
RenewDomain = Action("RenewDomain")
ResendContactReachabilityEmail = Action("ResendContactReachabilityEmail")
RetrieveDomainAuthCode = Action("RetrieveDomainAuthCode")
TransferDomain = Action("TransferDomain")
TransferDomainToAnotherAwsAccount = Action("TransferDomainToAnotherAwsAccount")
UpdateDomainContact = Action("UpdateDomainContact")
UpdateDomainContactPrivacy = Action("UpdateDomainContactPrivacy")
UpdateDomainNameservers = Action("UpdateDomainNameservers")
UpdateTagsForDomain = Action("UpdateTagsForDomain")
ViewBilling = Action("ViewBilling")
