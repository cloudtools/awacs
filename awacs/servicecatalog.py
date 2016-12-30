# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Service Catalog'
prefix = 'servicecatalog'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AcceptPortfolioShare = Action('AcceptPortfolioShare')
AssociatePrincipalWithPortfolio = \
    Action('AssociatePrincipalWithPortfolio')
AssociateProductWithPortfolio = Action('AssociateProductWithPortfolio')
CreateConstraint = Action('CreateConstraint')
CreatePortfolio = Action('CreatePortfolio')
CreatePortfolioShare = Action('CreatePortfolioShare')
CreateProduct = Action('CreateProduct')
CreateProvisioningArtifact = Action('CreateProvisioningArtifact')
DeleteConstraint = Action('DeleteConstraint')
DeletePortfolio = Action('DeletePortfolio')
DeletePortfolioShare = Action('DeletePortfolioShare')
DeleteProduct = Action('DeleteProduct')
DeleteProvisioningArtifact = Action('DeleteProvisioningArtifact')
DescribeConstraint = Action('DescribeConstraint')
DescribePortfolio = Action('DescribePortfolio')
DescribeProduct = Action('DescribeProduct')
DescribeProductAsAdmin = Action('DescribeProductAsAdmin')
DescribeProductView = Action('DescribeProductView')
DescribeProvisioningArtifact = Action('DescribeProvisioningArtifact')
DescribeProvisioningParameters = Action('DescribeProvisioningParameters')
DescribeRecord = Action('DescribeRecord')
DisassociatePrincipalFromPortfolio = \
    Action('DisassociatePrincipalFromPortfolio')
DisassociateProductFromPortfolio = \
    Action('DisassociateProductFromPortfolio')
ListAcceptedPortfolioShares = Action('ListAcceptedPortfolioShares')
ListConstraintsForPortfolio = Action('ListConstraintsForPortfolio')
ListLaunchPaths = Action('ListLaunchPaths')
ListPortfolioAccess = Action('ListPortfolioAccess')
ListPortfolios = Action('ListPortfolios')
ListPortfoliosForProduct = Action('ListPortfoliosForProduct')
ListPrincipalsForPortfolio = Action('ListPrincipalsForPortfolio')
ListProvisioningArtifacts = Action('ListProvisioningArtifacts')
ListRecordHistory = Action('ListRecordHistory')
ProvisionProduct = Action('ProvisionProduct')
RejectPortfolioShare = Action('RejectPortfolioShare')
ScanProvisionedProducts = Action('ScanProvisionedProducts')
SearchProducts = Action('SearchProducts')
SearchProductsAsAdmin = Action('SearchProductsAsAdmin')
TerminateProvisionedProduct = Action('TerminateProvisionedProduct')
UpdateConstraint = Action('UpdateConstraint')
UpdatePortfolio = Action('UpdatePortfolio')
UpdateProduct = Action('UpdateProduct')
UpdateProvisionedProduct = Action('UpdateProvisionedProduct')
UpdateProvisioningArtifact = Action('UpdateProvisioningArtifact')
