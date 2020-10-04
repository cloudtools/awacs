# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS IoT Things Graph'
prefix = 'iotthingsgraph'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateEntityToThing = Action('AssociateEntityToThing')
CreateFlowTemplate = Action('CreateFlowTemplate')
CreateSystemInstance = Action('CreateSystemInstance')
CreateSystemTemplate = Action('CreateSystemTemplate')
DeleteFlowTemplate = Action('DeleteFlowTemplate')
DeleteNamespace = Action('DeleteNamespace')
DeleteSystemInstance = Action('DeleteSystemInstance')
DeleteSystemTemplate = Action('DeleteSystemTemplate')
DeploySystemInstance = Action('DeploySystemInstance')
DeprecateFlowTemplate = Action('DeprecateFlowTemplate')
DeprecateSystemTemplate = Action('DeprecateSystemTemplate')
DescribeNamespace = Action('DescribeNamespace')
DissociateEntityFromThing = Action('DissociateEntityFromThing')
GetEntities = Action('GetEntities')
GetFlowTemplate = Action('GetFlowTemplate')
GetFlowTemplateRevisions = Action('GetFlowTemplateRevisions')
GetNamespaceDeletionStatus = Action('GetNamespaceDeletionStatus')
GetSystemInstance = Action('GetSystemInstance')
GetSystemTemplate = Action('GetSystemTemplate')
GetSystemTemplateRevisions = Action('GetSystemTemplateRevisions')
GetUploadStatus = Action('GetUploadStatus')
ListFlowExecutionMessages = Action('ListFlowExecutionMessages')
ListTagsForResource = Action('ListTagsForResource')
SearchEntities = Action('SearchEntities')
SearchFlowExecutions = Action('SearchFlowExecutions')
SearchFlowTemplates = Action('SearchFlowTemplates')
SearchSystemInstances = Action('SearchSystemInstances')
SearchSystemTemplates = Action('SearchSystemTemplates')
SearchThings = Action('SearchThings')
TagResource = Action('TagResource')
UndeploySystemInstance = Action('UndeploySystemInstance')
UntagResource = Action('UntagResource')
UpdateFlowTemplate = Action('UpdateFlowTemplate')
UpdateSystemTemplate = Action('UpdateSystemTemplate')
UploadEntityDefinitions = Action('UploadEntityDefinitions')
