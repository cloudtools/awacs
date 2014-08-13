# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Mobile Analytics'
prefix = 'mobileanalytics'

PutEvents = Action(prefix, 'PutEvents')
GetReports = Action(prefix, 'GetReports')
GetFinancialReports = Action(prefix, 'GetFinancialReports')
