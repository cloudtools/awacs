# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Security Lake"
prefix = "securitylake"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAwsLogSource = Action("CreateAwsLogSource")
CreateCustomLogSource = Action("CreateCustomLogSource")
CreateDataLake = Action("CreateDataLake")
CreateDataLakeExceptionSubscription = Action("CreateDataLakeExceptionSubscription")
CreateDataLakeOrganizationConfiguration = Action(
    "CreateDataLakeOrganizationConfiguration"
)
CreateDatalake = Action("CreateDatalake")
CreateDatalakeAutoEnable = Action("CreateDatalakeAutoEnable")
CreateDatalakeDelegatedAdmin = Action("CreateDatalakeDelegatedAdmin")
CreateDatalakeExceptionsSubscription = Action("CreateDatalakeExceptionsSubscription")
CreateSubscriber = Action("CreateSubscriber")
CreateSubscriberNotification = Action("CreateSubscriberNotification")
CreateSubscriptionNotificationConfiguration = Action(
    "CreateSubscriptionNotificationConfiguration"
)
DeleteAwsLogSource = Action("DeleteAwsLogSource")
DeleteCustomLogSource = Action("DeleteCustomLogSource")
DeleteDataLake = Action("DeleteDataLake")
DeleteDataLakeExceptionSubscription = Action("DeleteDataLakeExceptionSubscription")
DeleteDataLakeOrganizationConfiguration = Action(
    "DeleteDataLakeOrganizationConfiguration"
)
DeleteDatalake = Action("DeleteDatalake")
DeleteDatalakeAutoEnable = Action("DeleteDatalakeAutoEnable")
DeleteDatalakeDelegatedAdmin = Action("DeleteDatalakeDelegatedAdmin")
DeleteDatalakeExceptionsSubscription = Action("DeleteDatalakeExceptionsSubscription")
DeleteSubscriber = Action("DeleteSubscriber")
DeleteSubscriberNotification = Action("DeleteSubscriberNotification")
DeleteSubscriptionNotificationConfiguration = Action(
    "DeleteSubscriptionNotificationConfiguration"
)
DeregisterDataLakeDelegatedAdministrator = Action(
    "DeregisterDataLakeDelegatedAdministrator"
)
GetDataLakeExceptionSubscription = Action("GetDataLakeExceptionSubscription")
GetDataLakeOrganizationConfiguration = Action("GetDataLakeOrganizationConfiguration")
GetDataLakeSources = Action("GetDataLakeSources")
GetDatalake = Action("GetDatalake")
GetDatalakeAutoEnable = Action("GetDatalakeAutoEnable")
GetDatalakeExceptionsExpiry = Action("GetDatalakeExceptionsExpiry")
GetDatalakeExceptionsSubscription = Action("GetDatalakeExceptionsSubscription")
GetDatalakeStatus = Action("GetDatalakeStatus")
GetSubscriber = Action("GetSubscriber")
GetSubscriptionNotificationConfiguration = Action(
    "GetSubscriptionNotificationConfiguration"
)
ListDataLakeExceptions = Action("ListDataLakeExceptions")
ListDataLakes = Action("ListDataLakes")
ListDatalakeExceptions = Action("ListDatalakeExceptions")
ListLogSources = Action("ListLogSources")
ListSubscribers = Action("ListSubscribers")
ListTagsForResource = Action("ListTagsForResource")
RegisterDataLakeDelegatedAdministrator = Action(
    "RegisterDataLakeDelegatedAdministrator"
)
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateDataLake = Action("UpdateDataLake")
UpdateDataLakeExceptionSubscription = Action("UpdateDataLakeExceptionSubscription")
UpdateDatalake = Action("UpdateDatalake")
UpdateDatalakeExceptionsExpiry = Action("UpdateDatalakeExceptionsExpiry")
UpdateDatalakeExceptionsSubscription = Action("UpdateDatalakeExceptionsSubscription")
UpdateSubscriber = Action("UpdateSubscriber")
UpdateSubscriberNotification = Action("UpdateSubscriberNotification")
UpdateSubscriptionNotificationConfiguration = Action(
    "UpdateSubscriptionNotificationConfiguration"
)
