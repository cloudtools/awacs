# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional, Union

from . import AWSHelperFn, AWSProperty

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore[assignment]

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
PrincipalArn = "aws:PrincipalArn"
PrincipalOrgID = "aws:PrincipalOrgID"
PrincipalType = "aws:PrincipalType"
Referer = "aws:Referer"
RequestedRegion = "aws:RequestedRegion"
SecureTransport = "aws:SecureTransport"
SourceAccount = "aws:SourceAccount"
SourceArn = "aws:SourceArn"
SourceIp = "aws:SourceIp"
SourceVpc = "aws:SourceVpc"
SourceVpce = "aws:SourceVpce"
TagKeys = "aws:TagKeys"
TokenIssueTime = "aws:TokenIssueTime"
UserAgent = "aws:UserAgent"
userid = "aws:userid"
username = "aws:username"
VpcSourceIp = "aws:VpcSourceIp"


class Action(AWSHelperFn):
    def __init__(self, prefix: str, action: Optional[str] = None) -> None:
        self.prefix = prefix
        if prefix == "*" and action:
            raise ValueError("Action not supported with wildcard prefix")
        else:
            self.action = action

    def JSONrepr(self) -> str:
        if self.prefix == "*" or not self.action:
            return self.prefix
        else:
            return "".join([self.prefix, ":", self.action])


class BaseARN(AWSHelperFn):
    def __init__(
        self, service: str, resource: str, region: str = "", account: str = ""
    ) -> None:
        region_string = region.lower()
        if region == "${AWS::Region}":
            aws_partition = "${AWS::Partition}"
        elif region_string.startswith("cn-"):
            aws_partition = "aws-cn"
        elif region_string.startswith("us-gov"):
            aws_partition = "aws-us-gov"
        else:
            aws_partition = "aws"

        if service == "iam":
            region = ""
        elif service == "s3" and not resource.startswith(
            ("accesspoint/", "job/", "storage-lens/")
        ):
            region = ""

        self.data = "arn:%s:%s:%s:%s:%s" % (
            aws_partition,
            service,
            region,
            account,
            resource,
        )

    def JSONrepr(self) -> str:
        return self.data


class ConditionElement(AWSHelperFn, metaclass=ABCMeta):
    def __init__(self, data: Union[str, dict], value: Optional[Any] = None) -> None:
        """Create a ConditionElement

        There are two supported ways to create a new ConditionElement.
        For a simple key/value pair use something of the form:
            StringEquals('s3:prefix', ['', 'home/']),
        If more than one condition is needed, pass a dict:
            StringEquals({
                's3:prefix': ['', 'home/'],
                's3:delimiter': ['/'],
            }),
        """
        self.cond_dict: Optional[dict] = None
        if value is not None:
            self.key = data
            self.value = value
        else:
            assert isinstance(data, dict)
            self.cond_dict = data

    def get_dict(self) -> dict:
        if self.cond_dict:
            return self.cond_dict
        else:
            return {self.key: self.value}

    @property
    @abstractmethod
    def condition(self) -> str:
        raise NotImplementedError


class Condition(AWSHelperFn):
    def __init__(
        self, conditions: Union[ConditionElement, List[ConditionElement]]
    ) -> None:
        if isinstance(conditions, ConditionElement):
            self.conditions = [conditions]
        elif isinstance(conditions, list):
            for c in conditions:
                if not isinstance(c, ConditionElement):
                    raise ValueError("ConditionElement is type %s" % (type(c),))
            self.conditions = conditions
        else:
            raise TypeError

    def JSONrepr(self) -> dict:
        d = {}
        for c in self.conditions:
            d[c.condition] = c.get_dict()
        return d


class Principal(AWSHelperFn):
    data: Union[Literal["*"], Dict[str, Any]]
    VALID_PRINCIPALS = ["AWS", "CanonicalUser", "Federated", "Service"]

    def __init__(self, principal: str, resources: Optional[Any] = None) -> None:
        if principal == "*":
            if resources:
                raise ValueError("Cannot provide resources if principal is " "'*'.")
            self.data = "*"
        else:
            if not resources:
                raise ValueError("Must provide resources with principal.")
            if principal not in self.VALID_PRINCIPALS:
                raise ValueError(
                    "Principal must be one of: %s" % (", ".join(self.VALID_PRINCIPALS))
                )
            self.data = {principal: resources}

    def JSONrepr(self) -> Union[Literal["*"], Dict[str, Any]]:
        return self.data


