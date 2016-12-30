# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Rekognition'
prefix = 'rekognition'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CompareFaces = Action('CompareFaces')
CreateCollection = Action('CreateCollection')
DeleteCollection = Action('DeleteCollection')
DeleteFaces = Action('DeleteFaces')
DetectFaces = Action('DetectFaces')
DetectLabels = Action('DetectLabels')
IndexFaces = Action('IndexFaces')
ListCollections = Action('ListCollections')
ListFaces = Action('ListFaces')
SearchFaces = Action('SearchFaces')
SearchFacesByImage = Action('SearchFacesByImage')
