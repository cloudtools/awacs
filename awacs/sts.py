# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Security Token Service'
prefix = 'sts'

GetFederationToken = Action(prefix, 'GetFederationToken')
AssumeRole = Action(prefix, 'AssumeRole')
