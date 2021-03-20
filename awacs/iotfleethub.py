# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = 'Fleet Hub for AWS IoT Device Management'
prefix = 'iotfleethub'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApplication = Action('CreateApplication')
CreateDashboard = Action('CreateDashboard')
DeleteApplication = Action('DeleteApplication')
DeleteDashboard = Action('DeleteDashboard')
DescribeApplication = Action('DescribeApplication')
DescribeDashboard = Action('DescribeDashboard')
ListApplications = Action('ListApplications')
ListDashboards = Action('ListDashboards')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
UpdateDashboard = Action('UpdateDashboard')
