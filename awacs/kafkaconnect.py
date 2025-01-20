# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Streaming for Kafka Connect"
prefix = "kafkaconnect"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateConnector = Action("CreateConnector")
CreateCustomPlugin = Action("CreateCustomPlugin")
CreateWorkerConfiguration = Action("CreateWorkerConfiguration")
DeleteConnector = Action("DeleteConnector")
DeleteCustomPlugin = Action("DeleteCustomPlugin")
DeleteWorkerConfiguration = Action("DeleteWorkerConfiguration")
DescribeConnector = Action("DescribeConnector")
DescribeConnectorOperation = Action("DescribeConnectorOperation")
DescribeCustomPlugin = Action("DescribeCustomPlugin")
DescribeWorkerConfiguration = Action("DescribeWorkerConfiguration")
ListConnectorOperations = Action("ListConnectorOperations")
ListConnectors = Action("ListConnectors")
ListCustomPlugins = Action("ListCustomPlugins")
ListTagsForResource = Action("ListTagsForResource")
ListWorkerConfigurations = Action("ListWorkerConfigurations")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnector = Action("UpdateConnector")
