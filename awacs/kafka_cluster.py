# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Apache Kafka APIs for Amazon MSK clusters"
prefix = "kafka-cluster"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AlterCluster = Action("AlterCluster")
AlterClusterDynamicConfiguration = Action("AlterClusterDynamicConfiguration")
AlterGroup = Action("AlterGroup")
AlterTopic = Action("AlterTopic")
AlterTopicDynamicConfiguration = Action("AlterTopicDynamicConfiguration")
AlterTransactionalId = Action("AlterTransactionalId")
Connect = Action("Connect")
CreateTopic = Action("CreateTopic")
DeleteGroup = Action("DeleteGroup")
DeleteTopic = Action("DeleteTopic")
DescribeCluster = Action("DescribeCluster")
DescribeClusterDynamicConfiguration = Action("DescribeClusterDynamicConfiguration")
DescribeGroup = Action("DescribeGroup")
DescribeTopic = Action("DescribeTopic")
DescribeTopicDynamicConfiguration = Action("DescribeTopicDynamicConfiguration")
DescribeTransactionalId = Action("DescribeTransactionalId")
ReadData = Action("ReadData")
WriteData = Action("WriteData")
WriteDataIdempotently = Action("WriteDataIdempotently")
