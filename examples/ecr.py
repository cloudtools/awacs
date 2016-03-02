# Example taken from AWS docs:
# http://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr_managed_policies.html

from awacs.aws import Allow
from awacs.aws import Policy, Statement
import awacs.ecr as ecr


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
            Resource=['*']
        )
    ]
)


print(pd.to_json())
