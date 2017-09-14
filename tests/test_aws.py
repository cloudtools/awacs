import unittest

from awacs.aws import BaseARN, Principal


class TestPrincipal(unittest.TestCase):
    def test_wildcard_principal(self):
        p = Principal("*")
        self.assertEqual(p.data, "*")
        with self.assertRaises(ValueError):
            p = Principal("*", "FAIL")

    def test_normal_principal(self):
        p = Principal("AWS", "arn:aws:iam::AccountNumber-WithoutHyphens:root")
        self.assertEqual(
            p.data,
            {'AWS': 'arn:aws:iam::AccountNumber-WithoutHyphens:root'}
        )
        with self.assertRaises(ValueError):
            p = Principal("AWS")

    def test_invalid_principal_string(self):
        with self.assertRaises(ValueError):
            Principal("aws", "arn:aws:iam::AccountNumber-WithoutHyphens:root")


class TestBaseARN(unittest.TestCase):
    def test_aws(self):
        arn = BaseARN("service", "resource", "us-east-1", "account")
        self.assertEqual(
            arn.JSONrepr(), "arn:aws:service:us-east-1:account:resource")

    def test_cn(self):
        arn = BaseARN("service", "resource", "cn-north-1", "account")
        self.assertEqual(
            arn.JSONrepr(), "arn:aws-cn:service:cn-north-1:account:resource")

    def test_gov(self):
        arn = BaseARN("service", "resource", "us-gov-west-1", "account")
        self.assertEqual(
            arn.JSONrepr(),
            "arn:aws-us-gov:service:us-gov-west-1:account:resource")
