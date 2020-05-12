# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Elemental MediaStore'
prefix = 'mediastore'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateContainer = Action('CreateContainer')
DeleteContainer = Action('DeleteContainer')
DeleteContainerPolicy = Action('DeleteContainerPolicy')
DeleteCorsPolicy = Action('DeleteCorsPolicy')
DeleteLifecyclePolicy = Action('DeleteLifecyclePolicy')
DeleteMetricPolicy = Action('DeleteMetricPolicy')
DeleteObject = Action('DeleteObject')
DescribeContainer = Action('DescribeContainer')
DescribeObject = Action('DescribeObject')
GetContainerPolicy = Action('GetContainerPolicy')
GetCorsPolicy = Action('GetCorsPolicy')
GetLifecyclePolicy = Action('GetLifecyclePolicy')
GetMetricPolicy = Action('GetMetricPolicy')
GetObject = Action('GetObject')
ListContainers = Action('ListContainers')
ListItems = Action('ListItems')
ListTagsForResource = Action('ListTagsForResource')
PutContainerPolicy = Action('PutContainerPolicy')
PutCorsPolicy = Action('PutCorsPolicy')
PutLifecyclePolicy = Action('PutLifecyclePolicy')
PutMetricPolicy = Action('PutMetricPolicy')
PutObject = Action('PutObject')
StartAccessLogging = Action('StartAccessLogging')
StopAccessLogging = Action('StopAccessLogging')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
