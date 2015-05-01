import unittest

from awacs.aws import Principal


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
