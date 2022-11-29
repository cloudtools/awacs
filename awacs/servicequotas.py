# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Service Quotas"
prefix = "servicequotas"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateServiceQuotaTemplate = Action("AssociateServiceQuotaTemplate")
DeleteServiceQuotaIncreaseRequestFromTemplate = Action(
    "DeleteServiceQuotaIncreaseRequestFromTemplate"
)
DisassociateServiceQuotaTemplate = Action("DisassociateServiceQuotaTemplate")
GetAWSDefaultServiceQuota = Action("GetAWSDefaultServiceQuota")
GetAssociationForServiceQuotaTemplate = Action("GetAssociationForServiceQuotaTemplate")
GetRequestedServiceQuotaChange = Action("GetRequestedServiceQuotaChange")
GetServiceQuota = Action("GetServiceQuota")
GetServiceQuotaIncreaseRequestFromTemplate = Action(
    "GetServiceQuotaIncreaseRequestFromTemplate"
)
ListAWSDefaultServiceQuotas = Action("ListAWSDefaultServiceQuotas")
ListRequestedServiceQuotaChangeHistory = Action(
    "ListRequestedServiceQuotaChangeHistory"
)
ListRequestedServiceQuotaChangeHistoryByQuota = Action(
    "ListRequestedServiceQuotaChangeHistoryByQuota"
)
ListServiceQuotaIncreaseRequestsInTemplate = Action(
    "ListServiceQuotaIncreaseRequestsInTemplate"
)
ListServiceQuotas = Action("ListServiceQuotas")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
PutServiceQuotaIncreaseRequestIntoTemplate = Action(
    "PutServiceQuotaIncreaseRequestIntoTemplate"
)
RequestServiceQuotaIncrease = Action("RequestServiceQuotaIncrease")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
