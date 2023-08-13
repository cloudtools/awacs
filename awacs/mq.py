# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon MQ"
prefix = "mq"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateBroker = Action("CreateBroker")
CreateConfiguration = Action("CreateConfiguration")
CreateReplicaBroker = Action("CreateReplicaBroker")
CreateTags = Action("CreateTags")
CreateUser = Action("CreateUser")
DeleteBroker = Action("DeleteBroker")
DeleteTags = Action("DeleteTags")
DeleteUser = Action("DeleteUser")
DescribeBroker = Action("DescribeBroker")
DescribeBrokerEngineTypes = Action("DescribeBrokerEngineTypes")
DescribeBrokerInstanceOptions = Action("DescribeBrokerInstanceOptions")
DescribeConfiguration = Action("DescribeConfiguration")
DescribeConfigurationRevision = Action("DescribeConfigurationRevision")
DescribeUser = Action("DescribeUser")
ListBrokers = Action("ListBrokers")
ListConfigurationRevisions = Action("ListConfigurationRevisions")
ListConfigurations = Action("ListConfigurations")
ListTags = Action("ListTags")
ListUsers = Action("ListUsers")
Promote = Action("Promote")
RebootBroker = Action("RebootBroker")
UpdateBroker = Action("UpdateBroker")
UpdateConfiguration = Action("UpdateConfiguration")
UpdateUser = Action("UpdateUser")
