# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon MQ'
prefix = 'mq'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateBroker = Action('CreateBroker')
CreateConfiguration = Action('CreateConfiguration')
CreateTags = Action('CreateTags')
CreateUser = Action('CreateUser')
DeleteBroker = Action('DeleteBroker')
DeleteTags = Action('DeleteTags')
DeleteUser = Action('DeleteUser')
DescribeBroker = Action('DescribeBroker')
DescribeConfiguration = Action('DescribeConfiguration')
DescribeConfigurationRevision = Action('DescribeConfigurationRevision')
DescribeUser = Action('DescribeUser')
ListBrokers = Action('ListBrokers')
ListConfigurationRevisions = Action('ListConfigurationRevisions')
ListConfigurations = Action('ListConfigurations')
ListTags = Action('ListTags')
ListUsers = Action('ListUsers')
RebootBroker = Action('RebootBroker')
UpdateBroker = Action('UpdateBroker')
UpdateConfiguration = Action('UpdateConfiguration')
UpdateUser = Action('UpdateUser')
