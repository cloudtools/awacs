# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Support'
prefix = 'support'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddAttachmentsToSet = Action('AddAttachmentsToSet')
AddCommunicationToCase = Action('AddCommunicationToCase')
CreateCase = Action('CreateCase')
DescribeAttachment = Action('DescribeAttachment')
DescribeCaseAttributes = Action('DescribeCaseAttributes')
DescribeCases = Action('DescribeCases')
DescribeCommunications = Action('DescribeCommunications')
DescribeIssueTypes = Action('DescribeIssueTypes')
DescribeServices = Action('DescribeServices')
DescribeSeverityLevels = Action('DescribeSeverityLevels')
DescribeSupportLevel = Action('DescribeSupportLevel')
DescribeTrustedAdvisorCheckRefreshStatuses = \
    Action('DescribeTrustedAdvisorCheckRefreshStatuses')
DescribeTrustedAdvisorCheckResult = \
    Action('DescribeTrustedAdvisorCheckResult')
DescribeTrustedAdvisorCheckSummaries = \
    Action('DescribeTrustedAdvisorCheckSummaries')
DescribeTrustedAdvisorChecks = Action('DescribeTrustedAdvisorChecks')
InitiateCallForCase = Action('InitiateCallForCase')
InitiateChatForCase = Action('InitiateChatForCase')
PutCaseAttributes = Action('PutCaseAttributes')
RateCaseCommunication = Action('RateCaseCommunication')
RefreshTrustedAdvisorCheck = Action('RefreshTrustedAdvisorCheck')
ResolveCase = Action('ResolveCase')
SearchForCases = Action('SearchForCases')
