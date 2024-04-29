# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS App Mesh"
prefix = "appmesh"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateGatewayRoute = Action("CreateGatewayRoute")
CreateMesh = Action("CreateMesh")
CreateRoute = Action("CreateRoute")
CreateVirtualGateway = Action("CreateVirtualGateway")
CreateVirtualNode = Action("CreateVirtualNode")
CreateVirtualRouter = Action("CreateVirtualRouter")
CreateVirtualService = Action("CreateVirtualService")
DeleteGatewayRoute = Action("DeleteGatewayRoute")
DeleteMesh = Action("DeleteMesh")
DeleteMeshPolicy = Action("DeleteMeshPolicy")
DeleteRoute = Action("DeleteRoute")
DeleteVirtualGateway = Action("DeleteVirtualGateway")
DeleteVirtualNode = Action("DeleteVirtualNode")
DeleteVirtualRouter = Action("DeleteVirtualRouter")
DeleteVirtualService = Action("DeleteVirtualService")
DescribeGatewayRoute = Action("DescribeGatewayRoute")
DescribeMesh = Action("DescribeMesh")
DescribeRoute = Action("DescribeRoute")
DescribeVirtualGateway = Action("DescribeVirtualGateway")
DescribeVirtualNode = Action("DescribeVirtualNode")
DescribeVirtualRouter = Action("DescribeVirtualRouter")
DescribeVirtualService = Action("DescribeVirtualService")
GetMeshPolicy = Action("GetMeshPolicy")
ListGatewayRoutes = Action("ListGatewayRoutes")
ListMeshes = Action("ListMeshes")
ListRoutes = Action("ListRoutes")
ListTagsForResource = Action("ListTagsForResource")
ListVirtualGateways = Action("ListVirtualGateways")
ListVirtualNodes = Action("ListVirtualNodes")
ListVirtualRouters = Action("ListVirtualRouters")
ListVirtualServices = Action("ListVirtualServices")
PutMeshPolicy = Action("PutMeshPolicy")
StreamAggregatedResources = Action("StreamAggregatedResources")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateGatewayRoute = Action("UpdateGatewayRoute")
UpdateMesh = Action("UpdateMesh")
UpdateRoute = Action("UpdateRoute")
UpdateVirtualGateway = Action("UpdateVirtualGateway")
UpdateVirtualNode = Action("UpdateVirtualNode")
UpdateVirtualRouter = Action("UpdateVirtualRouter")
UpdateVirtualService = Action("UpdateVirtualService")
