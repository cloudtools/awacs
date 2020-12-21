# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Managed Service for Prometheus'
prefix = 'aps'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateWorkspace = Action('CreateWorkspace')
DeleteWorkspace = Action('DeleteWorkspace')
DescribeWorkspace = Action('DescribeWorkspace')
GetLabels = Action('GetLabels')
GetMetricMetadata = Action('GetMetricMetadata')
GetSeries = Action('GetSeries')
ListWorkspaces = Action('ListWorkspaces')
QueryMetrics = Action('QueryMetrics')
RemoteWrite = Action('RemoteWrite')
UpdateWorkspaceAlias = Action('UpdateWorkspaceAlias')
