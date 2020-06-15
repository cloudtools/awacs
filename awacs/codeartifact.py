# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS CodeArtifact'
prefix = 'codeartifact'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateExternalConnection = Action('AssociateExternalConnection')
AssociateWithDownstreamRepository = \
    Action('AssociateWithDownstreamRepository')
CopyPackageVersions = Action('CopyPackageVersions')
CreateDomain = Action('CreateDomain')
CreateRepository = Action('CreateRepository')
DeleteDomain = Action('DeleteDomain')
DeleteDomainPermissionsPolicy = Action('DeleteDomainPermissionsPolicy')
DeletePackageVersions = Action('DeletePackageVersions')
DeleteRepository = Action('DeleteRepository')
DeleteRepositoryPermissionsPolicy = \
    Action('DeleteRepositoryPermissionsPolicy')
DescribeDomain = Action('DescribeDomain')
DescribePackageVersion = Action('DescribePackageVersion')
DescribeRepository = Action('DescribeRepository')
DisassociateExternalConnection = Action('DisassociateExternalConnection')
DisposePackageVersions = Action('DisposePackageVersions')
GetAuthorizationToken = Action('GetAuthorizationToken')
GetDomainPermissionsPolicy = Action('GetDomainPermissionsPolicy')
GetPackageVersionAsset = Action('GetPackageVersionAsset')
GetPackageVersionReadme = Action('GetPackageVersionReadme')
GetRepositoryEndpoint = Action('GetRepositoryEndpoint')
GetRepositoryPermissionsPolicy = Action('GetRepositoryPermissionsPolicy')
ListDomains = Action('ListDomains')
ListPackageVersionAssets = Action('ListPackageVersionAssets')
ListPackageVersionDependencies = Action('ListPackageVersionDependencies')
ListPackageVersions = Action('ListPackageVersions')
ListPackages = Action('ListPackages')
ListRepositories = Action('ListRepositories')
ListRepositoriesInDomain = Action('ListRepositoriesInDomain')
PublishPackageVersion = Action('PublishPackageVersion')
PutDomainPermissionsPolicy = Action('PutDomainPermissionsPolicy')
PutPackageMetadata = Action('PutPackageMetadata')
PutRepositoryPermissionsPolicy = Action('PutRepositoryPermissionsPolicy')
ReadFromRepository = Action('ReadFromRepository')
UpdatePackageVersionsStatus = Action('UpdatePackageVersionsStatus')
UpdateRepository = Action('UpdateRepository')
