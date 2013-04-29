awacs - Amazon Web Access Control Subsystem

The awacs library allows for easier creation of AWS Access Policy
Language JSON by writing Python code to describe the AWS policies.
To facilitate catching  policy format or JSON errors early the
library has property and type checking built into the classes.

An example to use this comes from the [AWS IAM][] documentation.
This shows creating policy attached to an Amazon S3 bucket:

```
from awacs.aws import Action, Allow, Policy, Principal, Statement
from awacs.iam import IAM_ARN
from awacs.s3  import S3_ARN

account = "123456789012"
user = "user/Bob"

pd = Policy(
    Version="2012-10-17",
    Id="S3-Account-Permissions",
    Statement=[
        Statement(
            Sid="1",
            Effect=Allow,
            Principal=[Principal("AWS", [IAM_ARN(account, user)])],
            Action=[Action("s3", "*")],
            Resource=[S3_ARN("my_corporate_bucket/*"),],
        ),
    ],
)
print(pd.to_json())
```

would produce this json policy:

```
{
    "Id": "S3-Account-Permissions", 
    "Statement": [
        {
            "Action": [
                "s3:*"
            ], 
            "Effect": "Allow", 
            "Principal": [
                {
                    "AWS": [
                        "arn:aws:iam:123456789012:user/Bob:"
                    ]
                }
            ], 
            "Resource": [
                "arn:aws:s3::my_corporate_bucket/*:"
            ], 
            "Sid": "1"
        }
    ], 
    "Version": "2012-10-17"
}
```

[AWS IAM]: http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html
