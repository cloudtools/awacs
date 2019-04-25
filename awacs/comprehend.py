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
BatchDetectSyntax = Action('BatchDetectSyntax')
CreateDocumentClassifier = Action('CreateDocumentClassifier')
CreateEntityRecognizer = Action('CreateEntityRecognizer')
DeleteDocumentClassifier = Action('DeleteDocumentClassifier')
DeleteEntityRecognizer = Action('DeleteEntityRecognizer')
DescribeDocumentClassificationJob = \
    Action('DescribeDocumentClassificationJob')
DescribeDocumentClassifier = Action('DescribeDocumentClassifier')
DescribeDominantLanguageDetectionJob = \
    Action('DescribeDominantLanguageDetectionJob')
DescribeEntitiesDetectionJob = Action('DescribeEntitiesDetectionJob')
DescribeEntityRecognizer = Action('DescribeEntityRecognizer')
DescribeKeyPhrasesDetectionJob = Action('DescribeKeyPhrasesDetectionJob')
DescribeSentimentDetectionJob = Action('DescribeSentimentDetectionJob')
DescribeTopicsDetectionJob = Action('DescribeTopicsDetectionJob')
DetectDominantLanguage = Action('DetectDominantLanguage')
DetectEntities = Action('DetectEntities')
DetectKeyPhrases = Action('DetectKeyPhrases')
DetectSentiment = Action('DetectSentiment')
DetectSyntax = Action('DetectSyntax')
ListDocumentClassificationJobs = Action('ListDocumentClassificationJobs')
ListDocumentClassifiers = Action('ListDocumentClassifiers')
ListDominantLanguageDetectionJobs = \
    Action('ListDominantLanguageDetectionJobs')
ListEntitiesDetectionJobs = Action('ListEntitiesDetectionJobs')
ListEntityRecognizers = Action('ListEntityRecognizers')
ListKeyPhrasesDetectionJobs = Action('ListKeyPhrasesDetectionJobs')
ListSentimentDetectionJobs = Action('ListSentimentDetectionJobs')
ListTagsForResource = Action('ListTagsForResource')
ListTopicsDetectionJobs = Action('ListTopicsDetectionJobs')
StartDocumentClassificationJob = Action('StartDocumentClassificationJob')
StartDominantLanguageDetectionJob = \
    Action('StartDominantLanguageDetectionJob')
StartEntitiesDetectionJob = Action('StartEntitiesDetectionJob')
StartKeyPhrasesDetectionJob = Action('StartKeyPhrasesDetectionJob')
StartSentimentDetectionJob = Action('StartSentimentDetectionJob')
StartTopicsDetectionJob = Action('StartTopicsDetectionJob')
StopDominantLanguageDetectionJob = \
    Action('StopDominantLanguageDetectionJob')
StopEntitiesDetectionJob = Action('StopEntitiesDetectionJob')
StopKeyPhrasesDetectionJob = Action('StopKeyPhrasesDetectionJob')
StopSentimentDetectionJob = Action('StopSentimentDetectionJob')
StopTrainingDocumentClassifier = Action('StopTrainingDocumentClassifier')
StopTrainingEntityRecognizer = Action('StopTrainingEntityRecognizer')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
