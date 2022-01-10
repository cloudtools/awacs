# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Shield"
prefix = "shield"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateDRTLogBucket = Action("AssociateDRTLogBucket")
AssociateDRTRole = Action("AssociateDRTRole")
AssociateHealthCheck = Action("AssociateHealthCheck")
AssociateProactiveEngagementDetails = Action("AssociateProactiveEngagementDetails")
CreateProtection = Action("CreateProtection")
CreateProtectionGroup = Action("CreateProtectionGroup")
CreateSubscription = Action("CreateSubscription")
DeleteProtection = Action("DeleteProtection")
DeleteProtectionGroup = Action("DeleteProtectionGroup")
DeleteSubscription = Action("DeleteSubscription")
DescribeAttack = Action("DescribeAttack")
DescribeAttackStatistics = Action("DescribeAttackStatistics")
DescribeDRTAccess = Action("DescribeDRTAccess")
DescribeEmergencyContactSettings = Action("DescribeEmergencyContactSettings")
DescribeProtection = Action("DescribeProtection")
DescribeProtectionGroup = Action("DescribeProtectionGroup")
DescribeSubscription = Action("DescribeSubscription")
DisableApplicationLayerAutomaticResponse = Action(
    "DisableApplicationLayerAutomaticResponse"
)
DisableProactiveEngagement = Action("DisableProactiveEngagement")
DisassociateDRTLogBucket = Action("DisassociateDRTLogBucket")
DisassociateDRTRole = Action("DisassociateDRTRole")
DisassociateHealthCheck = Action("DisassociateHealthCheck")
EnableApplicationLayerAutomaticResponse = Action(
    "EnableApplicationLayerAutomaticResponse"
)
EnableProactiveEngagement = Action("EnableProactiveEngagement")
GetSubscriptionState = Action("GetSubscriptionState")
ListAttacks = Action("ListAttacks")
ListProtectionGroups = Action("ListProtectionGroups")
ListProtections = Action("ListProtections")
ListResourcesInProtectionGroup = Action("ListResourcesInProtectionGroup")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApplicationLayerAutomaticResponse = Action(
    "UpdateApplicationLayerAutomaticResponse"
)
UpdateEmergencyContactSettings = Action("UpdateEmergencyContactSettings")
UpdateProtectionGroup = Action("UpdateProtectionGroup")
UpdateSubscription = Action("UpdateSubscription")
