# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS OpsWorks Configuration Management'
prefix = 'opsworks-cm'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateNode = Action('AssociateNode')
CreateBackup = Action('CreateBackup')
CreateServer = Action('CreateServer')
DeleteBackup = Action('DeleteBackup')
DeleteServer = Action('DeleteServer')
DescribeAccountAttributes = Action('DescribeAccountAttributes')
DescribeBackups = Action('DescribeBackups')
DescribeEvents = Action('DescribeEvents')
DescribeNodeAssociationStatus = Action('DescribeNodeAssociationStatus')
DescribeServers = Action('DescribeServers')
DisassociateNode = Action('DisassociateNode')
RestoreServer = Action('RestoreServer')
StartMaintenance = Action('StartMaintenance')
UpdateServer = Action('UpdateServer')
UpdateServerEngineAttributes = Action('UpdateServerEngineAttributes')
