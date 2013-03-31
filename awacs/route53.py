# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Route 53'
prefix = 'route53'

ChangeResourceRecordSets = Action(prefix, 'ChangeResourceRecordSets')
CreateHostedZone = Action(prefix, 'CreateHostedZone')
DeleteHostedZone = Action(prefix, 'DeleteHostedZone')
GetChange = Action(prefix, 'GetChange')
GetHostedZone = Action(prefix, 'GetHostedZone')
ListHostedZones = Action(prefix, 'ListHostedZones')
ListResourceRecordSets = Action(prefix, 'ListResourceRecordSets')
