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
DeleteObjectVersion = Action('DeleteObjectVersion')
GetAccelerateConfiguration = Action('GetAccelerateConfiguration')
GetBucketAcl = Action('GetBucketAcl')
GetBucketCORS = Action('GetBucketCORS')
GetBucketLocation = Action('GetBucketLocation')
GetBucketLogging = Action('GetBucketLogging')
GetBucketNotification = Action('GetBucketNotification')
GetBucketPolicy = Action('GetBucketPolicy')
GetBucketRequestPayment = Action('GetBucketRequestPayment')
GetBucketTagging = Action('GetBucketTagging')
GetBucketVersioning = Action('GetBucketVersioning')
GetBucketWebsite = Action('GetBucketWebsite')
GetLifecycleConfiguration = Action('GetLifecycleConfiguration')
GetObject = Action('GetObject')
GetObjectAcl = Action('GetObjectAcl')
GetObjectTorrent = Action('GetObjectTorrent')
GetObjectVersion = Action('GetObjectVersion')
GetObjectVersionAcl = Action('GetObjectVersionAcl')
GetObjectVersionTorrent = Action('GetObjectVersionTorrent')
GetReplicationConfiguration = Action('GetReplicationConfiguration')
ListAllMyBuckets = Action('ListAllMyBuckets')
ListBucket = Action('ListBucket')
ListBucketMultipartUploads = Action('ListBucketMultipartUploads')
ListBucketVersions = Action('ListBucketVersions')
ListMultipartUploadParts = Action('ListMultipartUploadParts')
PutAccelerateConfiguration = Action('PutAccelerateConfiguration')
PutBucketAcl = Action('PutBucketAcl')
PutBucketCORS = Action('PutBucketCORS')
PutBucketLogging = Action('PutBucketLogging')
PutBucketNotification = Action('PutBucketNotification')
PutBucketPolicy = Action('PutBucketPolicy')
PutBucketRequestPayment = Action('PutBucketRequestPayment')
PutBucketTagging = Action('PutBucketTagging')
PutBucketVersioning = Action('PutBucketVersioning')
PutBucketWebsite = Action('PutBucketWebsite')
PutLifecycleConfiguration = Action('PutLifecycleConfiguration')
PutReplicationConfiguration = Action('PutReplicationConfiguration')
PutObject = Action('PutObject')
PutObjectAcl = Action('PutObjectAcl')
PutObjectVersionAcl = Action('PutObjectVersionAcl')
ReplicateDelete = Action('ReplicateDelete')
ReplicateObject = Action('ReplicateObject')
RestoreObject = Action('RestoreObject')
