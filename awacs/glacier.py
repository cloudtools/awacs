# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Glacier'
prefix = 'glacier'

AbortMultipartUpload = Action(prefix, 'AbortMultipartUpload')
CompleteMultipartUpload = Action(prefix, 'CompleteMultipartUpload')
CreateVault = Action(prefix, 'CreateVault')
DeleteArchive = Action(prefix, 'DeleteArchive')
DeleteVault = Action(prefix, 'DeleteVault')
DeleteVaultNotifications = Action(prefix, 'DeleteVaultNotifications')
DescribeJob = Action(prefix, 'DescribeJob')
DescribeVault = Action(prefix, 'DescribeVault')
GetJobOutput = Action(prefix, 'GetJobOutput')
GetVaultNotifications = Action(prefix, 'GetVaultNotifications')
InitiateMultipartUpload = Action(prefix, 'InitiateMultipartUpload')
InitiateJob = Action(prefix, 'InitiateJob')
ListJobs = Action(prefix, 'ListJobs')
ListMultipartUploads = Action(prefix, 'ListMultipartUploads')
ListParts = Action(prefix, 'ListParts')
ListVaults = Action(prefix, 'ListVaults')
SetVaultNotifications = Action(prefix, 'SetVaultNotifications')
UploadArchive = Action(prefix, 'UploadArchive')
UploadMultipartPart = Action(prefix, 'UploadMultipartPart')
