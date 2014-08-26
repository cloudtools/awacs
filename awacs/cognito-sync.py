# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Cognito Sync'
prefix = 'cognito-sync'

DeleteDataset = Action(prefix, 'DeleteDataset')
DescribeDataset = Action(prefix, 'DescribeDataset')
DescribeIdentityUsage = Action(prefix, 'DescribeIdentityUsage')
DescribeIdentityPoolUsage = Action(prefix, 'DescribeIdentityPoolUsage')
ListDatasets = Action(prefix, 'ListDatasets')
ListIdentityPoolUsage = Action(prefix, 'ListIdentityPoolUsage')
ListRecords = Action(prefix, 'ListRecords')
UpdateRecords = Action(prefix, 'UpdateRecords')
