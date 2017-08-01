import unittest

from awacs.aws import PolicyDocument


class TestAWSObject(unittest.TestCase):
    def test_invalid_property(self):
        with self.assertRaises(AttributeError) as exc:
            # statement should be Statement
            PolicyDocument(Version='2012-10-17', statement=[])

        self.assertEqual(
            exc.exception.args[0],
            "'awacs.aws.PolicyDocument' object does not support attribute "
            "'statement'"
        )
