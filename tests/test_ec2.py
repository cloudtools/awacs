import unittest

from awacs.ec2 import ARN


class TestARN(unittest.TestCase):
    def test_aws(self):
        arn = ARN("image/ami", "us-east-1", "account")
        self.assertEqual(
            arn.JSONrepr(), "arn:aws:ec2:us-east-1:account:image/ami")

    def test_cn(self):
        arn = ARN("image/ami", "cn-north-1", "account")
        self.assertEqual(
            arn.JSONrepr(), "arn:aws-cn:ec2:cn-north-1:account:image/ami")

    def test_gov(self):
        arn = ARN("image/ami", "us-gov-west-1", "account")
        self.assertEqual(
            arn.JSONrepr(),
            "arn:aws-us-gov:ec2:us-gov-west-1:account:image/ami")
