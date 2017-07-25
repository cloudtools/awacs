from awacs.aws import Statement, Principal, Allow, Policy
from awacs import sts


def make_simple_assume_statement(*principals):
    return Statement(
        Principal=Principal('Service', principals),
        Effect=Allow,
        Action=[sts.AssumeRole]
    )


def make_simple_assume_policy(*principals):
    return Policy(
        Statement=[
            make_simple_assume_statement(*principals)
        ]
    )


def get_codedeploy_assumerole_policy():
    """ Helper function for building the AWS CodeDeploy AssumeRole Policy
    """

    service = 'codedeploy.amazonaws.com'
    policy = Policy(
        Statement=[make_simple_assume_statement(service)]
    )
    return policy


def get_default_assumerole_policy(region=''):
    """ Helper function for building the Default AssumeRole Policy

    Taken from here:
        https://github.com/boto/boto/blob/develop/boto/iam/connection.py#L29
    Used to allow ec2 instances to assume the roles in their InstanceProfile.
    """

    service = 'ec2.amazonaws.com'
    if region == 'cn-north-1':
        service = 'ec2.amazonaws.com.cn'

    return make_simple_assume_policy(service)


def get_ecs_assumerole_policy(region=''):
    """ Helper function for building the ECS AssumeRole Policy
    """

    service = 'ecs.amazonaws.com'
    return make_simple_assume_policy(service)


def get_ecs_task_assumerole_policy(region=''):
    """ Helper function for building the AssumeRole Policy for ECS Tasks
    """

    service = 'ecs-tasks.amazonaws.com'
    policy = Policy(
        Statement=[make_simple_assume_statement(service)]
    )
    return policy


def get_lambda_assumerole_policy(region=''):
    """ Helper function for building the AWS Lambda AssumeRole Policy
    """

    service = 'lambda.amazonaws.com'
    return make_simple_assume_policy(service)
