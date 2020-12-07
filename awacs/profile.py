# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Connect Customer Profiles'
prefix = 'profile'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddProfileKey = Action('AddProfileKey')
CreateDomain = Action('CreateDomain')
CreateProfile = Action('CreateProfile')
DeleteDomain = Action('DeleteDomain')
DeleteIntegration = Action('DeleteIntegration')
DeleteProfile = Action('DeleteProfile')
DeleteProfileKey = Action('DeleteProfileKey')
DeleteProfileObject = Action('DeleteProfileObject')
DeleteProfileObjectType = Action('DeleteProfileObjectType')
GetDomain = Action('GetDomain')
GetIntegration = Action('GetIntegration')
GetProfileObjectType = Action('GetProfileObjectType')
GetProfileObjectTypeTemplate = Action('GetProfileObjectTypeTemplate')
ListAccountIntegrations = Action('ListAccountIntegrations')
ListDomains = Action('ListDomains')
ListIntegrations = Action('ListIntegrations')
ListProfileObjectTypeTemplates = Action('ListProfileObjectTypeTemplates')
ListProfileObjectTypes = Action('ListProfileObjectTypes')
ListProfileObjects = Action('ListProfileObjects')
ListTagsForResource = Action('ListTagsForResource')
PutIntegration = Action('PutIntegration')
PutProfileObject = Action('PutProfileObject')
PutProfileObjectType = Action('PutProfileObjectType')
SearchProfiles = Action('SearchProfiles')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDomain = Action('UpdateDomain')
UpdateProfile = Action('UpdateProfile')
