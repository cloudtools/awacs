# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudSearch'
prefix = 'cloudsearch'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BuildSuggesters = Action('BuildSuggesters')
CreateDomain = Action('CreateDomain')
DefineAnalysisScheme = Action('DefineAnalysisScheme')
DefineExpression = Action('DefineExpression')
DefineIndexField = Action('DefineIndexField')
DefineIndexFields = Action('DefineIndexFields')
DefineSuggester = Action('DefineSuggester')
DeleteAnalysisScheme = Action('DeleteAnalysisScheme')
DeleteDomain = Action('DeleteDomain')
DeleteExpression = Action('DeleteExpression')
DeleteIndexField = Action('DeleteIndexField')
DeleteSuggester = Action('DeleteSuggester')
DescribeAnalysisSchemes = Action('DescribeAnalysisSchemes')
DescribeAvailabilityOptions = Action('DescribeAvailabilityOptions')
DescribeDomains = Action('DescribeDomains')
DescribeExpressions = Action('DescribeExpressions')
DescribeIndexFields = Action('DescribeIndexFields')
DescribeScalingParameters = Action('DescribeScalingParameters')
DescribeServiceAccessPolicies = Action('DescribeServiceAccessPolicies')
DescribeSuggesters = Action('DescribeSuggesters')
document = Action('document')
IndexDocuments = Action('IndexDocuments')
ListDomainNames = Action('ListDomainNames')
search = Action('search')
suggest = Action('suggest')
UpdateAvailabilityOptions = Action('UpdateAvailabilityOptions')
UpdateScalingParameters = Action('UpdateScalingParameters')
UpdateServiceAccessPolicies = Action('UpdateServiceAccessPolicies')
