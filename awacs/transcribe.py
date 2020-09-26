# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Transcribe'
prefix = 'transcribe'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateLanguageModel = Action('CreateLanguageModel')
CreateMedicalVocabulary = Action('CreateMedicalVocabulary')
CreateVocabulary = Action('CreateVocabulary')
CreateVocabularyFilter = Action('CreateVocabularyFilter')
DeleteLanguageModel = Action('DeleteLanguageModel')
DeleteMedicalTranscriptionJob = Action('DeleteMedicalTranscriptionJob')
DeleteMedicalVocabulary = Action('DeleteMedicalVocabulary')
DeleteTranscriptionJob = Action('DeleteTranscriptionJob')
DeleteVocabulary = Action('DeleteVocabulary')
DeleteVocabularyFilter = Action('DeleteVocabularyFilter')
DescribeLanguageModel = Action('DescribeLanguageModel')
GetMedicalTranscriptionJob = Action('GetMedicalTranscriptionJob')
GetMedicalVocabulary = Action('GetMedicalVocabulary')
GetTranscriptionJob = Action('GetTranscriptionJob')
GetVocabulary = Action('GetVocabulary')
GetVocabularyFilter = Action('GetVocabularyFilter')
ListLanguageModels = Action('ListLanguageModels')
ListMedicalTranscriptionJobs = Action('ListMedicalTranscriptionJobs')
ListMedicalVocabularies = Action('ListMedicalVocabularies')
ListTranscriptionJobs = Action('ListTranscriptionJobs')
ListVocabularies = Action('ListVocabularies')
ListVocabularyFilters = Action('ListVocabularyFilters')
StartMedicalStreamTranscription = \
    Action('StartMedicalStreamTranscription')
StartMedicalStreamTranscriptionWebSocket = \
    Action('StartMedicalStreamTranscriptionWebSocket')
StartMedicalTranscriptionJob = Action('StartMedicalTranscriptionJob')
StartStreamTranscription = Action('StartStreamTranscription')
StartStreamTranscriptionWebSocket = \
    Action('StartStreamTranscriptionWebSocket')
StartTranscriptionJob = Action('StartTranscriptionJob')
UpdateMedicalVocabulary = Action('UpdateMedicalVocabulary')
UpdateVocabulary = Action('UpdateVocabulary')
UpdateVocabularyFilter = Action('UpdateVocabularyFilter')
