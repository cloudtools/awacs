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
ClassifyDocument = Action('ClassifyDocument')
CreateDocumentClassifier = Action('CreateDocumentClassifier')
CreateEndpoint = Action('CreateEndpoint')
CreateEntityRecognizer = Action('CreateEntityRecognizer')
DeleteDocumentClassifier = Action('DeleteDocumentClassifier')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteEntityRecognizer = Action('DeleteEntityRecognizer')
DescribeDocumentClassificationJob = \
    Action('DescribeDocumentClassificationJob')
DescribeDocumentClassifier = Action('DescribeDocumentClassifier')
DescribeDominantLanguageDetectionJob = \
    Action('DescribeDominantLanguageDetectionJob')
DescribeEndpoint = Action('DescribeEndpoint')
DescribeEntitiesDetectionJob = Action('DescribeEntitiesDetectionJob')
DescribeEntityRecognizer = Action('DescribeEntityRecognizer')
DescribeKeyPhrasesDetectionJob = Action('DescribeKeyPhrasesDetectionJob')
DescribePiiEntitiesDetectionJob = \
    Action('DescribePiiEntitiesDetectionJob')
DescribeSentimentDetectionJob = Action('DescribeSentimentDetectionJob')
DescribeTopicsDetectionJob = Action('DescribeTopicsDetectionJob')
DetectDominantLanguage = Action('DetectDominantLanguage')
DetectEntities = Action('DetectEntities')
DetectKeyPhrases = Action('DetectKeyPhrases')
DetectPiiEntities = Action('DetectPiiEntities')
DetectSentiment = Action('DetectSentiment')
DetectSyntax = Action('DetectSyntax')
ListDocumentClassificationJobs = Action('ListDocumentClassificationJobs')
ListDocumentClassifiers = Action('ListDocumentClassifiers')
ListDominantLanguageDetectionJobs = \
    Action('ListDominantLanguageDetectionJobs')
ListEndpoints = Action('ListEndpoints')
ListEntitiesDetectionJobs = Action('ListEntitiesDetectionJobs')
ListEntityRecognizers = Action('ListEntityRecognizers')
ListKeyPhrasesDetectionJobs = Action('ListKeyPhrasesDetectionJobs')
ListPiiEntitiesDetectionJobs = Action('ListPiiEntitiesDetectionJobs')
ListSentimentDetectionJobs = Action('ListSentimentDetectionJobs')
ListTagsForResource = Action('ListTagsForResource')
ListTopicsDetectionJobs = Action('ListTopicsDetectionJobs')
StartDocumentClassificationJob = Action('StartDocumentClassificationJob')
StartDominantLanguageDetectionJob = \
    Action('StartDominantLanguageDetectionJob')
StartEntitiesDetectionJob = Action('StartEntitiesDetectionJob')
StartKeyPhrasesDetectionJob = Action('StartKeyPhrasesDetectionJob')
StartPiiEntitiesDetectionJob = Action('StartPiiEntitiesDetectionJob')
StartSentimentDetectionJob = Action('StartSentimentDetectionJob')
StartTopicsDetectionJob = Action('StartTopicsDetectionJob')
StopDominantLanguageDetectionJob = \
    Action('StopDominantLanguageDetectionJob')
StopEntitiesDetectionJob = Action('StopEntitiesDetectionJob')
StopKeyPhrasesDetectionJob = Action('StopKeyPhrasesDetectionJob')
StopPiiEntitiesDetectionJob = Action('StopPiiEntitiesDetectionJob')
StopSentimentDetectionJob = Action('StopSentimentDetectionJob')
StopTrainingDocumentClassifier = Action('StopTrainingDocumentClassifier')
StopTrainingEntityRecognizer = Action('StopTrainingEntityRecognizer')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateEndpoint = Action('UpdateEndpoint')
