import unittest

from awacs.s3 import ARN


class TestARN(unittest.TestCase):
    def test_aws(self):
        arn = ARN("bucket/key", "us-east-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws:s3:::bucket/key")

    def test_cn(self):
        arn = ARN("bucket/key", "cn-north-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws-cn:s3:::bucket/key")

    def test_gov(self):
        arn = ARN("bucket/key", "us-gov-west-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws-us-gov:s3:::bucket/key")
