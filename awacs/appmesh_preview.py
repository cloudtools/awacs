# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS App Mesh Preview'
prefix = 'appmesh-preview'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateGatewayRoute = Action('CreateGatewayRoute')
CreateMesh = Action('CreateMesh')
CreateRoute = Action('CreateRoute')
CreateVirtualGateway = Action('CreateVirtualGateway')
CreateVirtualNode = Action('CreateVirtualNode')
CreateVirtualRouter = Action('CreateVirtualRouter')
CreateVirtualService = Action('CreateVirtualService')
DeleteGatewayRoute = Action('DeleteGatewayRoute')
DeleteMesh = Action('DeleteMesh')
DeleteRoute = Action('DeleteRoute')
DeleteVirtualGateway = Action('DeleteVirtualGateway')
DeleteVirtualNode = Action('DeleteVirtualNode')
DeleteVirtualRouter = Action('DeleteVirtualRouter')
DeleteVirtualService = Action('DeleteVirtualService')
DescribeGatewayRoute = Action('DescribeGatewayRoute')
DescribeMesh = Action('DescribeMesh')
DescribeRoute = Action('DescribeRoute')
DescribeVirtualGateway = Action('DescribeVirtualGateway')
DescribeVirtualNode = Action('DescribeVirtualNode')
DescribeVirtualRouter = Action('DescribeVirtualRouter')
DescribeVirtualService = Action('DescribeVirtualService')
ListGatewayRoutes = Action('ListGatewayRoutes')
ListMeshes = Action('ListMeshes')
ListRoutes = Action('ListRoutes')
ListVirtualGateways = Action('ListVirtualGateways')
ListVirtualNodes = Action('ListVirtualNodes')
ListVirtualRouters = Action('ListVirtualRouters')
ListVirtualServices = Action('ListVirtualServices')
StreamAggregatedResources = Action('StreamAggregatedResources')
UpdateGatewayRoute = Action('UpdateGatewayRoute')
UpdateMesh = Action('UpdateMesh')
UpdateRoute = Action('UpdateRoute')
UpdateVirtualGateway = Action('UpdateVirtualGateway')
UpdateVirtualNode = Action('UpdateVirtualNode')
UpdateVirtualRouter = Action('UpdateVirtualRouter')
UpdateVirtualService = Action('UpdateVirtualService')
