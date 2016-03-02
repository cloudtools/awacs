from awacs.aws import Statement, Principal, Allow, Policy
from awacs import sts


def make_simple_assume_statement(principal):
    return Statement(
        Principal=Principal('Service', [principal]),
        Effect=Allow,
        Action=[sts.AssumeRole])


def get_default_assumerole_policy(region=''):
    """ Helper function for building the Default AssumeRole Policy

    Taken from here:
        https://github.com/boto/boto/blob/develop/boto/iam/connection.py#L29
    Used to allow ec2 instances to assume the roles in their InstanceProfile.
    """

    service = 'ec2.amazonaws.com'
    if region == 'cn-north-1':
        service = 'ec2.amazonaws.com.cn'
    policy = Policy(
        Statement=[make_simple_assume_statement(service)]
    )
    return policy


def get_ecs_assumerole_policy(region=''):
    """ Helper function for building the ECS AssumeRole Policy
    """

    service = 'ecs.amazonaws.com'
    policy = Policy(
        Statement=[make_simple_assume_statement(service)]
    )
    return policy


def get_lambda_assumerole_policy(region=''):
    """ Helper function for building the ECS AssumeRole Policy
    """

    service = 'lambda.amazonaws.com'
    policy = Policy(
        Statement=[make_simple_assume_statement(service)]
    )
    return policy