class AWSPrincipal(Principal):
    def __init__(self, principals: Any) -> None:
        super().__init__("AWS", principals)


def effect(x: str) -> str:
    if x not in [Allow, Deny]:
        raise ValueError(x)
    return x


class Statement(AWSProperty):
    props = {
        "Action": ([Action], False),
        "Condition": (Condition, False),
        "Effect": (effect, True),
        "NotAction": (list, False),
        "NotPrincipal": (Principal, False),
        "Principal": (Principal, False),
        "Resource": (list, False),
        "NotResource": (list, False),
        "Sid": (str, False),
    }


class Policy(AWSProperty):
    props = {
        "Id": (str, False),
        "Statement": ([Statement], True),
        "Version": (str, False),
    }

    def JSONrepr(self) -> dict:
        return self.properties


class PolicyDocument(Policy):
    pass


# Generated Conditions


class ArnEquals(ConditionElement):
    condition = "ArnEquals"


class ArnEqualsIfExists(ConditionElement):
    condition = "ArnEqualsIfExists"


class ForAnyValueArnEquals(ConditionElement):
    condition = "ForAnyValue:ArnEquals"


class ForAnyValueArnEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:ArnEqualsIfExists"


class ForAllValuesArnEquals(ConditionElement):
    condition = "ForAllValues:ArnEquals"


class ForAllValuesArnEqualsIfExists(ConditionElement):
    condition = "ForAllValues:ArnEqualsIfExists"


class ArnNotEquals(ConditionElement):
    condition = "ArnNotEquals"


class ArnNotEqualsIfExists(ConditionElement):
    condition = "ArnNotEqualsIfExists"


class ForAnyValueArnNotEquals(ConditionElement):
    condition = "ForAnyValue:ArnNotEquals"


class ForAnyValueArnNotEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:ArnNotEqualsIfExists"


class ForAllValuesArnNotEquals(ConditionElement):
    condition = "ForAllValues:ArnNotEquals"


class ForAllValuesArnNotEqualsIfExists(ConditionElement):
    condition = "ForAllValues:ArnNotEqualsIfExists"


class ArnLike(ConditionElement):
    condition = "ArnLike"


class ArnLikeIfExists(ConditionElement):
    condition = "ArnLikeIfExists"


class ForAnyValueArnLike(ConditionElement):
    condition = "ForAnyValue:ArnLike"


class ForAnyValueArnLikeIfExists(ConditionElement):
    condition = "ForAnyValue:ArnLikeIfExists"


class ForAllValuesArnLike(ConditionElement):
    condition = "ForAllValues:ArnLike"


class ForAllValuesArnLikeIfExists(ConditionElement):
    condition = "ForAllValues:ArnLikeIfExists"


class ArnNotLike(ConditionElement):
    condition = "ArnNotLike"


class ArnNotLikeIfExists(ConditionElement):
    condition = "ArnNotLikeIfExists"


class ForAnyValueArnNotLike(ConditionElement):
    condition = "ForAnyValue:ArnNotLike"


class ForAnyValueArnNotLikeIfExists(ConditionElement):
    condition = "ForAnyValue:ArnNotLikeIfExists"


class ForAllValuesArnNotLike(ConditionElement):
    condition = "ForAllValues:ArnNotLike"


class ForAllValuesArnNotLikeIfExists(ConditionElement):
    condition = "ForAllValues:ArnNotLikeIfExists"


class Bool(ConditionElement):
    condition = "Bool"


class BoolIfExists(ConditionElement):
    condition = "BoolIfExists"


class ForAnyValueBool(ConditionElement):
    condition = "ForAnyValue:Bool"


class ForAnyValueBoolIfExists(ConditionElement):
    condition = "ForAnyValue:BoolIfExists"


class ForAllValuesBool(ConditionElement):
    condition = "ForAllValues:Bool"


class ForAllValuesBoolIfExists(ConditionElement):
    condition = "ForAllValues:BoolIfExists"


class DateEquals(ConditionElement):
    condition = "DateEquals"


class DateEqualsIfExists(ConditionElement):
    condition = "DateEqualsIfExists"


class ForAnyValueDateEquals(ConditionElement):
    condition = "ForAnyValue:DateEquals"


class ForAnyValueDateEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:DateEqualsIfExists"


class ForAllValuesDateEquals(ConditionElement):
    condition = "ForAllValues:DateEquals"


class ForAllValuesDateEqualsIfExists(ConditionElement):
    condition = "ForAllValues:DateEqualsIfExists"


