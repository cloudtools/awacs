# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action


# Actions Related to Objects
GetObject = Action("s3:GetObject")
GetObjectVersion = Action("s3:GetObjectVersion")
PutObject = Action("s3:PutObject")
GetObjectAcl = Action("s3:GetObjectAcl")
GetObjectVersionAcl = Action("s3:GetObjectVersionAcl")
PutObjectAcl = Action("s3:PutObjectAcl")
PutObjectVersionAcl = Action("s3:PutObjectVersionAcl")
DeleteObject = Action("s3:DeleteObject")
DeleteObjectVersion = Action("s3:DeleteObjectVersion")
ListMultipartUploadParts = Action("s3:ListMultipartUploadParts")
AbortMultipartUpload = Action("s3:AbortMultipartUpload")
GetObjectTorrent = Action("s3:GetObjectTorrent")
GetObjectVersionTorrent = Action("s3:GetObjectVersionTorrent")
RestoreObject = Action("s3:RestoreObject")

# Actions Related to Buckets
CreateBucket = Action("s3:CreateBucket")
DeleteBucket = Action("s3:DeleteBucket")
ListBucket = Action("s3:ListBucket")
ListBucketVersions = Action("s3:ListBucketVersions")
ListAllMyBuckets = Action("s3:ListAllMyBuckets")
ListBucketMultipartUploads = Action("s3:ListBucketMultipartUploads")

# Actions Related to Bucket Sub-Resources
GetBucketAcl = Action("s3:GetBucketAcl")
PutBucketAcl = Action("s3:PutBucketAcl")
GetBucketCORS = Action("s3:GetBucketCORS")
PutBucketCORS = Action("s3:PutBucketCORS")
GetBucketVersioning = Action("s3:GetBucketVersioning")
PutBucketVersioning = Action("s3:PutBucketVersioning")
GetBucketRequestPayment = Action("s3:GetBucketRequestPayment")
PutBucketRequestPayment = Action("s3:PutBucketRequestPayment")
GetBucketLocation = Action("s3:GetBucketLocation")
GetBucketPolicy = Action("s3:GetBucketPolicy")
DeleteBucketPolicy = Action("s3:DeleteBucketPolicy")
PutBucketPolicy = Action("s3:PutBucketPolicy")
GetBucketNotification = Action("s3:GetBucketNotification")
PutBucketNotification = Action("s3:PutBucketNotification")
GetBucketLogging = Action("s3:GetBucketLogging")
PutBucketLogging = Action("s3:PutBucketLogging")
GetBucketWebsite = Action("s3:GetBucketWebsite")
PutBucketWebsite = Action("s3:PutBucketWebsite")
DeleteBucketWebsite = Action("s3:DeleteBucketWebsite")
GetLifecycleConfiguration = Action("s3:GetLifecycleConfiguration")
PutLifecycleConfiguration = Action("s3:PutLifecycleConfiguration")
