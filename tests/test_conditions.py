import json
import unittest

import awacs.aws as aws
import awacs.s3 as s3


class TestConditions(unittest.TestCase):
    def test_for_all_values(self):
        c = aws.Condition(
            aws.ForAllValuesStringLike(
                "dynamodb:requestedAttributes", ["PostDateTime", "Message", "Tags"]
            )
        )
        pd = aws.PolicyDocument(
            Statement=[
                aws.Statement(
                    Action=[s3.ListBucket],
                    Effect=aws.Allow,
                    Resource=[s3.ARN("myBucket")],
                    Condition=c,
                )
            ]
        )
        self.assertEqual(
            {
                "Statement": [
                    {
                        "Action": ["s3:ListBucket"],
                        "Condition": {
                            "ForAllValues:StringLike": {
                                "dynamodb:requestedAttributes": [
                                    "PostDateTime",
                                    "Message",
                                    "Tags",
                                ]
                            }
                        },
                        "Effect": "Allow",
                        "Resource": ["arn:aws:s3:::myBucket"],
                    }
                ]
            },
            json.loads(pd.to_json()),
        )
