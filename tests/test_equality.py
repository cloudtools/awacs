import unittest

from awacs import s3, ec2, iam
from awacs.aws import PolicyDocument, Statement, Action, Condition
from awacs.aws import StringEquals, StringLike


class TestEquality(unittest.TestCase):
    def test_condition_equality(self):
        self.assertEqualWithHash(
            Condition(StringLike("s3:prefix", ["home/${aws:username}/*"])),
            Condition(StringLike("s3:prefix", ["home/${aws:username}/*"])))

        self.assertNotEqualWithHash(
            Condition(StringLike("s3:prefix", ["home/${aws:username}/*"])),
            Condition(StringLike("s3:prefix", ["other/${aws:username}/*"])))

        self.assertNotEqualWithHash(
            Condition(StringLike("s3:prefix", ["home/${aws:username}/*"])),
            Condition(StringEquals("s3:prefix", ["home/${aws:username}/*"])))

    def test_arn_equality(self):
        self.assertEqualWithHash(
            s3.ARN("myBucket"), s3.ARN("myBucket"))

        self.assertNotEqualWithHash(
            s3.ARN("myBucket"), s3.ARN("myOtherBucket"))

        self.assertEqualWithHash(
            ec2.ARN("some-resource", "some-region", "some-account"),
            ec2.ARN("some-resource", "some-region", "some-account"))

        self.assertNotEqualWithHash(
            ec2.ARN("some-resource", "some-region", "some-account"),
            ec2.ARN("some-resource", "some-other-region", "some-account"))

        self.assertNotEqualWithHash(
            ec2.ARN("some-resource", "some-region", "some-account"),
            iam.ARN("some-resource", "some-region", "some-account"))

    def test_action_equality(self):
        self.assertEqualWithHash(
            Action('autoscaling', 'DescribeLaunchConfigurations'),
            Action('autoscaling', 'DescribeLaunchConfigurations'))

        self.assertNotEqualWithHash(
            Action('autoscaling', 'DescribeLaunchConfigurations'),
            Action('ec2', 'DescribeInstances'))

    def test_statement_equality(self):
        one = Statement(
            Effect="Allow",
            Action=[
                Action('autoscaling', 'DescribeLaunchConfigurations'),
            ],
            Resource=["*"]
        )
        one_again = Statement(
            Effect="Allow",
            Action=[
                Action('autoscaling', 'DescribeLaunchConfigurations'),
            ],
            Resource=["*"]
        )
        two = Statement(
            Effect="Allow",
            Action=[
                Action('ec2', 'DescribeInstances'),
            ],
            Resource=["*"]
        )

        self.assertEqualWithHash(one, one_again)
        self.assertNotEqualWithHash(one, two)

    def test_policy_document_equality(self):
        one = PolicyDocument(
            Version="2012-10-17",
            Statement=[
                Statement(
                    Effect="Allow",
                    Action=[
                        Action('autoscaling', 'DescribeLaunchConfigurations'),
                    ],
                    Resource=["*"]
                )
            ]
        )
        one_again = PolicyDocument(
            Version="2012-10-17",
            Statement=[
                Statement(
                    Effect="Allow",
                    Action=[
                        Action('autoscaling', 'DescribeLaunchConfigurations'),
                    ],
                    Resource=["*"]
                )
            ]
        )

        two = PolicyDocument(
            Version="2012-10-17",
            Statement=[
                Statement(
                    Effect="Allow",
                    Action=[
                        Action('ec2', 'DescribeInstances'),
                    ],
                    Resource=["*"]
                )
            ]
        )
        self.assertEqualWithHash(one, one_again)
        self.assertNotEqualWithHash(one, two)

    def assertEqualWithHash(self, one, two):
        self.assertTrue(one == two)
        self.assertEqual(hash(one), hash(two))

    def assertNotEqualWithHash(self, one, two):
        self.assertTrue(one != two)
        self.assertNotEqual(hash(one), hash(two))
