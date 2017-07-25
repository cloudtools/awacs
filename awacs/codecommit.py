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
CancelUploadArchive = Action('CancelUploadArchive')
CreateBranch = Action('CreateBranch')
CreateRepository = Action('CreateRepository')
DeleteBranch = Action('DeleteBranch')
DeleteRepository = Action('DeleteRepository')
GetBlob = Action('GetBlob')
GetBranch = Action('GetBranch')
GetCommit = Action('GetCommit')
GetDifferences = Action('GetDifferences')
GetObjectIdentifier = Action('GetObjectIdentifier')
GetReferences = Action('GetReferences')
GetRepository = Action('GetRepository')
GetRepositoryTriggers = Action('GetRepositoryTriggers')
GetTree = Action('GetTree')
GetUploadArchiveStatus = Action('GetUploadArchiveStatus')
GitPull = Action('GitPull')
GitPush = Action('GitPush')
ListBranches = Action('ListBranches')
ListRepositories = Action('ListRepositories')
PutRepositoryTriggers = Action('PutRepositoryTriggers')
TestRepositoryTriggers = Action('TestRepositoryTriggers')
UpdateDefaultBranch = Action('UpdateDefaultBranch')
UpdateRepositoryDescription = Action('UpdateRepositoryDescription')
UpdateRepositoryName = Action('UpdateRepositoryName')
UploadArchive = Action('UploadArchive')
