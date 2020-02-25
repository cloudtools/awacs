# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Migration Hub'
prefix = 'mgh'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateCreatedArtifact = Action('AssociateCreatedArtifact')
AssociateDiscoveredResource = Action('AssociateDiscoveredResource')
CreateHomeRegionControl = Action('CreateHomeRegionControl')
CreateProgressUpdateStream = Action('CreateProgressUpdateStream')
DeleteProgressUpdateStream = Action('DeleteProgressUpdateStream')
DescribeApplicationState = Action('DescribeApplicationState')
DescribeHomeRegionControls = Action('DescribeHomeRegionControls')
DescribeMigrationTask = Action('DescribeMigrationTask')
DisassociateCreatedArtifact = Action('DisassociateCreatedArtifact')
DisassociateDiscoveredResource = Action('DisassociateDiscoveredResource')
GetHomeRegion = Action('GetHomeRegion')
ImportMigrationTask = Action('ImportMigrationTask')
ListCreatedArtifacts = Action('ListCreatedArtifacts')
ListDiscoveredResources = Action('ListDiscoveredResources')
ListMigrationTasks = Action('ListMigrationTasks')
ListProgressUpdateStreams = Action('ListProgressUpdateStreams')
NotifyApplicationState = Action('NotifyApplicationState')
NotifyMigrationTaskState = Action('NotifyMigrationTaskState')
PutResourceAttributes = Action('PutResourceAttributes')
