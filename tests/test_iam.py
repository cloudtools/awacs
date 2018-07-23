import unittest

from awacs.iam import ARN


class TestARN(unittest.TestCase):
    def test_aws(self):
        arn = ARN("root", "us-east-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws:iam::account:root")

    def test_cn(self):
        arn = ARN("root", "cn-north-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws-cn:iam::account:root")

    def test_gov(self):
        arn = ARN("root", "us-gov-west-1", "account")
        self.assertEqual(arn.JSONrepr(), "arn:aws-us-gov:iam::account:root")
