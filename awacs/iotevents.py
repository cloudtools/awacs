# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT Events'
prefix = 'iotevents'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchPutMessage = Action('BatchPutMessage')
BatchUpdateDetector = Action('BatchUpdateDetector')
CreateDetectorModel = Action('CreateDetectorModel')
CreateInput = Action('CreateInput')
DeleteDetectorModel = Action('DeleteDetectorModel')
DeleteInput = Action('DeleteInput')
DescribeDetector = Action('DescribeDetector')
DescribeDetectorModel = Action('DescribeDetectorModel')
DescribeInput = Action('DescribeInput')
DescribeLoggingOptions = Action('DescribeLoggingOptions')
ListDetectorModelVersions = Action('ListDetectorModelVersions')
ListDetectorModels = Action('ListDetectorModels')
ListDetectors = Action('ListDetectors')
ListInputs = Action('ListInputs')
ListTagsForResource = Action('ListTagsForResource')
PutLoggingOptions = Action('PutLoggingOptions')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDetectorModel = Action('UpdateDetectorModel')
UpdateInput = Action('UpdateInput')
UpdateInputRouting = Action('UpdateInputRouting')
