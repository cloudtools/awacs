# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Lambda'
prefix = 'lambda'

AddPermission = Action(prefix, 'AddPermission')
CreateAlias = Action(prefix, 'CreateAlias')
CreateEventSourceMapping = Action(prefix, 'CreateEventSourceMapping')
CreateFunction = Action(prefix, 'CreateFunction')
DeleteAlias = Action(prefix, 'DeleteAlias')
DeleteEventSourceMapping = Action(prefix, 'DeleteEventSourceMapping')
DeleteFunction = Action(prefix, 'DeleteFunction')
GetAlias = Action(prefix, 'GetAlias')
GetEventSourceMapping = Action(prefix, 'GetEventSourceMapping')
GetFunction = Action(prefix, 'GetFunction')
GetFunctionConfiguration = Action(prefix, 'GetFunctionConfiguration')
GetPolicy = Action(prefix, 'GetPolicy')
InvokeAsync = Action(prefix, 'InvokeAsync')
InvokeFunction = Action(prefix, 'InvokeFunction')
ListAliases = Action(prefix, 'ListAliases')
ListEventSourceMappings = Action(prefix, 'ListEventSourceMappings')
ListFunctions = Action(prefix, 'ListFunctions')
ListVersionsByFunction = Action(prefix, 'ListVersionsByFunction')
PublishVersion = Action(prefix, 'PublishVersion')
RemovePermission = Action(prefix, 'RemovePermission')
UpdateAlias = Action(prefix, 'UpdateAlias')
UpdateEventSourceMapping = Action(prefix, 'UpdateEventSourceMapping')
UpdateFunctionCode = Action(prefix, 'UpdateFunctionCode')
UpdateFunctionConfiguration = \
    Action(prefix, 'UpdateFunctionConfiguration')
