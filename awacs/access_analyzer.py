# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'IAM Access Analyzer'
prefix = 'access-analyzer'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateAnalyzer = Action('CreateAnalyzer')
CreateArchiveRule = Action('CreateArchiveRule')
DeleteAnalyzer = Action('DeleteAnalyzer')
DeleteArchiveRule = Action('DeleteArchiveRule')
GetAnalyzedResource = Action('GetAnalyzedResource')
GetAnalyzer = Action('GetAnalyzer')
GetArchiveRule = Action('GetArchiveRule')
GetFinding = Action('GetFinding')
ListAnalyzedResources = Action('ListAnalyzedResources')
ListAnalyzers = Action('ListAnalyzers')
ListArchiveRules = Action('ListArchiveRules')
ListFindings = Action('ListFindings')
ListTagsForResource = Action('ListTagsForResource')
StartResourceScan = Action('StartResourceScan')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateArchiveRule = Action('UpdateArchiveRule')
UpdateFindings = Action('UpdateFindings')
