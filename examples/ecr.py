# Example taken from AWS docs:
# http://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr_managed_policies.html

import awacs.ecr as ecr
from awacs.aws import Allow, Policy, Statement

# AmazonEC2ContainerRegistryReadOnly
pd = Policy(
    Statement=[
        Statement(
            Effect=Allow,
            Action=[
                ecr.GetAuthorizationToken,
                ecr.BatchCheckLayerAvailability,
                ecr.GetDownloadUrlForLayer,
                ecr.GetRepositoryPolicy,
                ecr.DescribeRepositories,
                ecr.ListImages,
                ecr.BatchGetImage,
            ],
            Resource=["*"],
        )
    ]
)


print(pd.to_json())
