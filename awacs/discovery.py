# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Application Discovery Service'
prefix = 'discovery'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateTags = Action('CreateTags')
DeleteTags = Action('DeleteTags')
DescribeAgents = Action('DescribeAgents')
DescribeConfigurations = Action('DescribeConfigurations')
DescribeExportConfigurations = Action('DescribeExportConfigurations')
DescribeTags = Action('DescribeTags')
ExportConfigurations = Action('ExportConfigurations')
ListConfigurations = Action('ListConfigurations')
StartDataCollectionByAgentIds = Action('StartDataCollectionByAgentIds')
StopDataCollectionByAgentIds = Action('StopDataCollectionByAgentIds')
