# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Snowball"
prefix = "snowball"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CancelCluster = Action("CancelCluster")
CancelJob = Action("CancelJob")
CreateAddress = Action("CreateAddress")
CreateCluster = Action("CreateCluster")
CreateJob = Action("CreateJob")
CreateLongTermPricing = Action("CreateLongTermPricing")
CreateReturnShippingLabel = Action("CreateReturnShippingLabel")
DescribeAddress = Action("DescribeAddress")
DescribeAddresses = Action("DescribeAddresses")
DescribeCluster = Action("DescribeCluster")
DescribeJob = Action("DescribeJob")
DescribeReturnShippingLabel = Action("DescribeReturnShippingLabel")
GetJobManifest = Action("GetJobManifest")
GetJobUnlockCode = Action("GetJobUnlockCode")
GetSnowballUsage = Action("GetSnowballUsage")
GetSoftwareUpdates = Action("GetSoftwareUpdates")
ListClusterJobs = Action("ListClusterJobs")
ListClusters = Action("ListClusters")
ListCompatibleImages = Action("ListCompatibleImages")
ListJobs = Action("ListJobs")
ListLongTermPricing = Action("ListLongTermPricing")
ListPickupLocations = Action("ListPickupLocations")
ListServiceVersions = Action("ListServiceVersions")
UpdateCluster = Action("UpdateCluster")
UpdateJob = Action("UpdateJob")
UpdateJobShipmentState = Action("UpdateJobShipmentState")
UpdateLongTermPricing = Action("UpdateLongTermPricing")
