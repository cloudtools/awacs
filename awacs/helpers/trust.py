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
        ],
        Version="2012-10-17"
    )


def make_service_domain_name(service, region=''):
    """ Helper function for creating proper service domain names. """
    tld = ".com.cn" if region == "cn-north-1" else ".com"
    return "{}.amazonaws{}".format(service, tld)


def get_codedeploy_assumerole_policy(region=''):
    """ Helper function for building the AWS CodeDeploy AssumeRole Policy. """
    service = make_service_domain_name('codedeploy', region)
    return make_simple_assume_policy(service)


def get_default_assumerole_policy(region=''):
    """ Helper function for building the Default AssumeRole Policy.

    Taken from here:
        https://github.com/boto/boto/blob/develop/boto/iam/connection.py#L29
    Used to allow ec2 instances to assume the roles in their InstanceProfile.
    """
    service = make_service_domain_name('ec2', region)
    return make_simple_assume_policy(service)


def get_ecs_assumerole_policy(region=''):
    """ Helper function for building the ECS AssumeRole Policy. """
    service = make_service_domain_name('ecs', region)
    return make_simple_assume_policy(service)


def get_ecs_task_assumerole_policy(region=''):
    """ Helper function for building the AssumeRole Policy for ECS Tasks. """
    service = make_service_domain_name('ecs-tasks', region)
    return make_simple_assume_policy(service)


def get_lambda_assumerole_policy(region=''):
    """ Helper function for building the AWS Lambda AssumeRole Policy. """
    service = make_service_domain_name('lambda', region)
    return make_simple_assume_policy(service)


def get_lambda_edge_assumerole_policy(region=''):
    """ Helper function for building the AWS Lambda@Edge AssumeRole Policy. """
    return make_simple_assume_policy(*[
        make_service_domain_name(service, region)
        for service in ('lambda', 'edgelambda')
    ])


def get_application_autoscaling_assumerole_policy(region=''):
    """ Helper function for building the AWS Lambda AssumeRole Policy. """
    service = make_service_domain_name('application-autoscaling', region)
    return make_simple_assume_policy(service)
