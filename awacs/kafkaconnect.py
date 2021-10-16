# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Streaming for Kafka Connect"
prefix = "kafkaconnect"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
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
DescribeConnector = Action("DescribeConnector")
DescribeCustomPlugin = Action("DescribeCustomPlugin")
DescribeWorkerConfiguration = Action("DescribeWorkerConfiguration")
ListConnectors = Action("ListConnectors")
ListCustomPlugins = Action("ListCustomPlugins")
ListWorkerConfigurations = Action("ListWorkerConfigurations")
UpdateConnector = Action("UpdateConnector")
