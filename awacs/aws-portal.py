# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Billing'
prefix = 'aws-portal'

ModifyAccount = Action(prefix, 'ModifyAccount')
ModifyBilling = Action(prefix, 'ModifyBilling')
ModifyPaymentMethods = Action(prefix, 'ModifyPaymentMethods')
ViewAccount = Action(prefix, 'ViewAccount')
ViewBilling = Action(prefix, 'ViewBilling')
ViewPaymentMethods = Action(prefix, 'ViewPaymentMethods')
ViewUsage = Action(prefix, 'ViewUsage')
