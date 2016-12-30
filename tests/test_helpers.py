import unittest

from awacs.helpers.trust import get_default_assumerole_policy


def get_policy_service(policy):
    statement = policy.properties['Statement'][0]
    principal = statement.properties['Principal']
    return principal.data['Service']


class TestTrustHelpers(unittest.TestCase):
    def test_get_default_assumerole_policy(self):
        default_policy = get_default_assumerole_policy('us-east-1')
        cn_policy = get_default_assumerole_policy('cn-north-1')

        self.assertEqual(get_policy_service(default_policy),
                         ['ec2.amazonaws.com'])
        self.assertEqual(get_policy_service(cn_policy),
                         ['ec2.amazonaws.com.cn'])


if __name__ == '__main__':
    unittest.main()
