# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Import Export'
prefix = 'importexport'

CreateJob = Action(prefix, 'CreateJob')
UpdateJob = Action(prefix, 'UpdateJob')
CancelJob = Action(prefix, 'CancelJob')
ListJobs = Action(prefix, 'ListJobs')
GetStatus = Action(prefix, 'GetStatus')