class DateNotEquals(ConditionElement):
    condition = "DateNotEquals"


class DateNotEqualsIfExists(ConditionElement):
    condition = "DateNotEqualsIfExists"


class ForAnyValueDateNotEquals(ConditionElement):
    condition = "ForAnyValue:DateNotEquals"


class ForAnyValueDateNotEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:DateNotEqualsIfExists"


class ForAllValuesDateNotEquals(ConditionElement):
    condition = "ForAllValues:DateNotEquals"


class ForAllValuesDateNotEqualsIfExists(ConditionElement):
    condition = "ForAllValues:DateNotEqualsIfExists"


class DateLessThan(ConditionElement):
    condition = "DateLessThan"


class DateLessThanIfExists(ConditionElement):
    condition = "DateLessThanIfExists"


class ForAnyValueDateLessThan(ConditionElement):
    condition = "ForAnyValue:DateLessThan"


class ForAnyValueDateLessThanIfExists(ConditionElement):
    condition = "ForAnyValue:DateLessThanIfExists"


class ForAllValuesDateLessThan(ConditionElement):
    condition = "ForAllValues:DateLessThan"


class ForAllValuesDateLessThanIfExists(ConditionElement):
    condition = "ForAllValues:DateLessThanIfExists"


class DateLessThanEquals(ConditionElement):
    condition = "DateLessThanEquals"


class DateLessThanEqualsIfExists(ConditionElement):
    condition = "DateLessThanEqualsIfExists"


class ForAnyValueDateLessThanEquals(ConditionElement):
    condition = "ForAnyValue:DateLessThanEquals"


class ForAnyValueDateLessThanEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:DateLessThanEqualsIfExists"


class ForAllValuesDateLessThanEquals(ConditionElement):
    condition = "ForAllValues:DateLessThanEquals"


class ForAllValuesDateLessThanEqualsIfExists(ConditionElement):
    condition = "ForAllValues:DateLessThanEqualsIfExists"


class DateGreaterThan(ConditionElement):
    condition = "DateGreaterThan"


class DateGreaterThanIfExists(ConditionElement):
    condition = "DateGreaterThanIfExists"


class ForAnyValueDateGreaterThan(ConditionElement):
    condition = "ForAnyValue:DateGreaterThan"


class ForAnyValueDateGreaterThanIfExists(ConditionElement):
    condition = "ForAnyValue:DateGreaterThanIfExists"


class ForAllValuesDateGreaterThan(ConditionElement):
    condition = "ForAllValues:DateGreaterThan"


class ForAllValuesDateGreaterThanIfExists(ConditionElement):
    condition = "ForAllValues:DateGreaterThanIfExists"


class DateGreaterThanEquals(ConditionElement):
    condition = "DateGreaterThanEquals"


class DateGreaterThanEqualsIfExists(ConditionElement):
    condition = "DateGreaterThanEqualsIfExists"


class ForAnyValueDateGreaterThanEquals(ConditionElement):
    condition = "ForAnyValue:DateGreaterThanEquals"


class ForAnyValueDateGreaterThanEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:DateGreaterThanEqualsIfExists"


class ForAllValuesDateGreaterThanEquals(ConditionElement):
    condition = "ForAllValues:DateGreaterThanEquals"


class ForAllValuesDateGreaterThanEqualsIfExists(ConditionElement):
    condition = "ForAllValues:DateGreaterThanEqualsIfExists"


class IpAddress(ConditionElement):
    condition = "IpAddress"


class IpAddressIfExists(ConditionElement):
    condition = "IpAddressIfExists"


class ForAnyValueIpAddress(ConditionElement):
    condition = "ForAnyValue:IpAddress"


class ForAnyValueIpAddressIfExists(ConditionElement):
    condition = "ForAnyValue:IpAddressIfExists"


class ForAllValuesIpAddress(ConditionElement):
    condition = "ForAllValues:IpAddress"


class ForAllValuesIpAddressIfExists(ConditionElement):
    condition = "ForAllValues:IpAddressIfExists"


class NotIpAddress(ConditionElement):
    condition = "NotIpAddress"


class NotIpAddressIfExists(ConditionElement):
    condition = "NotIpAddressIfExists"


class ForAnyValueNotIpAddress(ConditionElement):
    condition = "ForAnyValue:NotIpAddress"


class ForAnyValueNotIpAddressIfExists(ConditionElement):
    condition = "ForAnyValue:NotIpAddressIfExists"


