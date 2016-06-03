# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Inspector'
prefix = 'inspector'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddAttributesToFindings = Action('AddAttributesToFindings')
AttachAssessmentAndRulesPackage = \
    Action('AttachAssessmentAndRulesPackage')
CreateApplication = Action('CreateApplication')
CreateAssessment = Action('CreateAssessment')
CreateResourceGroup = Action('CreateResourceGroup')
DeleteApplication = Action('DeleteApplication')
DeleteAssessment = Action('DeleteAssessment')
DeleteRun = Action('DeleteRun')
DescribeApplication = Action('DescribeApplication')
DescribeAssessment = Action('DescribeAssessment')
DescribeCrossAccountAccessRole = Action('DescribeCrossAccountAccessRole')
DescribeFinding = Action('DescribeFinding')
DescribeResourceGroup = Action('DescribeResourceGroup')
DescribeRulesPackage = Action('DescribeRulesPackage')
DescribeRun = Action('DescribeRun')
DetachAssessmentAndRulesPackage = \
    Action('DetachAssessmentAndRulesPackage')
GetAssessmentTelemetry = Action('GetAssessmentTelemetry')
ListApplications = Action('ListApplications')
ListAssessmentAgents = Action('ListAssessmentAgents')
ListAssessments = Action('ListAssessments')
ListAttachedAssessments = Action('ListAttachedAssessments')
ListAttachedRulesPackages = Action('ListAttachedRulesPackages')
ListFindings = Action('ListFindings')
ListRulesPackages = Action('ListRulesPackages')
ListRuns = Action('ListRuns')
ListTagsForResource = Action('ListTagsForResource')
LocalizeText = Action('LocalizeText')
PreviewAgentsForResourceGroup = Action('PreviewAgentsForResourceGroup')
RegisterCrossAccountAccessRole = Action('RegisterCrossAccountAccessRole')
RemoveAttributesFromFindings = Action('RemoveAttributesFromFindings')
RetireRulesPackage = Action('RetireRulesPackage')
RunAssessment = Action('RunAssessment')
SetTagsForResource = Action('SetTagsForResource')
StartDataCollection = Action('StartDataCollection')
StopDataCollection = Action('StopDataCollection')
UpdateApplication = Action('UpdateApplication')
UpdateAssessment = Action('UpdateAssessment')
