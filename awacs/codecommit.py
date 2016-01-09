# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS CodeCommit'
prefix = 'codecommit'

BatchGetRepositories = Action(prefix, 'BatchGetRepositories')
CreateBranch = Action(prefix, 'CreateBranch')
CreateRepository = Action(prefix, 'CreateRepository')
DeleteRepository = Action(prefix, 'DeleteRepository')
GetBranch = Action(prefix, 'GetBranch')
GetRepository = Action(prefix, 'GetRepository')
ListBranches = Action(prefix, 'ListBranches')
ListRepositories = Action(prefix, 'ListRepositories')
UpdateDefaultBranch = Action(prefix, 'UpdateDefaultBranch')
UpdateRepositoryDescription = Action(prefix, 'UpdateRepositoryDescription')
UpdateRepositoryName = Action(prefix, 'UpdateRepositoryName')
