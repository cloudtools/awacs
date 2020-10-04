# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Keyspaces (for Apache Cassandra)'
prefix = 'cassandra'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


Alter = Action('Alter')
Create = Action('Create')
Drop = Action('Drop')
Modify = Action('Modify')
Restore = Action('Restore')
Select = Action('Select')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
