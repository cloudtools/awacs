# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Cloud Map"
prefix = "servicediscovery"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateHttpNamespace = Action("CreateHttpNamespace")
CreatePrivateDnsNamespace = Action("CreatePrivateDnsNamespace")
CreatePublicDnsNamespace = Action("CreatePublicDnsNamespace")
CreateService = Action("CreateService")
DeleteNamespace = Action("DeleteNamespace")
DeleteService = Action("DeleteService")
DeleteServiceAttributes = Action("DeleteServiceAttributes")
DeregisterInstance = Action("DeregisterInstance")
DiscoverInstances = Action("DiscoverInstances")
DiscoverInstancesRevision = Action("DiscoverInstancesRevision")
GetInstance = Action("GetInstance")
GetInstancesHealthStatus = Action("GetInstancesHealthStatus")
GetNamespace = Action("GetNamespace")
GetOperation = Action("GetOperation")
GetService = Action("GetService")
GetServiceAttributes = Action("GetServiceAttributes")
ListInstances = Action("ListInstances")
ListNamespaces = Action("ListNamespaces")
ListOperations = Action("ListOperations")
ListServices = Action("ListServices")
ListTagsForResource = Action("ListTagsForResource")
RegisterInstance = Action("RegisterInstance")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateHttpNamespace = Action("UpdateHttpNamespace")
UpdateInstanceCustomHealthStatus = Action("UpdateInstanceCustomHealthStatus")
UpdateInstanceHeartbeatStatus = Action("UpdateInstanceHeartbeatStatus")
UpdatePrivateDnsNamespace = Action("UpdatePrivateDnsNamespace")
UpdatePublicDnsNamespace = Action("UpdatePublicDnsNamespace")
UpdateService = Action("UpdateService")
UpdateServiceAttributes = Action("UpdateServiceAttributes")