class ForAllValuesNotIpAddress(ConditionElement):
    condition = "ForAllValues:NotIpAddress"


class ForAllValuesNotIpAddressIfExists(ConditionElement):
    condition = "ForAllValues:NotIpAddressIfExists"


class Null(ConditionElement):
    condition = "Null"


class NullIfExists(ConditionElement):
    condition = "NullIfExists"


class ForAnyValueNull(ConditionElement):
    condition = "ForAnyValue:Null"


class ForAnyValueNullIfExists(ConditionElement):
    condition = "ForAnyValue:NullIfExists"


class ForAllValuesNull(ConditionElement):
    condition = "ForAllValues:Null"


class ForAllValuesNullIfExists(ConditionElement):
    condition = "ForAllValues:NullIfExists"


class NumericEquals(ConditionElement):
    condition = "NumericEquals"


class NumericEqualsIfExists(ConditionElement):
    condition = "NumericEqualsIfExists"


class ForAnyValueNumericEquals(ConditionElement):
    condition = "ForAnyValue:NumericEquals"


class ForAnyValueNumericEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:NumericEqualsIfExists"


class ForAllValuesNumericEquals(ConditionElement):
    condition = "ForAllValues:NumericEquals"


class ForAllValuesNumericEqualsIfExists(ConditionElement):
    condition = "ForAllValues:NumericEqualsIfExists"


class NumericNotEquals(ConditionElement):
    condition = "NumericNotEquals"


class NumericNotEqualsIfExists(ConditionElement):
    condition = "NumericNotEqualsIfExists"


class ForAnyValueNumericNotEquals(ConditionElement):
    condition = "ForAnyValue:NumericNotEquals"


class ForAnyValueNumericNotEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:NumericNotEqualsIfExists"


class ForAllValuesNumericNotEquals(ConditionElement):
    condition = "ForAllValues:NumericNotEquals"


class ForAllValuesNumericNotEqualsIfExists(ConditionElement):
    condition = "ForAllValues:NumericNotEqualsIfExists"


class NumericLessThan(ConditionElement):
    condition = "NumericLessThan"


class NumericLessThanIfExists(ConditionElement):
    condition = "NumericLessThanIfExists"


class ForAnyValueNumericLessThan(ConditionElement):
    condition = "ForAnyValue:NumericLessThan"


class ForAnyValueNumericLessThanIfExists(ConditionElement):
    condition = "ForAnyValue:NumericLessThanIfExists"


class ForAllValuesNumericLessThan(ConditionElement):
    condition = "ForAllValues:NumericLessThan"


class ForAllValuesNumericLessThanIfExists(ConditionElement):
    condition = "ForAllValues:NumericLessThanIfExists"


class NumericLessThanEquals(ConditionElement):
    condition = "NumericLessThanEquals"


class NumericLessThanEqualsIfExists(ConditionElement):
    condition = "NumericLessThanEqualsIfExists"


class ForAnyValueNumericLessThanEquals(ConditionElement):
    condition = "ForAnyValue:NumericLessThanEquals"


class ForAnyValueNumericLessThanEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:NumericLessThanEqualsIfExists"


class ForAllValuesNumericLessThanEquals(ConditionElement):
    condition = "ForAllValues:NumericLessThanEquals"


class ForAllValuesNumericLessThanEqualsIfExists(ConditionElement):
    condition = "ForAllValues:NumericLessThanEqualsIfExists"


class NumericGreaterThan(ConditionElement):
    condition = "NumericGreaterThan"


class NumericGreaterThanIfExists(ConditionElement):
    condition = "NumericGreaterThanIfExists"


class ForAnyValueNumericGreaterThan(ConditionElement):
    condition = "ForAnyValue:NumericGreaterThan"


class ForAnyValueNumericGreaterThanIfExists(ConditionElement):
    condition = "ForAnyValue:NumericGreaterThanIfExists"


class ForAllValuesNumericGreaterThan(ConditionElement):
    condition = "ForAllValues:NumericGreaterThan"


class ForAllValuesNumericGreaterThanIfExists(ConditionElement):
    condition = "ForAllValues:NumericGreaterThanIfExists"


class NumericGreaterThanEquals(ConditionElement):
    condition = "NumericGreaterThanEquals"


class NumericGreaterThanEqualsIfExists(ConditionElement):
    condition = "NumericGreaterThanEqualsIfExists"


