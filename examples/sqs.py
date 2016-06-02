from awacs.aws import Allow, AWSPrincipal, Condition
from awacs.aws import Policy, Statement
from awacs.aws import DateGreaterThan, DateLessThan, IpAddress
import awacs.sqs as sqs


region = 'us-east-1'
account = '444455556666'

pd = Policy(
    Id="Queue1_Policy_UUID",
    Statement=[
        Statement(
            Sid="Queue1_SendMessage",
            Effect=Allow,
            Principal=AWSPrincipal("111122223333"),
            Action=[sqs.SendMessage],
            Resource=[sqs.ARN(region, account, "queue1"), ],
            Condition=Condition([
                DateGreaterThan("aws:CurrentTime", "2010-08-16T12:00:00Z"),
                DateLessThan("aws:CurrentTime", "2010-08-16T15:00:00Z"),
                IpAddress("aws:SourceIp", ["192.0.2.0/24", "203.0.113.0/24"]),
            ]),
        ),
    ],
)
print(pd.to_json())
