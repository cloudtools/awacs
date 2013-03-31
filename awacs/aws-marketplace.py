# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Marketplace'
prefix = 'aws-marketplace'

Subscribe = Action(prefix, 'Subscribe')
Unsubscribe = Action(prefix, 'Unsubscribe')
ViewSubscriptions = Action(prefix, 'ViewSubscriptions')
