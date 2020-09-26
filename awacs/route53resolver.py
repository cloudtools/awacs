# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Route 53 Resolver'
prefix = 'route53resolver'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateResolverEndpointIpAddress = \
    Action('AssociateResolverEndpointIpAddress')
AssociateResolverQueryLogConfig = \
    Action('AssociateResolverQueryLogConfig')
AssociateResolverRule = Action('AssociateResolverRule')
CreateResolverEndpoint = Action('CreateResolverEndpoint')
CreateResolverQueryLogConfig = Action('CreateResolverQueryLogConfig')
CreateResolverRule = Action('CreateResolverRule')
DeleteResolverEndpoint = Action('DeleteResolverEndpoint')
DeleteResolverQueryLogConfig = Action('DeleteResolverQueryLogConfig')
DeleteResolverRule = Action('DeleteResolverRule')
DisassociateResolverEndpointIpAddress = \
    Action('DisassociateResolverEndpointIpAddress')
DisassociateResolverQueryLogConfig = \
    Action('DisassociateResolverQueryLogConfig')
DisassociateResolverRule = Action('DisassociateResolverRule')
GetResolverEndpoint = Action('GetResolverEndpoint')
GetResolverQueryLogConfig = Action('GetResolverQueryLogConfig')
GetResolverQueryLogConfigAssociation = \
    Action('GetResolverQueryLogConfigAssociation')
GetResolverQueryLogConfigPolicy = \
    Action('GetResolverQueryLogConfigPolicy')
GetResolverRule = Action('GetResolverRule')
GetResolverRuleAssociation = Action('GetResolverRuleAssociation')
GetResolverRulePolicy = Action('GetResolverRulePolicy')
ListResolverEndpointIpAddresses = \
    Action('ListResolverEndpointIpAddresses')
ListResolverEndpoints = Action('ListResolverEndpoints')
ListResolverQueryLogConfigAssociations = \
    Action('ListResolverQueryLogConfigAssociations')
ListResolverQueryLogConfigs = Action('ListResolverQueryLogConfigs')
ListResolverRuleAssociations = Action('ListResolverRuleAssociations')
ListResolverRules = Action('ListResolverRules')
ListTagsForResource = Action('ListTagsForResource')
PutResolverQueryLogConfigPolicy = \
    Action('PutResolverQueryLogConfigPolicy')
PutResolverRulePolicy = Action('PutResolverRulePolicy')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateResolverEndpoint = Action('UpdateResolverEndpoint')
UpdateResolverRule = Action('UpdateResolverRule')
