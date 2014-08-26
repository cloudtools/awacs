# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS CloudTrail'
prefix = 'cloudtrail'

CreateTrail = Action(prefix, 'CreateTrail')
DeleteTrail = Action(prefix, 'DeleteTrail')
DescribeTrails = Action(prefix, 'DescribeTrails')
GetTrailStatus = Action(prefix, 'GetTrailStatus')
StartLogging = Action(prefix, 'StartLogging')
StopLogging = Action(prefix, 'StopLogging')
UpdateTrail = Action(prefix, 'UpdateTrail')
