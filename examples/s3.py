# Example taken from AWS docs:
# http://docs.aws.amazon.com/IAM/latest/UserGuide/
# ExampleIAMPolicies.html#iampolicy-example-s3homedir

from awacs.aws import Action, Allow, Condition
from awacs.aws import Policy, Statement
from awacs.aws import StringEquals, StringLike
import awacs.s3 as s3


pd = Policy(
    Statement=[
        Statement(
            Action=[s3.ListAllMyBuckets, s3.GetBucketLocation],
            Effect=Allow,
            Resource=[s3.ARN("*"), ],
        ),
        Statement(
            Action=[s3.ListBucket],
            Effect=Allow,
            Resource=[s3.ARN("myBucket")],
            Condition=Condition(
                StringEquals({
                    's3:prefix': ['', 'home/'],
                    's3:delimiter': ['/'],
                }),
            ),
        ),
        Statement(
            Action=[s3.ListBucket],
            Effect=Allow,
            Resource=[s3.ARN("myBucket")],
            Condition=Condition(
                StringLike("s3:prefix", ["home/${aws:username}/*"])
            ),
        ),
        Statement(
            Action=[Action("s3", "*")],
            Effect=Allow,
            Resource=[
                s3.ARN("myBucket/home/${aws:username}"),
                s3.ARN("myBucket/home/${aws:username}/*"),
            ],
        ),
    ],
)
print(pd.to_json())
