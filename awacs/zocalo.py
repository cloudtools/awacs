# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Zocalo'
prefix = 'zocalo'

ActivateUser = Action(prefix, 'ActivateUser')
AddUserToGroup = Action(prefix, 'AddUserToGroup')
CheckAlias = Action(prefix, 'CheckAlias')
CreateInstance = Action(prefix, 'CreateInstance')
DeactivateUser = Action(prefix, 'DeactivateUser')
DeleteInstance = Action(prefix, 'DeleteInstance')
DeregisterDirectory = Action(prefix, 'DeregisterDirectory')
DescribeAvailableDirectories = \
    Action(prefix, 'DescribeAvailableDirectories')
DescribeInstances = Action(prefix, 'DescribeInstances')
RegisterDirectory = Action(prefix, 'RegisterDirectory')
RemoveUserFromGroup = Action(prefix, 'RemoveUserFromGroup')
UpdateInstanceAlias = Action(prefix, 'UpdateInstanceAlias')
