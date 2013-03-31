# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon DynamoDB'
prefix = 'dynamodb'

BatchGetItem = Action(prefix, 'BatchGetItem')
CreateTable = Action(prefix, 'CreateTable')
DeleteItem = Action(prefix, 'DeleteItem')
DeleteTable = Action(prefix, 'DeleteTable')
DescribeTable = Action(prefix, 'DescribeTable')
GetItem = Action(prefix, 'GetItem')
ListTables = Action(prefix, 'ListTables')
PutItem = Action(prefix, 'PutItem')
Query = Action(prefix, 'Query')
Scan = Action(prefix, 'Scan')
UpdateItem = Action(prefix, 'UpdateItem')
UpdateTable = Action(prefix, 'UpdateTable')
