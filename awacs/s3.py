import warnings
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon S3'
prefix = 's3'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        # account is empty for S3
        account = ''
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class S3_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(S3_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use s3.ARN instead.",
                      FutureWarning)


AbortMultipartUpload = Action('AbortMultipartUpload')
CreateBucket = Action('CreateBucket')
DeleteBucket = Action('DeleteBucket')
DeleteBucketPolicy = Action('DeleteBucketPolicy')
DeleteBucketWebsite = Action('DeleteBucketWebsite')
DeleteObject = Action('DeleteObject')
DeleteObjectTagging = Action('DeleteObjectTagging')
DeleteObjectVersion = Action('DeleteObjectVersion')
DeleteObjectVersionTagging = Action('DeleteObjectVersionTagging')
GetAccelerateConfiguration = Action('GetAccelerateConfiguration')
GetAccountPublicAccessBlock = Action('GetAccountPublicAccessBlock')
GetAnalyticsConfiguration = Action('GetAnalyticsConfiguration')
GetBucketAcl = Action('GetBucketAcl')
GetBucketCORS = Action('GetBucketCORS')
GetBucketLocation = Action('GetBucketLocation')
GetBucketLogging = Action('GetBucketLogging')
GetBucketNotification = Action('GetBucketNotification')
GetBucketPolicy = Action('GetBucketPolicy')
GetBucketPolicyStatus = Action('GetBucketPolicyStatus')
GetBucketPublicAccessBlock = Action('GetBucketPublicAccessBlock')
GetBucketRequestPayment = Action('GetBucketRequestPayment')
GetBucketTagging = Action('GetBucketTagging')
GetBucketVersioning = Action('GetBucketVersioning')
GetBucketWebsite = Action('GetBucketWebsite')
GetEncryptionConfiguration = Action('GetEncryptionConfiguration')
GetInventoryConfiguration = Action('GetInventoryConfiguration')
GetIpConfiguration = Action('GetIpConfiguration')
GetLifecycleConfiguration = Action('GetLifecycleConfiguration')
GetMetricsConfiguration = Action('GetMetricsConfiguration')
GetObject = Action('GetObject')
GetObjectAcl = Action('GetObjectAcl')
GetObjectTagging = Action('GetObjectTagging')
GetObjectTorrent = Action('GetObjectTorrent')
GetObjectVersion = Action('GetObjectVersion')
GetObjectVersionAcl = Action('GetObjectVersionAcl')
GetObjectVersionForReplication = Action('GetObjectVersionForReplication')
GetObjectVersionTagging = Action('GetObjectVersionTagging')
GetObjectVersionTorrent = Action('GetObjectVersionTorrent')
GetReplicationConfiguration = Action('GetReplicationConfiguration')
HeadBucket = Action('HeadBucket')
ListAllMyBuckets = Action('ListAllMyBuckets')
ListBucket = Action('ListBucket')
ListBucketByTags = Action('ListBucketByTags')
ListBucketMultipartUploads = Action('ListBucketMultipartUploads')
ListBucketVersions = Action('ListBucketVersions')
ListMultipartUploadParts = Action('ListMultipartUploadParts')
ListObjects = Action('ListObjects')
ObjectOwnerOverrideToBucketOwner = \
    Action('ObjectOwnerOverrideToBucketOwner')
PutAccelerateConfiguration = Action('PutAccelerateConfiguration')
PutAccountPublicAccessBlock = Action('PutAccountPublicAccessBlock')
PutAnalyticsConfiguration = Action('PutAnalyticsConfiguration')
PutBucketAcl = Action('PutBucketAcl')
PutBucketCORS = Action('PutBucketCORS')
PutBucketLogging = Action('PutBucketLogging')
PutBucketNotification = Action('PutBucketNotification')
PutBucketPolicy = Action('PutBucketPolicy')
PutBucketPublicAccessBlock = Action('PutBucketPublicAccessBlock')
PutBucketRequestPayment = Action('PutBucketRequestPayment')
PutBucketTagging = Action('PutBucketTagging')
PutBucketVersioning = Action('PutBucketVersioning')
PutBucketWebsite = Action('PutBucketWebsite')
PutEncryptionConfiguration = Action('PutEncryptionConfiguration')
PutInventoryConfiguration = Action('PutInventoryConfiguration')
PutIpConfiguration = Action('PutIpConfiguration')
PutLifecycleConfiguration = Action('PutLifecycleConfiguration')
PutMetricsConfiguration = Action('PutMetricsConfiguration')
PutObject = Action('PutObject')
PutObjectAcl = Action('PutObjectAcl')
PutObjectTagging = Action('PutObjectTagging')
PutObjectVersionAcl = Action('PutObjectVersionAcl')
PutObjectVersionTagging = Action('PutObjectVersionTagging')
PutReplicationConfiguration = Action('PutReplicationConfiguration')
ReplicateDelete = Action('ReplicateDelete')
ReplicateObject = Action('ReplicateObject')
ReplicateTags = Action('ReplicateTags')
RestoreObject = Action('RestoreObject')
