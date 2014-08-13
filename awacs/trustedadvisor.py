# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Trusted Advisor'
prefix = 'trustedadvisor'

DescribeCheckItems = Action(prefix, 'DescribeCheckItems')
DescribeCheckRefreshStatuses = \
    Action(prefix, 'DescribeCheckRefreshStatuses')
DescribeCheckStatusHistoryChanges = \
    Action(prefix, 'DescribeCheckStatusHistoryChanges')
DescribeCheckSummaries = Action(prefix, 'DescribeCheckSummaries')
DescribeNotificationPreferences = \
    Action(prefix, 'DescribeNotificationPreferences')
ExcludeCheckItems = Action(prefix, 'ExcludeCheckItems')
IncludeCheckItems = Action(prefix, 'IncludeCheckItems')
RefreshCheck = Action(prefix, 'RefreshCheck')
UpdateNotificationPreferences = \
    Action(prefix, 'UpdateNotificationPreferences')
