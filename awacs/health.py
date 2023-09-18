# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Health APIs and Notifications"
prefix = "health"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


DescribeAffectedAccountsForOrganization = Action(
    "DescribeAffectedAccountsForOrganization"
)
DescribeAffectedEntities = Action("DescribeAffectedEntities")
DescribeAffectedEntitiesForOrganization = Action(
    "DescribeAffectedEntitiesForOrganization"
)
DescribeEntityAggregates = Action("DescribeEntityAggregates")
DescribeEntityAggregatesForOrganization = Action(
    "DescribeEntityAggregatesForOrganization"
)
DescribeEventAggregates = Action("DescribeEventAggregates")
DescribeEventDetails = Action("DescribeEventDetails")
DescribeEventDetailsForOrganization = Action("DescribeEventDetailsForOrganization")
DescribeEventTypes = Action("DescribeEventTypes")
DescribeEvents = Action("DescribeEvents")
DescribeEventsForOrganization = Action("DescribeEventsForOrganization")
DescribeHealthServiceStatusForOrganization = Action(
    "DescribeHealthServiceStatusForOrganization"
)
DisableHealthServiceAccessForOrganization = Action(
    "DisableHealthServiceAccessForOrganization"
)
EnableHealthServiceAccessForOrganization = Action(
    "EnableHealthServiceAccessForOrganization"
)