class ForAnyValueNumericGreaterThanEquals(ConditionElement):
    condition = "ForAnyValue:NumericGreaterThanEquals"


class ForAnyValueNumericGreaterThanEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:NumericGreaterThanEqualsIfExists"


class ForAllValuesNumericGreaterThanEquals(ConditionElement):
    condition = "ForAllValues:NumericGreaterThanEquals"


class ForAllValuesNumericGreaterThanEqualsIfExists(ConditionElement):
    condition = "ForAllValues:NumericGreaterThanEqualsIfExists"


class StringEquals(ConditionElement):
    condition = "StringEquals"


class StringEqualsIfExists(ConditionElement):
    condition = "StringEqualsIfExists"


class ForAnyValueStringEquals(ConditionElement):
    condition = "ForAnyValue:StringEquals"


class ForAnyValueStringEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:StringEqualsIfExists"


class ForAllValuesStringEquals(ConditionElement):
    condition = "ForAllValues:StringEquals"


class ForAllValuesStringEqualsIfExists(ConditionElement):
    condition = "ForAllValues:StringEqualsIfExists"


class StringNotEquals(ConditionElement):
    condition = "StringNotEquals"


class StringNotEqualsIfExists(ConditionElement):
    condition = "StringNotEqualsIfExists"


class ForAnyValueStringNotEquals(ConditionElement):
    condition = "ForAnyValue:StringNotEquals"


class ForAnyValueStringNotEqualsIfExists(ConditionElement):
    condition = "ForAnyValue:StringNotEqualsIfExists"


class ForAllValuesStringNotEquals(ConditionElement):
    condition = "ForAllValues:StringNotEquals"


class ForAllValuesStringNotEqualsIfExists(ConditionElement):
    condition = "ForAllValues:StringNotEqualsIfExists"


class StringEqualsIgnoreCase(ConditionElement):
    condition = "StringEqualsIgnoreCase"


class StringEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "StringEqualsIgnoreCaseIfExists"


class ForAnyValueStringEqualsIgnoreCase(ConditionElement):
    condition = "ForAnyValue:StringEqualsIgnoreCase"


class ForAnyValueStringEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "ForAnyValue:StringEqualsIgnoreCaseIfExists"


class ForAllValuesStringEqualsIgnoreCase(ConditionElement):
    condition = "ForAllValues:StringEqualsIgnoreCase"


class ForAllValuesStringEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "ForAllValues:StringEqualsIgnoreCaseIfExists"


class StringNotEqualsIgnoreCase(ConditionElement):
    condition = "StringNotEqualsIgnoreCase"


class StringNotEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "StringNotEqualsIgnoreCaseIfExists"


class ForAnyValueStringNotEqualsIgnoreCase(ConditionElement):
    condition = "ForAnyValue:StringNotEqualsIgnoreCase"


class ForAnyValueStringNotEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "ForAnyValue:StringNotEqualsIgnoreCaseIfExists"


class ForAllValuesStringNotEqualsIgnoreCase(ConditionElement):
    condition = "ForAllValues:StringNotEqualsIgnoreCase"


class ForAllValuesStringNotEqualsIgnoreCaseIfExists(ConditionElement):
    condition = "ForAllValues:StringNotEqualsIgnoreCaseIfExists"


class StringLike(ConditionElement):
    condition = "StringLike"


class StringLikeIfExists(ConditionElement):
    condition = "StringLikeIfExists"


class ForAnyValueStringLike(ConditionElement):
    condition = "ForAnyValue:StringLike"


class ForAnyValueStringLikeIfExists(ConditionElement):
    condition = "ForAnyValue:StringLikeIfExists"


class ForAllValuesStringLike(ConditionElement):
    condition = "ForAllValues:StringLike"


class ForAllValuesStringLikeIfExists(ConditionElement):
    condition = "ForAllValues:StringLikeIfExists"


class StringNotLike(ConditionElement):
    condition = "StringNotLike"


class StringNotLikeIfExists(ConditionElement):
    condition = "StringNotLikeIfExists"


class ForAnyValueStringNotLike(ConditionElement):
    condition = "ForAnyValue:StringNotLike"


class ForAnyValueStringNotLikeIfExists(ConditionElement):
    condition = "ForAnyValue:StringNotLikeIfExists"


class ForAllValuesStringNotLike(ConditionElement):
    condition = "ForAllValues:StringNotLike"


class ForAllValuesStringNotLikeIfExists(ConditionElement):
    condition = "ForAllValues:StringNotLikeIfExists"
