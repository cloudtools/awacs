# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon CloudSearch'
prefix = 'cloudsearch'

BuildSuggesters = Action(prefix, 'BuildSuggesters')
CreateDomain = Action(prefix, 'CreateDomain')
DefineAnalysisScheme = Action(prefix, 'DefineAnalysisScheme')
DefineExpression = Action(prefix, 'DefineExpression')
DefineIndexField = Action(prefix, 'DefineIndexField')
DefineSuggester = Action(prefix, 'DefineSuggester')
DeleteAnalysisScheme = Action(prefix, 'DeleteAnalysisScheme')
DeleteDomain = Action(prefix, 'DeleteDomain')
DeleteExpression = Action(prefix, 'DeleteExpression')
DeleteIndexField = Action(prefix, 'DeleteIndexField')
DeleteSuggester = Action(prefix, 'DeleteSuggester')
DescribeAnalysisSchemes = Action(prefix, 'DescribeAnalysisSchemes')
DescribeAvailabilityOptions = \
    Action(prefix, 'DescribeAvailabilityOptions')
DescribeDomains = Action(prefix, 'DescribeDomains')
DescribeExpressions = Action(prefix, 'DescribeExpressions')
DescribeIndexFields = Action(prefix, 'DescribeIndexFields')
DescribeScalingParameters = Action(prefix, 'DescribeScalingParameters')
DescribeServiceAccessPolicies = \
    Action(prefix, 'DescribeServiceAccessPolicies')
DescribeSuggesters = Action(prefix, 'DescribeSuggesters')
IndexDocuments = Action(prefix, 'IndexDocuments')
ListDomainNames = Action(prefix, 'ListDomainNames')
UpdateAvailabilityOptions = Action(prefix, 'UpdateAvailabilityOptions')
UpdateScalingParameters = Action(prefix, 'UpdateScalingParameters')
UpdateServiceAccessPolicies = \
    Action(prefix, 'UpdateServiceAccessPolicies')
