import warnings
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SimpleDB'
prefix = 'sdb'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class SDB_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(SDB_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use sdb.ARN instead.",
                      FutureWarning)


BatchDeleteAttributes = Action('BatchDeleteAttributes')
BatchPutAttributes = Action('BatchPutAttributes')
CreateDomain = Action('CreateDomain')
DeleteAttributes = Action('DeleteAttributes')
DeleteDomain = Action('DeleteDomain')
DomainMetadata = Action('DomainMetadata')
GetAttributes = Action('GetAttributes')
ListDomains = Action('ListDomains')
PutAttributes = Action('PutAttributes')
Select = Action('Select')
