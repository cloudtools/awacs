# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic Kubernetes Service"
prefix = "eks"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AccessKubernetesApi = Action("AccessKubernetesApi")
AssociateAccessPolicy = Action("AssociateAccessPolicy")
AssociateEncryptionConfig = Action("AssociateEncryptionConfig")
AssociateIdentityProviderConfig = Action("AssociateIdentityProviderConfig")
CreateAccessEntry = Action("CreateAccessEntry")
CreateAddon = Action("CreateAddon")
CreateCluster = Action("CreateCluster")
CreateEksAnywhereSubscription = Action("CreateEksAnywhereSubscription")
CreateFargateProfile = Action("CreateFargateProfile")
CreateNodegroup = Action("CreateNodegroup")
CreatePodIdentityAssociation = Action("CreatePodIdentityAssociation")
DeleteAccessEntry = Action("DeleteAccessEntry")
DeleteAddon = Action("DeleteAddon")
DeleteCluster = Action("DeleteCluster")
DeleteEksAnywhereSubscription = Action("DeleteEksAnywhereSubscription")
DeleteFargateProfile = Action("DeleteFargateProfile")
DeleteNodegroup = Action("DeleteNodegroup")
DeletePodIdentityAssociation = Action("DeletePodIdentityAssociation")
DeregisterCluster = Action("DeregisterCluster")
DescribeAccessEntry = Action("DescribeAccessEntry")
DescribeAddon = Action("DescribeAddon")
DescribeAddonConfiguration = Action("DescribeAddonConfiguration")
DescribeAddonVersions = Action("DescribeAddonVersions")
DescribeCluster = Action("DescribeCluster")
DescribeClusterVersions = Action("DescribeClusterVersions")
DescribeEksAnywhereSubscription = Action("DescribeEksAnywhereSubscription")
DescribeFargateProfile = Action("DescribeFargateProfile")
DescribeIdentityProviderConfig = Action("DescribeIdentityProviderConfig")
DescribeInsight = Action("DescribeInsight")
DescribeNodegroup = Action("DescribeNodegroup")
DescribePodIdentityAssociation = Action("DescribePodIdentityAssociation")
DescribeUpdate = Action("DescribeUpdate")
DisassociateAccessPolicy = Action("DisassociateAccessPolicy")
DisassociateIdentityProviderConfig = Action("DisassociateIdentityProviderConfig")
ListAccessEntries = Action("ListAccessEntries")
ListAccessPolicies = Action("ListAccessPolicies")
ListAddons = Action("ListAddons")
ListAssociatedAccessPolicies = Action("ListAssociatedAccessPolicies")
ListClusters = Action("ListClusters")
ListEksAnywhereSubscriptions = Action("ListEksAnywhereSubscriptions")
ListFargateProfiles = Action("ListFargateProfiles")
ListIdentityProviderConfigs = Action("ListIdentityProviderConfigs")
ListInsights = Action("ListInsights")
ListNodegroups = Action("ListNodegroups")
ListPodIdentityAssociations = Action("ListPodIdentityAssociations")
ListTagsForResource = Action("ListTagsForResource")
ListUpdates = Action("ListUpdates")
RegisterCluster = Action("RegisterCluster")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAccessEntry = Action("UpdateAccessEntry")
UpdateAddon = Action("UpdateAddon")
UpdateClusterConfig = Action("UpdateClusterConfig")
UpdateClusterVersion = Action("UpdateClusterVersion")
UpdateEksAnywhereSubscription = Action("UpdateEksAnywhereSubscription")
UpdateNodegroupConfig = Action("UpdateNodegroupConfig")
UpdateNodegroupVersion = Action("UpdateNodegroupVersion")
UpdatePodIdentityAssociation = Action("UpdatePodIdentityAssociation")
