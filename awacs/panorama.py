# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Panorama'
prefix = 'panorama'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApp = Action('CreateApp')
CreateAppDeployment = Action('CreateAppDeployment')
CreateAppVersion = Action('CreateAppVersion')
CreateDataSource = Action('CreateDataSource')
CreateDeploymentConfiguration = Action('CreateDeploymentConfiguration')
CreateDevice = Action('CreateDevice')
CreateDeviceUpdate = Action('CreateDeviceUpdate')
CreateInputs = Action('CreateInputs')
CreateModel = Action('CreateModel')
CreateStreams = Action('CreateStreams')
DeleteApp = Action('DeleteApp')
DeleteAppVersion = Action('DeleteAppVersion')
DeleteDataSource = Action('DeleteDataSource')
DeleteDevice = Action('DeleteDevice')
DeleteModel = Action('DeleteModel')
DescribeApp = Action('DescribeApp')
DescribeAppDeployment = Action('DescribeAppDeployment')
DescribeAppVersion = Action('DescribeAppVersion')
DescribeDataSource = Action('DescribeDataSource')
DescribeDevice = Action('DescribeDevice')
DescribeDeviceUpdate = Action('DescribeDeviceUpdate')
DescribeModel = Action('DescribeModel')
DescribeSoftware = Action('DescribeSoftware')
GetDeploymentConfiguration = Action('GetDeploymentConfiguration')
GetInputs = Action('GetInputs')
GetStreams = Action('GetStreams')
GetWebSocketURL = Action('GetWebSocketURL')
ListAppDeploymentOperations = Action('ListAppDeploymentOperations')
ListAppVersions = Action('ListAppVersions')
ListApps = Action('ListApps')
ListDataSources = Action('ListDataSources')
ListDeploymentConfigurations = Action('ListDeploymentConfigurations')
ListDeviceUpdates = Action('ListDeviceUpdates')
ListDevices = Action('ListDevices')
ListModels = Action('ListModels')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateApp = Action('UpdateApp')
UpdateAppConfiguration = Action('UpdateAppConfiguration')
UpdateDataSource = Action('UpdateDataSource')
UpdateDevice = Action('UpdateDevice')
