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


AssociateApprovalRuleTemplateWithRepository = \
    Action('AssociateApprovalRuleTemplateWithRepository')
BatchAssociateApprovalRuleTemplateWithRepositories = \
    Action('BatchAssociateApprovalRuleTemplateWithRepositories')
BatchDescribeMergeConflicts = Action('BatchDescribeMergeConflicts')
BatchDisassociateApprovalRuleTemplateFromRepositories = \
    Action('BatchDisassociateApprovalRuleTemplateFromRepositories')
BatchGetCommits = Action('BatchGetCommits')
BatchGetPullRequests = Action('BatchGetPullRequests')
BatchGetRepositories = Action('BatchGetRepositories')
CancelUploadArchive = Action('CancelUploadArchive')
CreateApprovalRuleTemplate = Action('CreateApprovalRuleTemplate')
CreateBranch = Action('CreateBranch')
CreateCommit = Action('CreateCommit')
CreatePullRequest = Action('CreatePullRequest')
CreatePullRequestApprovalRule = Action('CreatePullRequestApprovalRule')
CreateRepository = Action('CreateRepository')
CreateUnreferencedMergeCommit = Action('CreateUnreferencedMergeCommit')
DeleteApprovalRuleTemplate = Action('DeleteApprovalRuleTemplate')
DeleteBranch = Action('DeleteBranch')
DeleteCommentContent = Action('DeleteCommentContent')
DeleteFile = Action('DeleteFile')
DeletePullRequestApprovalRule = Action('DeletePullRequestApprovalRule')
DeleteRepository = Action('DeleteRepository')
DescribeMergeConflicts = Action('DescribeMergeConflicts')
DescribePullRequestEvents = Action('DescribePullRequestEvents')
DisassociateApprovalRuleTemplateFromRepository = \
    Action('DisassociateApprovalRuleTemplateFromRepository')
EvaluatePullRequestApprovalRules = \
    Action('EvaluatePullRequestApprovalRules')
GetApprovalRuleTemplate = Action('GetApprovalRuleTemplate')
GetBlob = Action('GetBlob')
GetBranch = Action('GetBranch')
GetComment = Action('GetComment')
GetCommentReactions = Action('GetCommentReactions')
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
GetPullRequestApprovalStates = Action('GetPullRequestApprovalStates')
GetPullRequestOverrideState = Action('GetPullRequestOverrideState')
GetReferences = Action('GetReferences')
GetRepository = Action('GetRepository')
GetRepositoryTriggers = Action('GetRepositoryTriggers')
GetTree = Action('GetTree')
GetUploadArchiveStatus = Action('GetUploadArchiveStatus')
GitPull = Action('GitPull')
GitPush = Action('GitPush')
ListApprovalRuleTemplates = Action('ListApprovalRuleTemplates')
ListAssociatedApprovalRuleTemplatesForRepository = \
    Action('ListAssociatedApprovalRuleTemplatesForRepository')
ListBranches = Action('ListBranches')
ListPullRequests = Action('ListPullRequests')
ListRepositories = Action('ListRepositories')
ListRepositoriesForApprovalRuleTemplate = \
    Action('ListRepositoriesForApprovalRuleTemplate')
ListTagsForResource = Action('ListTagsForResource')
MergeBranchesByFastForward = Action('MergeBranchesByFastForward')
MergeBranchesBySquash = Action('MergeBranchesBySquash')
MergeBranchesByThreeWay = Action('MergeBranchesByThreeWay')
MergePullRequestByFastForward = Action('MergePullRequestByFastForward')
MergePullRequestBySquash = Action('MergePullRequestBySquash')
MergePullRequestByThreeWay = Action('MergePullRequestByThreeWay')
OverridePullRequestApprovalRules = \
    Action('OverridePullRequestApprovalRules')
PostCommentForComparedCommit = Action('PostCommentForComparedCommit')
PostCommentForPullRequest = Action('PostCommentForPullRequest')
PostCommentReply = Action('PostCommentReply')
PutCommentReaction = Action('PutCommentReaction')
PutFile = Action('PutFile')
PutRepositoryTriggers = Action('PutRepositoryTriggers')
TagResource = Action('TagResource')
TestRepositoryTriggers = Action('TestRepositoryTriggers')
UntagResource = Action('UntagResource')
UpdateApprovalRuleTemplateContent = \
    Action('UpdateApprovalRuleTemplateContent')
UpdateApprovalRuleTemplateDescription = \
    Action('UpdateApprovalRuleTemplateDescription')
UpdateApprovalRuleTemplateName = Action('UpdateApprovalRuleTemplateName')
UpdateComment = Action('UpdateComment')
UpdateDefaultBranch = Action('UpdateDefaultBranch')
UpdatePullRequestApprovalRuleContent = \
    Action('UpdatePullRequestApprovalRuleContent')
UpdatePullRequestApprovalState = Action('UpdatePullRequestApprovalState')
UpdatePullRequestDescription = Action('UpdatePullRequestDescription')
UpdatePullRequestStatus = Action('UpdatePullRequestStatus')
UpdatePullRequestTitle = Action('UpdatePullRequestTitle')
UpdateRepositoryDescription = Action('UpdateRepositoryDescription')
UpdateRepositoryName = Action('UpdateRepositoryName')
UploadArchive = Action('UploadArchive')
