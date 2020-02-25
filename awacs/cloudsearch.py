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


AddTags = Action('AddTags')
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
DescribeDomainEndpointOptions = Action('DescribeDomainEndpointOptions')
DescribeDomains = Action('DescribeDomains')
DescribeExpressions = Action('DescribeExpressions')
DescribeIndexFields = Action('DescribeIndexFields')
DescribeScalingParameters = Action('DescribeScalingParameters')
DescribeServiceAccessPolicies = Action('DescribeServiceAccessPolicies')
DescribeSuggesters = Action('DescribeSuggesters')
IndexDocuments = Action('IndexDocuments')
ListDomainNames = Action('ListDomainNames')
ListTags = Action('ListTags')
RemoveTags = Action('RemoveTags')
UpdateAvailabilityOptions = Action('UpdateAvailabilityOptions')
UpdateDomainEndpointOptions = Action('UpdateDomainEndpointOptions')
UpdateScalingParameters = Action('UpdateScalingParameters')
UpdateServiceAccessPolicies = Action('UpdateServiceAccessPolicies')
document = Action('document')
search = Action('search')
suggest = Action('suggest')
