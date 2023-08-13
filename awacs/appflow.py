# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon AppFlow"
prefix = "appflow"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelFlowExecutions = Action("CancelFlowExecutions")
CreateConnectorProfile = Action("CreateConnectorProfile")
CreateFlow = Action("CreateFlow")
DeleteConnectorProfile = Action("DeleteConnectorProfile")
DeleteFlow = Action("DeleteFlow")
DescribeConnector = Action("DescribeConnector")
DescribeConnectorEntity = Action("DescribeConnectorEntity")
DescribeConnectorFields = Action("DescribeConnectorFields")
DescribeConnectorProfiles = Action("DescribeConnectorProfiles")
DescribeConnectors = Action("DescribeConnectors")
DescribeFlow = Action("DescribeFlow")
DescribeFlowExecution = Action("DescribeFlowExecution")
DescribeFlowExecutionRecords = Action("DescribeFlowExecutionRecords")
DescribeFlows = Action("DescribeFlows")
ListConnectorEntities = Action("ListConnectorEntities")
ListConnectorFields = Action("ListConnectorFields")
ListConnectors = Action("ListConnectors")
ListFlows = Action("ListFlows")
ListTagsForResource = Action("ListTagsForResource")
RegisterConnector = Action("RegisterConnector")
ResetConnectorMetadataCache = Action("ResetConnectorMetadataCache")
RunFlow = Action("RunFlow")
StartFlow = Action("StartFlow")
StopFlow = Action("StopFlow")
TagResource = Action("TagResource")
UnRegisterConnector = Action("UnRegisterConnector")
UntagResource = Action("UntagResource")
UpdateConnectorProfile = Action("UpdateConnectorProfile")
UpdateConnectorRegistration = Action("UpdateConnectorRegistration")
UpdateFlow = Action("UpdateFlow")
UseConnectorProfile = Action("UseConnectorProfile")
