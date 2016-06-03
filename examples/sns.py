from awacs.aws import Allow, ArnEquals, AWSPrincipal, Condition
from awacs.aws import Policy, Statement
import awacs.sns as sns
import awacs.sqs as sqs


region = 'us-east-1'
account = '012345678891'

pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Principal=AWSPrincipal("210987654321"),
            Action=[sqs.SendMessage],
            Resource=[sqs.ARN(region, account, "your_queue_xyz"), ],
            Condition=Condition(
                ArnEquals(
                    "aws:SourceArn",
                    sns.ARN(region, '123456789012', 'your_special_topic_1')
                ),
            ),
        ),
    ],
)
print(pd.to_json())
