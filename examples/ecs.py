# Example taken from AWS docs:
# http://docs.aws.amazon.com/IAM/latest/UserGuide/
# ExampleIAMPolicies.html#iampolicy-example-s3homedir

from awacs.aws import Allow
from awacs.aws import Policy, Statement
import awacs.ecs as ecs


pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Action=[ecs.CreateCluster, ecs.RegisterContainerInstance,
                    ecs.DeregisterContainerInstance, ecs.DiscoverPollEndpoint,
                    ecs.ECSAction("Submit*"), ecs.Poll],
            Resource=["*"]
        )
    ]
)
print(pd.to_json())
