# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon S3 on Outposts'
prefix = 's3-outposts'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AbortMultipartUpload = Action('AbortMultipartUpload')
CreateAccessPoint = Action('CreateAccessPoint')
CreateBucket = Action('CreateBucket')
CreateEndpoint = Action('CreateEndpoint')
DeleteAccessPoint = Action('DeleteAccessPoint')
DeleteAccessPointPolicy = Action('DeleteAccessPointPolicy')
DeleteBucket = Action('DeleteBucket')
DeleteBucketPolicy = Action('DeleteBucketPolicy')
DeleteEndpoint = Action('DeleteEndpoint')
DeleteObject = Action('DeleteObject')
DeleteObjectTagging = Action('DeleteObjectTagging')
GetAccessPoint = Action('GetAccessPoint')
GetAccessPointPolicy = Action('GetAccessPointPolicy')
GetBucket = Action('GetBucket')
GetBucketPolicy = Action('GetBucketPolicy')
GetBucketTagging = Action('GetBucketTagging')
GetLifecycleConfiguration = Action('GetLifecycleConfiguration')
GetObject = Action('GetObject')
GetObjectTagging = Action('GetObjectTagging')
ListAccessPoints = Action('ListAccessPoints')
ListBucket = Action('ListBucket')
ListBucketMultipartUploads = Action('ListBucketMultipartUploads')
ListEndpoints = Action('ListEndpoints')
ListMultipartUploadParts = Action('ListMultipartUploadParts')
ListRegionalBuckets = Action('ListRegionalBuckets')
PutAccessPointPolicy = Action('PutAccessPointPolicy')
PutBucketPolicy = Action('PutBucketPolicy')
PutBucketTagging = Action('PutBucketTagging')
PutLifecycleConfiguration = Action('PutLifecycleConfiguration')
PutObject = Action('PutObject')
PutObjectAcl = Action('PutObjectAcl')
PutObjectTagging = Action('PutObjectTagging')
