# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import warnings

from aws import Action, BaseARN

service_name = 'Amazon SimpleDB'
prefix = 'sdb'


class ARN(BaseARN):
    def __init__(self, region, account, domain=None):
        sup = super(ARN, self)
        resource = '*'
        if domain:
            resource = 'domain/' + domain
        sup.__init__(prefix, region=region, account=account, resource=resource)


class SDB_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(SDB_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use sdb.ARN instead.",
                      FutureWarning)


BatchDeleteAttributes = Action(prefix, 'BatchDeleteAttributes')
BatchPutAttributes = Action(prefix, 'BatchPutAttributes')
CreateDomain = Action(prefix, 'CreateDomain')
DeleteAttributes = Action(prefix, 'DeleteAttributes')
DeleteDomain = Action(prefix, 'DeleteDomain')
DomainMetadata = Action(prefix, 'DomainMetadata')
GetAttributes = Action(prefix, 'GetAttributes')
ListDomains = Action(prefix, 'ListDomains')
PutAttributes = Action(prefix, 'PutAttributes')
Select = Action(prefix, 'Select')
