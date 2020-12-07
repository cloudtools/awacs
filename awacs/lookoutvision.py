# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Lookout for Vision'
prefix = 'lookoutvision'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateDataset = Action('CreateDataset')
CreateModel = Action('CreateModel')
CreateProject = Action('CreateProject')
DeleteDataset = Action('DeleteDataset')
DeleteModel = Action('DeleteModel')
DeleteProject = Action('DeleteProject')
DescribeDataset = Action('DescribeDataset')
DescribeModel = Action('DescribeModel')
DescribeProject = Action('DescribeProject')
DescribeTrialDetection = Action('DescribeTrialDetection')
DetectAnomalies = Action('DetectAnomalies')
ListDatasetEntries = Action('ListDatasetEntries')
ListModels = Action('ListModels')
ListProjects = Action('ListProjects')
ListTrialDetections = Action('ListTrialDetections')
StartModel = Action('StartModel')
StartTrialDetection = Action('StartTrialDetection')
StopModel = Action('StopModel')
UpdateDatasetEntries = Action('UpdateDatasetEntries')
