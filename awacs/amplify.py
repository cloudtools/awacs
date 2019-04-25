# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Amplify'
prefix = 'amplify'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateApp = Action('CreateApp')
CreateBranch = Action('CreateBranch')
CreateDomainAssociation = Action('CreateDomainAssociation')
DeleteApp = Action('DeleteApp')
DeleteBranch = Action('DeleteBranch')
DeleteDomainAssociation = Action('DeleteDomainAssociation')
DeleteJob = Action('DeleteJob')
GetApp = Action('GetApp')
GetBranch = Action('GetBranch')
GetDomainAssociation = Action('GetDomainAssociation')
GetJob = Action('GetJob')
ListApps = Action('ListApps')
ListBranches = Action('ListBranches')
ListDomainAssociations = Action('ListDomainAssociations')
ListJobs = Action('ListJobs')
StartJob = Action('StartJob')
StopJob = Action('StopJob')
UpdateApp = Action('UpdateApp')
UpdateBranch = Action('UpdateBranch')
UpdateDomainAssociation = Action('UpdateDomainAssociation')
