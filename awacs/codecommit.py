# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeCommit'
prefix = 'codecommit'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchGetRepositories = Action('BatchGetRepositories')
CreateBranch = Action('CreateBranch')
CreateRepository = Action('CreateRepository')
DeleteRepository = Action('DeleteRepository')
GetBlob = Action('GetBlob')
GetBranch = Action('GetBranch')
GetObjectIdentifier = Action('GetObjectIdentifier')
GetRepository = Action('GetRepository')
GetTree = Action('GetTree')
GitPull = Action('GitPull')
GitPush = Action('GitPush')
ListBranches = Action('ListBranches')
ListRepositories = Action('ListRepositories')
UpdateDefaultBranch = Action('UpdateDefaultBranch')
UpdateRepositoryDescription = Action('UpdateRepositoryDescription')
UpdateRepositoryName = Action('UpdateRepositoryName')
