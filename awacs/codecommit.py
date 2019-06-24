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


BatchDescribeMergeConflicts = Action('BatchDescribeMergeConflicts')
BatchGetPullRequests = Action('BatchGetPullRequests')
BatchGetRepositories = Action('BatchGetRepositories')
CancelUploadArchive = Action('CancelUploadArchive')
CreateBranch = Action('CreateBranch')
CreateCommit = Action('CreateCommit')
CreatePullRequest = Action('CreatePullRequest')
CreateRepository = Action('CreateRepository')
CreateUnreferencedMergeCommit = Action('CreateUnreferencedMergeCommit')
DeleteBranch = Action('DeleteBranch')
DeleteCommentContent = Action('DeleteCommentContent')
DeleteFile = Action('DeleteFile')
DeleteRepository = Action('DeleteRepository')
DescribeMergeConflicts = Action('DescribeMergeConflicts')
DescribePullRequestEvents = Action('DescribePullRequestEvents')
GetBlob = Action('GetBlob')
GetBranch = Action('GetBranch')
GetComment = Action('GetComment')
GetCommentsForComparedCommit = Action('GetCommentsForComparedCommit')
GetCommentsForPullRequest = Action('GetCommentsForPullRequest')
GetCommit = Action('GetCommit')
GetCommitHistory = Action('GetCommitHistory')
GetCommitsFromMergeBase = Action('GetCommitsFromMergeBase')
GetDifferences = Action('GetDifferences')
GetFile = Action('GetFile')
GetFolder = Action('GetFolder')
GetMergeCommit = Action('GetMergeCommit')
GetMergeConflicts = Action('GetMergeConflicts')
GetMergeOptions = Action('GetMergeOptions')
GetObjectIdentifier = Action('GetObjectIdentifier')
GetPullRequest = Action('GetPullRequest')
GetReferences = Action('GetReferences')
GetRepository = Action('GetRepository')
GetRepositoryTriggers = Action('GetRepositoryTriggers')
GetTree = Action('GetTree')
GetUploadArchiveStatus = Action('GetUploadArchiveStatus')
GitPull = Action('GitPull')
GitPush = Action('GitPush')
ListBranches = Action('ListBranches')
ListPullRequests = Action('ListPullRequests')
ListRepositories = Action('ListRepositories')
ListTagsForResource = Action('ListTagsForResource')
MergeBranchesByFastForward = Action('MergeBranchesByFastForward')
MergeBranchesBySquash = Action('MergeBranchesBySquash')
MergeBranchesByThreeWay = Action('MergeBranchesByThreeWay')
MergePullRequestByFastForward = Action('MergePullRequestByFastForward')
MergePullRequestBySquash = Action('MergePullRequestBySquash')
MergePullRequestByThreeWay = Action('MergePullRequestByThreeWay')
PostCommentForComparedCommit = Action('PostCommentForComparedCommit')
PostCommentForPullRequest = Action('PostCommentForPullRequest')
PostCommentReply = Action('PostCommentReply')
PutFile = Action('PutFile')
PutRepositoryTriggers = Action('PutRepositoryTriggers')
TagResource = Action('TagResource')
TestRepositoryTriggers = Action('TestRepositoryTriggers')
UntagResource = Action('UntagResource')
UpdateComment = Action('UpdateComment')
UpdateDefaultBranch = Action('UpdateDefaultBranch')
UpdatePullRequestDescription = Action('UpdatePullRequestDescription')
UpdatePullRequestStatus = Action('UpdatePullRequestStatus')
UpdatePullRequestTitle = Action('UpdatePullRequestTitle')
UpdateRepositoryDescription = Action('UpdateRepositoryDescription')
UpdateRepositoryName = Action('UpdateRepositoryName')
UploadArchive = Action('UploadArchive')
