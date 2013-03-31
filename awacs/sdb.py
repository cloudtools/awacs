# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon SimpleDB'
prefix = 'sdb'

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
