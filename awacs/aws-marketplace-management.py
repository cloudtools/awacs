# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'AWS Marketplace Management Portal'
prefix = 'aws-marketplace-management'

uploadFiles = Action(prefix, 'uploadFiles')
viewMarketing = Action(prefix, 'viewMarketing')
viewReports = Action(prefix, 'viewReports')
viewSupport = Action(prefix, 'viewSupport')
