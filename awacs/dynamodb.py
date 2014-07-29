# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action
from aws import BaseARN

service_name = 'Amazon DynamoDB'
prefix = 'dynamodb'


class ARN(BaseARN):
    def __init__(self, region, account, table=None, index=None):
        sup = super(ARN, self)
        resource = '*'
        if table:
            resource = 'table/' + table
            if index:
                resource += '/index/' + index
        sup.__init__(prefix, region=region, account=account, resource=resource)


BatchGetItem = Action(prefix, 'BatchGetItem')
BatchWriteItem = Action(prefix, 'BatchWriteItem')
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
