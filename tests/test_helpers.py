import unittest

from awacs.helpers.trust import (
    get_default_assumerole_policy,
    get_application_autoscaling_assumerole_policy,
    make_service_domain_name,
)


def get_policy_service(policy):
    statement = policy.properties['Statement'][0]
    principal = statement.properties['Principal']
    return principal.data['Service'][0]


class TestTrustHelpers(unittest.TestCase):

    def test_make_service_domain_name(self):
        self.assertEqual(
            'ec2.amazonaws.com',
            make_service_domain_name('ec2')
        )
        self.assertEqual(
            'ec2.amazonaws.com.cn',
            make_service_domain_name('ec2', region='cn-north-1')
        )
        # proove function is future proof.
        self.assertEqual(
            'ec2.amazonaws.com',
            make_service_domain_name('ec2', region='us-east-15')
        )

    def test_get_default_assumerole_policy(self):
        default_policy = get_default_assumerole_policy('us-east-1')
        cn_policy = get_default_assumerole_policy('cn-north-1')

        self.assertEqual(get_policy_service(default_policy),
                         'ec2.amazonaws.com')
        self.assertEqual(get_policy_service(cn_policy),
                         'ec2.amazonaws.com.cn')

    def test_get_application_autoscaling_assumerole_policy(self):
        assumerole_policy = get_application_autoscaling_assumerole_policy()
        self.assertEqual(
            'application-autoscaling.amazonaws.com',
            get_policy_service(assumerole_policy)
        )


if __name__ == '__main__':
    unittest.main()
