# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
from . import AWSHelperFn, AWSProperty, awsencode


# Policy effect constants.
Allow = "Allow"
Deny = "Deny"

# Policy principal constants.
Everybody = "*"

# Policy condition key constants.
CurrentTime = "aws:CurrentTime"
EpochTime = "aws:EpochTime"
MultiFactorAuthAge = "aws:MultiFactorAuthAge"
Referer = "aws:Referer"
SecureTransport = "aws:SecureTransport"
SourceArn = "aws:SourceArn"
SourceIp = "aws:SourceIp"
UserAgent = "aws:UserAgent"


class Action(AWSHelperFn):
    def __init__(self, prefix, action):
        self.prefix = prefix
        self.action = action

    def JSONrepr(self):
        return ''.join([self.prefix, ":", self.action])


class ARN(AWSHelperFn):
    def __init__(self, service, resource, region='', account=''):
        self.data = "arn:aws:%s:%s:%s:%s" % (
            service, region, account, resource)

    def JSONrepr(self):
        return self.data


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
    def __init__(self, principal, resources):
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

    def to_json(self, indent=4, sort_keys=True):
        p = self.properties
        return json.dumps(p, cls=awsencode, indent=indent, sort_keys=sort_keys)

    def JSONrepr(self):
        return self.properties


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
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoresCase",
    "StringLike",
    "StringNotLike",
]

# Create condition classes
for i in _condition_strings:
    globals()[i] = type(i, (ConditionElement,), dict(condition=i))
    i = i + "IfExists"
    globals()[i] = type(i, (ConditionElement,), dict(condition=i))
