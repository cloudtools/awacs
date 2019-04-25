# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon FSx'
prefix = 'fsx'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateBackup = Action('CreateBackup')
CreateFileSystem = Action('CreateFileSystem')
CreateFileSystemFromBackup = Action('CreateFileSystemFromBackup')
DeleteBackup = Action('DeleteBackup')
DeleteFileSystem = Action('DeleteFileSystem')
DescribeBackups = Action('DescribeBackups')
DescribeFileSystems = Action('DescribeFileSystems')
ListTagsForResource = Action('ListTagsForResource')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateFileSystem = Action('UpdateFileSystem')
