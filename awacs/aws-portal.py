# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Website'
prefix = 'aws-portal'

ViewBilling = Action(prefix, 'ViewBilling')
ViewUsage = Action(prefix, 'ViewUsage')
