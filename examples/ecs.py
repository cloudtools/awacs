# Example taken from AWS docs:
# http://docs.aws.amazon.com/AmazonECS/latest/developerguide/IAM_policies.html#instance_IAM_role

from awacs.aws import Allow
from awacs.aws import Policy, Statement
import awacs.ecs as ecs


pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Action=[ecs.CreateCluster, ecs.RegisterContainerInstance,
                    ecs.DeregisterContainerInstance, ecs.DiscoverPollEndpoint,
                    ecs.Action("Submit*"), ecs.Poll],
            Resource=["*"]
        )
    ]
)
print(pd.to_json())
