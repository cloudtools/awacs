# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon AppStream'
prefix = 'appstream'

CreateApplication = Action(prefix, 'CreateApplication')
CreateSession = Action(prefix, 'CreateSession')
DeleteApplication = Action(prefix, 'DeleteApplication')
GetApiRoot = Action(prefix, 'GetApiRoot')
GetApplication = Action(prefix, 'GetApplication')
GetApplications = Action(prefix, 'GetApplications')
GetApplicationError = Action(prefix, 'GetApplicationError')
GetApplicationErrors = Action(prefix, 'GetApplicationErrors')
GetApplicationStatus = Action(prefix, 'GetApplicationStatus')
GetSession = Action(prefix, 'GetSession')
GetSessions = Action(prefix, 'GetSessions')
GetSessionStatus = Action(prefix, 'GetSessionStatus')
UpdateApplication = Action(prefix, 'UpdateApplication')
UpdateApplicationState = Action(prefix, 'UpdateApplicationState')
UpdateSessionState = Action(prefix, 'UpdateSessionState')
