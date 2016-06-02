# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon AppStream'
prefix = 'appstream'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApplication = Action('CreateApplication')
CreateSession = Action('CreateSession')
DeleteApplication = Action('DeleteApplication')
GetApiRoot = Action('GetApiRoot')
GetApplication = Action('GetApplication')
GetApplications = Action('GetApplications')
GetApplicationError = Action('GetApplicationError')
GetApplicationErrors = Action('GetApplicationErrors')
GetApplicationStatus = Action('GetApplicationStatus')
GetSession = Action('GetSession')
GetSessions = Action('GetSessions')
GetSessionStatus = Action('GetSessionStatus')
UpdateApplication = Action('UpdateApplication')
UpdateApplicationState = Action('UpdateApplicationState')
UpdateSessionState = Action('UpdateSessionState')
