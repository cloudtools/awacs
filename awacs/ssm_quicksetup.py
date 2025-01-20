# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Systems Manager Quick Setup"
prefix = "ssm-quicksetup"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateConfigurationManager = Action("CreateConfigurationManager")
DeleteConfigurationManager = Action("DeleteConfigurationManager")
GetConfiguration = Action("GetConfiguration")
GetConfigurationManager = Action("GetConfigurationManager")
GetServiceSettings = Action("GetServiceSettings")
ListConfigurationManagers = Action("ListConfigurationManagers")
ListConfigurations = Action("ListConfigurations")
ListQuickSetupTypes = Action("ListQuickSetupTypes")
ListTagsForResource = Action("ListTagsForResource")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConfigurationDefinition = Action("UpdateConfigurationDefinition")
UpdateConfigurationManager = Action("UpdateConfigurationManager")
UpdateServiceSettings = Action("UpdateServiceSettings")
