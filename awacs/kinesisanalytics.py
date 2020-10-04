# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Kinesis Analytics'
prefix = 'kinesisanalytics'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddApplicationCloudWatchLoggingOption = \
    Action('AddApplicationCloudWatchLoggingOption')
AddApplicationInput = Action('AddApplicationInput')
AddApplicationInputProcessingConfiguration = \
    Action('AddApplicationInputProcessingConfiguration')
AddApplicationOutput = Action('AddApplicationOutput')
AddApplicationReferenceDataSource = \
    Action('AddApplicationReferenceDataSource')
AddApplicationVpcConfiguration = Action('AddApplicationVpcConfiguration')
CreateApplication = Action('CreateApplication')
CreateApplicationSnapshot = Action('CreateApplicationSnapshot')
DeleteApplication = Action('DeleteApplication')
DeleteApplicationCloudWatchLoggingOption = \
    Action('DeleteApplicationCloudWatchLoggingOption')
DeleteApplicationInputProcessingConfiguration = \
    Action('DeleteApplicationInputProcessingConfiguration')
DeleteApplicationOutput = Action('DeleteApplicationOutput')
DeleteApplicationReferenceDataSource = \
    Action('DeleteApplicationReferenceDataSource')
DeleteApplicationSnapshot = Action('DeleteApplicationSnapshot')
DeleteApplicationVpcConfiguration = \
    Action('DeleteApplicationVpcConfiguration')
DescribeApplication = Action('DescribeApplication')
DescribeApplicationSnapshot = Action('DescribeApplicationSnapshot')
DiscoverInputSchema = Action('DiscoverInputSchema')
GetApplicationState = Action('GetApplicationState')
ListApplicationSnapshots = Action('ListApplicationSnapshots')
ListApplications = Action('ListApplications')
ListTagsForResource = Action('ListTagsForResource')
StartApplication = Action('StartApplication')
StopApplication = Action('StopApplication')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
