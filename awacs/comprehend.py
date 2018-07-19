# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Comprehend'
prefix = 'comprehend'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchDetectDominantLanguage = Action('BatchDetectDominantLanguage')
BatchDetectEntities = Action('BatchDetectEntities')
BatchDetectKeyPhrases = Action('BatchDetectKeyPhrases')
BatchDetectSentiment = Action('BatchDetectSentiment')
DescribeTopicsDetectionJob = Action('DescribeTopicsDetectionJob')
DetectDominantLanguage = Action('DetectDominantLanguage')
DetectEntities = Action('DetectEntities')
DetectKeyPhrases = Action('DetectKeyPhrases')
DetectSentiment = Action('DetectSentiment')
ListTopicsDetectionJobs = Action('ListTopicsDetectionJobs')
StartTopicsDetectionJob = Action('StartTopicsDetectionJob')
