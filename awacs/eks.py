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
AssociateEncryptionConfig = Action("AssociateEncryptionConfig")
AssociateIdentityProviderConfig = Action("AssociateIdentityProviderConfig")
CreateAddon = Action("CreateAddon")
CreateCluster = Action("CreateCluster")
CreateEksAnywhereSubscription = Action("CreateEksAnywhereSubscription")
CreateFargateProfile = Action("CreateFargateProfile")
CreateNodegroup = Action("CreateNodegroup")
DeleteAddon = Action("DeleteAddon")
DeleteCluster = Action("DeleteCluster")
DeleteEksAnywhereSubscription = Action("DeleteEksAnywhereSubscription")
DeleteFargateProfile = Action("DeleteFargateProfile")
DeleteNodegroup = Action("DeleteNodegroup")
DeregisterCluster = Action("DeregisterCluster")
DescribeAddon = Action("DescribeAddon")
DescribeAddonConfiguration = Action("DescribeAddonConfiguration")
DescribeAddonVersions = Action("DescribeAddonVersions")
DescribeCluster = Action("DescribeCluster")
DescribeEksAnywhereSubscription = Action("DescribeEksAnywhereSubscription")
DescribeFargateProfile = Action("DescribeFargateProfile")
DescribeIdentityProviderConfig = Action("DescribeIdentityProviderConfig")
DescribeNodegroup = Action("DescribeNodegroup")
DescribeUpdate = Action("DescribeUpdate")
DisassociateIdentityProviderConfig = Action("DisassociateIdentityProviderConfig")
ListAddons = Action("ListAddons")
ListClusters = Action("ListClusters")
ListEksAnywhereSubscriptions = Action("ListEksAnywhereSubscriptions")
ListFargateProfiles = Action("ListFargateProfiles")
ListIdentityProviderConfigs = Action("ListIdentityProviderConfigs")
ListNodegroups = Action("ListNodegroups")
ListTagsForResource = Action("ListTagsForResource")
ListUpdates = Action("ListUpdates")
RegisterCluster = Action("RegisterCluster")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateAddon = Action("UpdateAddon")
UpdateClusterConfig = Action("UpdateClusterConfig")
UpdateClusterVersion = Action("UpdateClusterVersion")
UpdateEksAnywhereSubscription = Action("UpdateEksAnywhereSubscription")
UpdateNodegroupConfig = Action("UpdateNodegroupConfig")
UpdateNodegroupVersion = Action("UpdateNodegroupVersion")
