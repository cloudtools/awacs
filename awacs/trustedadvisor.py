# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Trusted Advisor'
prefix = 'trustedadvisor'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DescribeAccount = Action('DescribeAccount')
DescribeAccountAccess = Action('DescribeAccountAccess')
DescribeCheckItems = Action('DescribeCheckItems')
DescribeCheckRefreshStatuses = Action('DescribeCheckRefreshStatuses')
DescribeCheckSummaries = Action('DescribeCheckSummaries')
DescribeChecks = Action('DescribeChecks')
DescribeNotificationPreferences = \
    Action('DescribeNotificationPreferences')
ExcludeCheckItems = Action('ExcludeCheckItems')
IncludeCheckItems = Action('IncludeCheckItems')
RefreshCheck = Action('RefreshCheck')
SetAccountAccess = Action('SetAccountAccess')
UpdateNotificationPreferences = Action('UpdateNotificationPreferences')
