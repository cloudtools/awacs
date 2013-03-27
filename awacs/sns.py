# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action, ARN


# SNS policy condition key constants.
EndPoint = "sns:EndPoint"
Protocol = "sns:Protocol"

# SNS policy action constants.
AddPermission = Action("sns:AddPermission")
DeleteTopic = Action("sns:DeleteTopic")
GetTopicAttributes = Action("sns:GetTopicAttributes")
ListSubscriptionsByTopic = Action("sns:ListSubscriptionsByTopic")
Publish = Action("sns:Publish")
Receive = Action("sns:Receive")
RemovePermission = Action("sns:RemovePermission")
SetTopicAttributes = Action("sns:SetTopicAttributes")
Subscribe = Action("sns:Subscribe")


class SNS_ARN(ARN):
    def __init__(self, region, account, data):
        sup = super(SNS_ARN, self)
        sup.__init__('sns', region, account, data)
