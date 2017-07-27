import unittest

import awacs.aws as aws
import awacs.s3 as s3
import json


class TestConditions(unittest.TestCase):
    def test_for_all_values(self):
        c = aws.Condition(aws.ForAllValuesStringLike(
            "dynamodb:requestedAttributes", [
                "PostDateTime",
                "Message",
                "Tags"
            ]))
        pd = aws.PolicyDocument(
            Statement=[
                aws.Statement(
                    Action=[s3.ListBucket],
                    Effect=aws.Allow,
                    Resource=[s3.ARN("myBucket")],
                    Condition=c,
                )])
        self.assertEqual({u'Statement': [
            {
                u'Action': [u's3:ListBucket'],
                u'Condition': {u'ForAllValues:StringLike':
                               {u'dynamodb:requestedAttributes':
                                [u'PostDateTime', u'Message', u'Tags']}},
                u'Effect': u'Allow',
                u'Resource': [u'arn:aws:s3:::myBucket']}
            ]},
            json.loads(pd.to_json()))
