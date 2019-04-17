# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS App Mesh'
prefix = 'appmesh'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateMesh = Action('CreateMesh')
CreateRoute = Action('CreateRoute')
CreateVirtualNode = Action('CreateVirtualNode')
CreateVirtualRouter = Action('CreateVirtualRouter')
CreateVirtualService = Action('CreateVirtualService')
DeleteMesh = Action('DeleteMesh')
DeleteRoute = Action('DeleteRoute')
DeleteVirtualNode = Action('DeleteVirtualNode')
DeleteVirtualRouter = Action('DeleteVirtualRouter')
DeleteVirtualService = Action('DeleteVirtualService')
DescribeMesh = Action('DescribeMesh')
DescribeRoute = Action('DescribeRoute')
DescribeVirtualNode = Action('DescribeVirtualNode')
DescribeVirtualRouter = Action('DescribeVirtualRouter')
DescribeVirtualService = Action('DescribeVirtualService')
ListMeshes = Action('ListMeshes')
ListRoutes = Action('ListRoutes')
ListTagsForResource = Action('ListTagsForResource')
ListVirtualNodes = Action('ListVirtualNodes')
ListVirtualRouters = Action('ListVirtualRouters')
ListVirtualServices = Action('ListVirtualServices')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateMesh = Action('UpdateMesh')
UpdateRoute = Action('UpdateRoute')
UpdateVirtualNode = Action('UpdateVirtualNode')
UpdateVirtualRouter = Action('UpdateVirtualRouter')
UpdateVirtualService = Action('UpdateVirtualService')
