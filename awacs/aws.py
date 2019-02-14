# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import warnings

from . import AWSHelperFn, AWSProperty

# Policy effect constants.
Allow = "Allow"
Deny = "Deny"

# Policy principal constants.
Everybody = "*"

# Policy condition key constants.
CurrentTime = "aws:CurrentTime"
EpochTime = "aws:EpochTime"
MultiFactorAuthAge = "aws:MultiFactorAuthAge"
MultiFactorAuthPresent = "aws:MultiFactorAuthPresent"
Referer = "aws:Referer"
SecureTransport = "aws:SecureTransport"
SourceAccount = "aws:SourceAccount"
SourceArn = "aws:SourceArn"
SourceIp = "aws:SourceIp"
UserAgent = "aws:UserAgent"


class Action(AWSHelperFn):
    def __init__(self, prefix, action=None):
        self.prefix = prefix
        if prefix == '*' and action:
            raise ValueError("Action not supported with wildcard prefix")
        else:
            self.action = action

    def JSONrepr(self):
        if self.prefix == '*' and not self.action:
            return self.prefix
        else:
            return ''.join([self.prefix, ":", self.action])


class BaseARN(AWSHelperFn):
    def __init__(self, service, resource, region='', account=''):
        region_string = region.lower()
        if region_string.startswith("cn-"):
            aws_partition = "aws-cn"
        elif region_string.startswith("us-gov"):
            aws_partition = "aws-us-gov"
        else:
            aws_partition = "aws"

        regionless = ['iam', 's3']
        if service in regionless:
            region = ""

        self.data = "arn:%s:%s:%s:%s:%s" % (
            aws_partition, service, region, account, resource)

    def JSONrepr(self):
        return self.data


class ARN(BaseARN):
    def __init__(self, service, resource, region='', account=''):
        super(ARN, self).__init__(service, resource, region, account)
        warnings.warn('This is going away. Either use a service specific '
                      'ARN class, or use the BaseARN class.', FutureWarning)


class ConditionElement(AWSHelperFn):
    def __init__(self, data, value=None):
        """Create a ConditionElement

        There are two supported ways to create a new ConditionElement.
        For a simple key/value pair use something of the form:
            StringEquals('s3:prefix': ['', 'home/']),
        If more than one condition is needed, pass a dict:
            StringEquals({
                's3:prefix': ['', 'home/'],
                's3:delimiter': ['/'],
            }),
        """
        self.cond_dict = None
        if value is not None:
            self.key = data
            self.value = value
        else:
            self.cond_dict = data

    def get_dict(self):
        if self.cond_dict:
            return self.cond_dict
        else:
            return {self.key: self.value}


class Condition(AWSHelperFn):
    def __init__(self, conditions):
        if isinstance(conditions, ConditionElement):
            self.conditions = [conditions]
        elif isinstance(conditions, list):
            for c in conditions:
                if not isinstance(c, ConditionElement):
                    raise ValueError(
                        "ConditionElement is type %s" % (type(c),))
            self.conditions = conditions
        else:
            raise TypeError

    def JSONrepr(self):
        d = {}
        for c in self.conditions:
            d[c.condition] = c.get_dict()
        return d


class Principal(AWSHelperFn):
    VALID_PRINCIPALS = ["AWS", "CanonicalUser", "Federated", "Service"]

    def __init__(self, principal, resources=None):
        if principal == "*":
            if resources:
                raise ValueError("Cannot provide resources if principal is "
                                 "'*'.")
            self.data = "*"
        else:
            if not resources:
                raise ValueError("Must provide resources with principal.")
            if principal not in self.VALID_PRINCIPALS:
                raise ValueError("Principal must be one of: %s" % (
                    ', '.join(self.VALID_PRINCIPALS))
                )
            self.data = {principal: resources}

    def JSONrepr(self):
        return self.data


class AWSPrincipal(Principal):
    def __init__(self, principals):
        sup = super(AWSPrincipal, self)
        sup.__init__('AWS', principals)


def effect(x):
    if x not in [Allow, Deny]:
        raise ValueError(x)
    return x


class Statement(AWSProperty):
    props = {
        'Action': ([Action], False),
        'Condition': (Condition, False),
        'Effect': (effect, True),
        'NotAction': (list, False),
        'NotPrincipal': (Principal, False),
        'Principal': (Principal, False),
        'Resource': (list, False),
        'NotResource': (list, False),
        'Sid': (basestring, False),
    }


class Policy(AWSProperty):
    props = {
        'Id': (basestring, False),
        'Statement': ([Statement], True),
        'Version': (basestring, False),
    }

    def JSONrepr(self):
        return self.properties


class PolicyDocument(Policy):
    pass


_condition_strings = [
    "ArnEquals",
    "ArnNotEquals",
    "ArnLike",
    "ArnNotLike",
    "Bool",
    "DateEquals",
    "DateNotEquals",
    "DateLessThan",
    "DateLessThanEquals",
    "DateGreaterThan",
    "DateGreaterThanEquals",
    "IpAddress",
    "NotIpAddress",
    "Null",
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoreCase",
    "StringNotEqualsIgnoreCase",
    "StringLike",
    "StringNotLike",
]

_condition_qualifier_strings = [
    "ForAnyValue",
    "ForAllValues"
]


def make_condition(type_name, condition_name):
    globals()[type_name] = type(type_name, (ConditionElement,),
                                dict(condition=condition_name))
    globals()[type_name + "IfExists"] = type(type_name + "IfExists",
                                             (ConditionElement,),
                                             dict(
                                                  condition=condition_name +
                                                  "IfExists"))


# Create condition classes
for i in _condition_strings:
    make_condition(i, i)

    for qual in _condition_qualifier_strings:
        make_condition(qual+i, "%s:%s" % (qual, i))
