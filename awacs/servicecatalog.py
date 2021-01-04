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
AssociateAttributeGroup = Action('AssociateAttributeGroup')
AssociateBudgetWithResource = Action('AssociateBudgetWithResource')
AssociatePrincipalWithPortfolio = \
    Action('AssociatePrincipalWithPortfolio')
AssociateProductWithPortfolio = Action('AssociateProductWithPortfolio')
AssociateResource = Action('AssociateResource')
AssociateServiceActionWithProvisioningArtifact = \
    Action('AssociateServiceActionWithProvisioningArtifact')
AssociateTagOptionWithResource = Action('AssociateTagOptionWithResource')
BatchAssociateServiceActionWithProvisioningArtifact = \
    Action('BatchAssociateServiceActionWithProvisioningArtifact')
BatchDisassociateServiceActionFromProvisioningArtifact = \
    Action('BatchDisassociateServiceActionFromProvisioningArtifact')
CopyProduct = Action('CopyProduct')
CreateApplication = Action('CreateApplication')
CreateAttributeGroup = Action('CreateAttributeGroup')
CreateConstraint = Action('CreateConstraint')
CreatePortfolio = Action('CreatePortfolio')
CreatePortfolioShare = Action('CreatePortfolioShare')
CreateProduct = Action('CreateProduct')
CreateProvisionedProductPlan = Action('CreateProvisionedProductPlan')
CreateProvisioningArtifact = Action('CreateProvisioningArtifact')
CreateServiceAction = Action('CreateServiceAction')
CreateTagOption = Action('CreateTagOption')
DeleteApplication = Action('DeleteApplication')
DeleteAttributeGroup = Action('DeleteAttributeGroup')
DeleteConstraint = Action('DeleteConstraint')
DeletePortfolio = Action('DeletePortfolio')
DeletePortfolioShare = Action('DeletePortfolioShare')
DeleteProduct = Action('DeleteProduct')
DeleteProvisionedProductPlan = Action('DeleteProvisionedProductPlan')
DeleteProvisioningArtifact = Action('DeleteProvisioningArtifact')
DeleteServiceAction = Action('DeleteServiceAction')
DeleteTagOption = Action('DeleteTagOption')
DescribeConstraint = Action('DescribeConstraint')
DescribeCopyProductStatus = Action('DescribeCopyProductStatus')
DescribePortfolio = Action('DescribePortfolio')
DescribePortfolioShareStatus = Action('DescribePortfolioShareStatus')
DescribeProduct = Action('DescribeProduct')
DescribeProductAsAdmin = Action('DescribeProductAsAdmin')
DescribeProductView = Action('DescribeProductView')
DescribeProvisionedProduct = Action('DescribeProvisionedProduct')
DescribeProvisionedProductPlan = Action('DescribeProvisionedProductPlan')
DescribeProvisioningArtifact = Action('DescribeProvisioningArtifact')
DescribeProvisioningParameters = Action('DescribeProvisioningParameters')
DescribeRecord = Action('DescribeRecord')
DescribeServiceAction = Action('DescribeServiceAction')
DescribeServiceActionExecutionParameters = \
    Action('DescribeServiceActionExecutionParameters')
DescribeTagOption = Action('DescribeTagOption')
DisableAWSOrganizationsAccess = Action('DisableAWSOrganizationsAccess')
DisassociateAttributeGroup = Action('DisassociateAttributeGroup')
DisassociateBudgetFromResource = Action('DisassociateBudgetFromResource')
DisassociatePrincipalFromPortfolio = \
    Action('DisassociatePrincipalFromPortfolio')
DisassociateProductFromPortfolio = \
    Action('DisassociateProductFromPortfolio')
DisassociateResource = Action('DisassociateResource')
DisassociateServiceActionFromProvisioningArtifact = \
    Action('DisassociateServiceActionFromProvisioningArtifact')
DisassociateTagOptionFromResource = \
    Action('DisassociateTagOptionFromResource')
EnableAWSOrganizationsAccess = Action('EnableAWSOrganizationsAccess')
ExecuteProvisionedProductPlan = Action('ExecuteProvisionedProductPlan')
ExecuteProvisionedProductServiceAction = \
    Action('ExecuteProvisionedProductServiceAction')
GetAWSOrganizationsAccessStatus = \
    Action('GetAWSOrganizationsAccessStatus')
GetApplication = Action('GetApplication')
GetAttributeGroup = Action('GetAttributeGroup')
ImportAsProvisionedProduct = Action('ImportAsProvisionedProduct')
ListAcceptedPortfolioShares = Action('ListAcceptedPortfolioShares')
ListApplications = Action('ListApplications')
ListAssociatedAttributeGroups = Action('ListAssociatedAttributeGroups')
ListAssociatedResources = Action('ListAssociatedResources')
ListAttributeGroups = Action('ListAttributeGroups')
ListBudgetsForResource = Action('ListBudgetsForResource')
ListConstraintsForPortfolio = Action('ListConstraintsForPortfolio')
ListLaunchPaths = Action('ListLaunchPaths')
ListOrganizationPortfolioAccess = \
    Action('ListOrganizationPortfolioAccess')
ListPortfolioAccess = Action('ListPortfolioAccess')
ListPortfolios = Action('ListPortfolios')
ListPortfoliosForProduct = Action('ListPortfoliosForProduct')
ListPrincipalsForPortfolio = Action('ListPrincipalsForPortfolio')
ListProvisionedProductPlans = Action('ListProvisionedProductPlans')
ListProvisioningArtifacts = Action('ListProvisioningArtifacts')
ListProvisioningArtifactsForServiceAction = \
    Action('ListProvisioningArtifactsForServiceAction')
ListRecordHistory = Action('ListRecordHistory')
ListResourcesForTagOption = Action('ListResourcesForTagOption')
ListServiceActions = Action('ListServiceActions')
ListServiceActionsForProvisioningArtifact = \
    Action('ListServiceActionsForProvisioningArtifact')
ListStackInstancesForProvisionedProduct = \
    Action('ListStackInstancesForProvisionedProduct')
ListTagOptions = Action('ListTagOptions')
ListTagsForResource = Action('ListTagsForResource')
ProvisionProduct = Action('ProvisionProduct')
RejectPortfolioShare = Action('RejectPortfolioShare')
ScanProvisionedProducts = Action('ScanProvisionedProducts')
SearchProducts = Action('SearchProducts')
SearchProductsAsAdmin = Action('SearchProductsAsAdmin')
SearchProvisionedProducts = Action('SearchProvisionedProducts')
SyncResource = Action('SyncResource')
TagResource = Action('TagResource')
TerminateProvisionedProduct = Action('TerminateProvisionedProduct')
UntagResource = Action('UntagResource')
UpdateApplication = Action('UpdateApplication')
UpdateAttributeGroup = Action('UpdateAttributeGroup')
UpdateConstraint = Action('UpdateConstraint')
UpdatePortfolio = Action('UpdatePortfolio')
UpdateProduct = Action('UpdateProduct')
UpdateProvisionedProduct = Action('UpdateProvisionedProduct')
UpdateProvisionedProductProperties = \
    Action('UpdateProvisionedProductProperties')
UpdateProvisioningArtifact = Action('UpdateProvisioningArtifact')
UpdateServiceAction = Action('UpdateServiceAction')
UpdateTagOption = Action('UpdateTagOption')
