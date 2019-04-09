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


CreateVocabulary = Action('CreateVocabulary')
DeleteTranscriptionJob = Action('DeleteTranscriptionJob')
DeleteVocabulary = Action('DeleteVocabulary')
GetTranscriptionJob = Action('GetTranscriptionJob')
GetVocabulary = Action('GetVocabulary')
ListTranscriptionJobs = Action('ListTranscriptionJobs')
ListVocabularies = Action('ListVocabularies')
StartStreamTranscription = Action('StartStreamTranscription')
StartTranscriptionJob = Action('StartTranscriptionJob')
UpdateVocabulary = Action('UpdateVocabulary')
