# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodeArtifact"
prefix = "codeartifact"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AssociateExternalConnection = Action("AssociateExternalConnection")
AssociateWithDownstreamRepository = Action("AssociateWithDownstreamRepository")
CopyPackageVersions = Action("CopyPackageVersions")
CreateDomain = Action("CreateDomain")
CreatePackageGroup = Action("CreatePackageGroup")
CreateRepository = Action("CreateRepository")
DeleteDomain = Action("DeleteDomain")
DeleteDomainPermissionsPolicy = Action("DeleteDomainPermissionsPolicy")
DeletePackage = Action("DeletePackage")
DeletePackageGroup = Action("DeletePackageGroup")
DeletePackageVersions = Action("DeletePackageVersions")
DeleteRepository = Action("DeleteRepository")
DeleteRepositoryPermissionsPolicy = Action("DeleteRepositoryPermissionsPolicy")
DescribeDomain = Action("DescribeDomain")
DescribePackage = Action("DescribePackage")
DescribePackageGroup = Action("DescribePackageGroup")
DescribePackageVersion = Action("DescribePackageVersion")
DescribeRepository = Action("DescribeRepository")
DisassociateExternalConnection = Action("DisassociateExternalConnection")
DisposePackageVersions = Action("DisposePackageVersions")
GetAssociatedPackageGroup = Action("GetAssociatedPackageGroup")
GetAuthorizationToken = Action("GetAuthorizationToken")
GetDomainPermissionsPolicy = Action("GetDomainPermissionsPolicy")
GetPackageVersionAsset = Action("GetPackageVersionAsset")
GetPackageVersionReadme = Action("GetPackageVersionReadme")
GetRepositoryEndpoint = Action("GetRepositoryEndpoint")
GetRepositoryPermissionsPolicy = Action("GetRepositoryPermissionsPolicy")
ListAllowedRepositoriesForGroup = Action("ListAllowedRepositoriesForGroup")
ListAssociatedPackages = Action("ListAssociatedPackages")
ListDomains = Action("ListDomains")
ListPackageGroups = Action("ListPackageGroups")
ListPackageVersionAssets = Action("ListPackageVersionAssets")
ListPackageVersionDependencies = Action("ListPackageVersionDependencies")
ListPackageVersions = Action("ListPackageVersions")
ListPackages = Action("ListPackages")
ListRepositories = Action("ListRepositories")
ListRepositoriesInDomain = Action("ListRepositoriesInDomain")
ListSubPackageGroups = Action("ListSubPackageGroups")
ListTagsForResource = Action("ListTagsForResource")
PublishPackageVersion = Action("PublishPackageVersion")
PutDomainPermissionsPolicy = Action("PutDomainPermissionsPolicy")
PutPackageMetadata = Action("PutPackageMetadata")
PutPackageOriginConfiguration = Action("PutPackageOriginConfiguration")
PutRepositoryPermissionsPolicy = Action("PutRepositoryPermissionsPolicy")
ReadFromRepository = Action("ReadFromRepository")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdatePackageGroup = Action("UpdatePackageGroup")
UpdatePackageGroupOriginConfiguration = Action("UpdatePackageGroupOriginConfiguration")
UpdatePackageVersionsStatus = Action("UpdatePackageVersionsStatus")
UpdateRepository = Action("UpdateRepository")
