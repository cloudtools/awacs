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


AddApplicationInput = Action('AddApplicationInput')
AddApplicationOutput = Action('AddApplicationOutput')
AddApplicationReferenceDataSource = \
    Action('AddApplicationReferenceDataSource')
CreateApplication = Action('CreateApplication')
DeleteApplication = Action('DeleteApplication')
DeleteApplicationOutput = Action('DeleteApplicationOutput')
DeleteApplicationReferenceDataSource = \
    Action('DeleteApplicationReferenceDataSource')
DescribeApplication = Action('DescribeApplication')
DiscoverInputSchema = Action('DiscoverInputSchema')
GetApplicationState = Action('GetApplicationState')
ListApplications = Action('ListApplications')
ListTagsForResource = Action('ListTagsForResource')
StartApplication = Action('StartApplication')
StopApplication = Action('StopApplication')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
AddApplicationCloudWatchLoggingOption = \
    Action('AddApplicationCloudWatchLoggingOption')
AddApplicationInputProcessingConfiguration = \
    Action('AddApplicationInputProcessingConfiguration')
CreateApplicationSnapshot = Action('CreateApplicationSnapshot')
DeleteApplicationCloudWatchLoggingOption = \
    Action('DeleteApplicationCloudWatchLoggingOption')
DeleteApplicationInputProcessingConfiguration = \
    Action('DeleteApplicationInputProcessingConfiguration')
DeleteApplicationSnapshot = Action('DeleteApplicationSnapshot')
DescribeApplicationSnapshot = Action('DescribeApplicationSnapshot')
GetApplicationState = Action('GetApplicationState')
ListApplicationSnapshots = Action('ListApplicationSnapshots')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
