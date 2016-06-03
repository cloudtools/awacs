# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Glacier'
prefix = 'glacier'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AbortVaultLock = Action('AbortVaultLock')
AddTagsToVault = Action('AddTagsToVault')
AbortMultipartUpload = Action('AbortMultipartUpload')
CompleteMultipartUpload = Action('CompleteMultipartUpload')
CompleteVaultLock = Action('CompleteVaultLock')
CreateVault = Action('CreateVault')
DeleteArchive = Action('DeleteArchive')
DeleteVault = Action('DeleteVault')
DeleteVaultAccessPolicy = Action('DeleteVaultAccessPolicy')
DeleteVaultNotifications = Action('DeleteVaultNotifications')
DescribeJob = Action('DescribeJob')
DescribeVault = Action('DescribeVault')
GetDataRetrievalPolicy = Action('GetDataRetrievalPolicy')
GetJobOutput = Action('GetJobOutput')
GetVaultAccessPolicy = Action('GetVaultAccessPolicy')
GetVaultLock = Action('GetVaultLock')
GetVaultNotifications = Action('GetVaultNotifications')
InitiateJob = Action('InitiateJob')
InitiateMultipartUpload = Action('InitiateMultipartUpload')
InitiateVaultLock = Action('InitiateVaultLock')
ListJobs = Action('ListJobs')
ListMultipartUploads = Action('ListMultipartUploads')
ListParts = Action('ListParts')
ListTagsForVault = Action('ListTagsForVault')
ListVaults = Action('ListVaults')
RemoveTagsFromVault = Action('RemoveTagsFromVault')
SetDataRetrievalPolicy = Action('SetDataRetrievalPolicy')
SetVaultAccessPolicy = Action('SetVaultAccessPolicy')
SetVaultNotifications = Action('SetVaultNotifications')
UploadArchive = Action('UploadArchive')
UploadMultipartPart = Action('UploadMultipartPart')
