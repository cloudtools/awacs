# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import warnings

from aws import Action, BaseARN

service_name = 'Amazon S3'
prefix = 's3'


class ARN(BaseARN):
    def __init__(self, resource):
        sup = super(ARN, self)
        sup.__init__(service='s3', resource=resource)


class S3_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(S3_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use s3.ARN instead.",
                      FutureWarning)


AbortMultipartUpload = Action(prefix, 'AbortMultipartUpload')
CreateBucket = Action(prefix, 'CreateBucket')
DeleteBucket = Action(prefix, 'DeleteBucket')
DeleteBucketPolicy = Action(prefix, 'DeleteBucketPolicy')
DeleteBucketWebsite = Action(prefix, 'DeleteBucketWebsite')
DeleteObject = Action(prefix, 'DeleteObject')
DeleteObjectVersion = Action(prefix, 'DeleteObjectVersion')
GetBucketAcl = Action(prefix, 'GetBucketAcl')
GetBucketCORS = Action(prefix, 'GetBucketCORS')
GetBucketLocation = Action(prefix, 'GetBucketLocation')
GetBucketLogging = Action(prefix, 'GetBucketLogging')
GetBucketNotification = Action(prefix, 'GetBucketNotification')
GetBucketPolicy = Action(prefix, 'GetBucketPolicy')
GetBucketRequestPayment = Action(prefix, 'GetBucketRequestPayment')
GetBucketTagging = Action(prefix, 'GetBucketTagging')
GetBucketVersioning = Action(prefix, 'GetBucketVersioning')
GetBucketWebsite = Action(prefix, 'GetBucketWebsite')
GetLifecycleConfiguration = Action(prefix, 'GetLifecycleConfiguration')
GetObject = Action(prefix, 'GetObject')
GetObjectAcl = Action(prefix, 'GetObjectAcl')
GetObjectTorrent = Action(prefix, 'GetObjectTorrent')
GetObjectVersion = Action(prefix, 'GetObjectVersion')
GetObjectVersionAcl = Action(prefix, 'GetObjectVersionAcl')
GetObjectVersionTorrent = Action(prefix, 'GetObjectVersionTorrent')
ListAllMyBuckets = Action(prefix, 'ListAllMyBuckets')
ListBucket = Action(prefix, 'ListBucket')
ListBucketMultipartUploads = \
    Action(prefix, 'ListBucketMultipartUploads')
ListBucketVersions = Action(prefix, 'ListBucketVersions')
ListMultipartUploadParts = Action(prefix, 'ListMultipartUploadParts')
PutBucketAcl = Action(prefix, 'PutBucketAcl')
PutBucketCORS = Action(prefix, 'PutBucketCORS')
PutBucketLogging = Action(prefix, 'PutBucketLogging')
PutBucketNotification = Action(prefix, 'PutBucketNotification')
PutBucketPolicy = Action(prefix, 'PutBucketPolicy')
PutBucketRequestPayment = Action(prefix, 'PutBucketRequestPayment')
PutBucketTagging = Action(prefix, 'PutBucketTagging')
PutBucketVersioning = Action(prefix, 'PutBucketVersioning')
PutBucketWebsite = Action(prefix, 'PutBucketWebsite')
PutLifecycleConfiguration = Action(prefix, 'PutLifecycleConfiguration')
PutObject = Action(prefix, 'PutObject')
PutObjectAcl = Action(prefix, 'PutObjectAcl')
PutObjectVersionAcl = Action(prefix, 'PutObjectVersionAcl')
RestoreObject = Action(prefix, 'RestoreObject')
