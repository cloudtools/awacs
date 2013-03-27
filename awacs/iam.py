# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import ARN


class IAM_ARN(ARN):
    def __init__(self, region, account, data):
        sup = super(IAM_ARN, self)
        sup.__init__('iam', region, account, data)
