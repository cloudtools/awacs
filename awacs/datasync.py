# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'DataSync'
prefix = 'datasync'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelTaskExecution = Action('CancelTaskExecution')
CreateAgent = Action('CreateAgent')
CreateLocationEfs = Action('CreateLocationEfs')
CreateLocationNfs = Action('CreateLocationNfs')
CreateLocationS3 = Action('CreateLocationS3')
CreateTask = Action('CreateTask')
DeleteAgent = Action('DeleteAgent')
DeleteLocation = Action('DeleteLocation')
DeleteTask = Action('DeleteTask')
DescribeAgent = Action('DescribeAgent')
DescribeLocationEfs = Action('DescribeLocationEfs')
DescribeLocationNfs = Action('DescribeLocationNfs')
DescribeLocationS3 = Action('DescribeLocationS3')
DescribeTask = Action('DescribeTask')
DescribeTaskExecution = Action('DescribeTaskExecution')
ListAgents = Action('ListAgents')
ListLocations = Action('ListLocations')
ListTagsForResource = Action('ListTagsForResource')
ListTaskExecutions = Action('ListTaskExecutions')
ListTasks = Action('ListTasks')
StartTaskExecution = Action('StartTaskExecution')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAgent = Action('UpdateAgent')
UpdateTask = Action('UpdateTask')
