# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = 'AWS Billing'
prefix = 'aws-portal'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


ModifyAccount = Action('ModifyAccount')
ModifyBilling = Action('ModifyBilling')
ModifyPaymentMethods = Action('ModifyPaymentMethods')
ViewAccount = Action('ViewAccount')
ViewBilling = Action('ViewBilling')
ViewPaymentMethods = Action('ViewPaymentMethods')
ViewUsage = Action('ViewUsage')
