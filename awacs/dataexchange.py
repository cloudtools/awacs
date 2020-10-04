# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Data Exchange'
prefix = 'dataexchange'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelJob = Action('CancelJob')
CreateAsset = Action('CreateAsset')
CreateDataSet = Action('CreateDataSet')
CreateJob = Action('CreateJob')
CreateRevision = Action('CreateRevision')
DeleteAsset = Action('DeleteAsset')
DeleteDataSet = Action('DeleteDataSet')
DeleteRevision = Action('DeleteRevision')
GetAsset = Action('GetAsset')
GetDataSet = Action('GetDataSet')
GetJob = Action('GetJob')
GetRevision = Action('GetRevision')
ListDataSetRevisions = Action('ListDataSetRevisions')
ListDataSets = Action('ListDataSets')
ListJobs = Action('ListJobs')
ListRevisionAssets = Action('ListRevisionAssets')
ListTagsForResource = Action('ListTagsForResource')
StartJob = Action('StartJob')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAsset = Action('UpdateAsset')
UpdateDataSet = Action('UpdateDataSet')
UpdateRevision = Action('UpdateRevision')
