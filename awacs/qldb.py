# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon QLDB'
prefix = 'qldb'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CancelJournalKinesisStream = Action('CancelJournalKinesisStream')
CreateLedger = Action('CreateLedger')
DeleteLedger = Action('DeleteLedger')
DescribeJournalKinesisStream = Action('DescribeJournalKinesisStream')
DescribeJournalS3Export = Action('DescribeJournalS3Export')
DescribeLedger = Action('DescribeLedger')
ExecuteStatement = Action('ExecuteStatement')
ExportJournalToS3 = Action('ExportJournalToS3')
GetBlock = Action('GetBlock')
GetDigest = Action('GetDigest')
GetRevision = Action('GetRevision')
InsertSampleData = Action('InsertSampleData')
ListJournalKinesisStreamsForLedger = \
    Action('ListJournalKinesisStreamsForLedger')
ListJournalS3Exports = Action('ListJournalS3Exports')
ListJournalS3ExportsForLedger = Action('ListJournalS3ExportsForLedger')
ListLedgers = Action('ListLedgers')
ListTagsForResource = Action('ListTagsForResource')
SendCommand = Action('SendCommand')
ShowCatalog = Action('ShowCatalog')
StreamJournalToKinesis = Action('StreamJournalToKinesis')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateLedger = Action('UpdateLedger')
