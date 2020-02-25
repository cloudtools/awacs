# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS RoboMaker'
prefix = 'robomaker'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchDescribeSimulationJob = Action('BatchDescribeSimulationJob')
CancelDeploymentJob = Action('CancelDeploymentJob')
CancelSimulationJob = Action('CancelSimulationJob')
CancelSimulationJobBatch = Action('CancelSimulationJobBatch')
CreateDeploymentJob = Action('CreateDeploymentJob')
CreateFleet = Action('CreateFleet')
CreateRobot = Action('CreateRobot')
CreateRobotApplication = Action('CreateRobotApplication')
CreateRobotApplicationVersion = Action('CreateRobotApplicationVersion')
CreateSimulationApplication = Action('CreateSimulationApplication')
CreateSimulationApplicationVersion = \
    Action('CreateSimulationApplicationVersion')
CreateSimulationJob = Action('CreateSimulationJob')
DeleteFleet = Action('DeleteFleet')
DeleteRobot = Action('DeleteRobot')
DeleteRobotApplication = Action('DeleteRobotApplication')
DeleteSimulationApplication = Action('DeleteSimulationApplication')
DeregisterRobot = Action('DeregisterRobot')
DescribeDeploymentJob = Action('DescribeDeploymentJob')
DescribeFleet = Action('DescribeFleet')
DescribeRobot = Action('DescribeRobot')
DescribeRobotApplication = Action('DescribeRobotApplication')
DescribeSimulationApplication = Action('DescribeSimulationApplication')
DescribeSimulationJob = Action('DescribeSimulationJob')
DescribeSimulationJobBatch = Action('DescribeSimulationJobBatch')
ListDeploymentJobs = Action('ListDeploymentJobs')
ListFleets = Action('ListFleets')
ListRobotApplications = Action('ListRobotApplications')
ListRobots = Action('ListRobots')
ListSimulationApplications = Action('ListSimulationApplications')
ListSimulationJobBatches = Action('ListSimulationJobBatches')
ListSimulationJobs = Action('ListSimulationJobs')
ListTagsForResource = Action('ListTagsForResource')
RegisterRobot = Action('RegisterRobot')
RestartSimulationJob = Action('RestartSimulationJob')
StartSimulationJobBatch = Action('StartSimulationJobBatch')
SyncDeploymentJob = Action('SyncDeploymentJob')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateRobotApplication = Action('UpdateRobotApplication')
UpdateSimulationApplication = Action('UpdateSimulationApplication')
