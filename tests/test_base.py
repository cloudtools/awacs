import unittest

from awacs.aws import Policy


class TestAWSObject(unittest.TestCase):
    def test_invalid_property(self):
        with self.assertRaises(AttributeError) as exc:
            # statement should be Statement
            Policy(Version='2012-10-17', statement=[])

        self.assertEqual(
            exc.exception.args[0],
            "'awacs.aws.Policy' object does not support attribute 'statement'"
        )
