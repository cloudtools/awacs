# Example taken from AWS docs:
# http://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html

import awacs.ecr as aecr
import awacs.ecs as aecs
import awacs.logs as alogs
from awacs.aws import Allow, Policy, Statement

pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Action=[
                aecs.CreateCluster,
                aecs.DeregisterContainerInstance,
                aecs.DiscoverPollEndpoint,
                aecs.Poll,
                aecs.RegisterContainerInstance,
                aecs.StartTelemetrySession,
                aecr.GetAuthorizationToken,
                aecr.BatchCheckLayerAvailability,
                aecr.GetDownloadUrlForLayer,
                aecr.BatchGetImage,
                alogs.CreateLogStream,
                alogs.PutLogEvents,
                aecs.Action("Submit*"),
            ],
            Resource=["*"],
        )
    ]
)
print(pd.to_json())
