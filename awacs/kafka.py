# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Managed Streaming for Apache Kafka"
prefix = "kafka"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


BatchAssociateScramSecret = Action("BatchAssociateScramSecret")
BatchDisassociateScramSecret = Action("BatchDisassociateScramSecret")
CreateCluster = Action("CreateCluster")
CreateClusterV2 = Action("CreateClusterV2")
CreateConfiguration = Action("CreateConfiguration")
CreateReplicator = Action("CreateReplicator")
CreateVpcConnection = Action("CreateVpcConnection")
DeleteCluster = Action("DeleteCluster")
DeleteClusterPolicy = Action("DeleteClusterPolicy")
DeleteConfiguration = Action("DeleteConfiguration")
DeleteReplicator = Action("DeleteReplicator")
DeleteVpcConnection = Action("DeleteVpcConnection")
DescribeCluster = Action("DescribeCluster")
DescribeClusterOperation = Action("DescribeClusterOperation")
DescribeClusterOperationV2 = Action("DescribeClusterOperationV2")
DescribeClusterV2 = Action("DescribeClusterV2")
DescribeConfiguration = Action("DescribeConfiguration")
DescribeConfigurationRevision = Action("DescribeConfigurationRevision")
DescribeReplicator = Action("DescribeReplicator")
DescribeVpcConnection = Action("DescribeVpcConnection")
GetBootstrapBrokers = Action("GetBootstrapBrokers")
GetClusterPolicy = Action("GetClusterPolicy")
GetCompatibleKafkaVersions = Action("GetCompatibleKafkaVersions")
ListClientVpcConnections = Action("ListClientVpcConnections")
ListClusterOperations = Action("ListClusterOperations")
ListClusterOperationsV2 = Action("ListClusterOperationsV2")
ListClusters = Action("ListClusters")
ListClustersV2 = Action("ListClustersV2")
ListConfigurationRevisions = Action("ListConfigurationRevisions")
ListConfigurations = Action("ListConfigurations")
ListKafkaVersions = Action("ListKafkaVersions")
ListNodes = Action("ListNodes")
ListReplicators = Action("ListReplicators")
ListScramSecrets = Action("ListScramSecrets")
ListTagsForResource = Action("ListTagsForResource")
ListVpcConnections = Action("ListVpcConnections")
PutClusterPolicy = Action("PutClusterPolicy")
RebootBroker = Action("RebootBroker")
RejectClientVpcConnection = Action("RejectClientVpcConnection")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateBrokerCount = Action("UpdateBrokerCount")
UpdateBrokerStorage = Action("UpdateBrokerStorage")
UpdateBrokerType = Action("UpdateBrokerType")
UpdateClusterConfiguration = Action("UpdateClusterConfiguration")
UpdateClusterKafkaVersion = Action("UpdateClusterKafkaVersion")
UpdateConfiguration = Action("UpdateConfiguration")
UpdateConnectivity = Action("UpdateConnectivity")
UpdateMonitoring = Action("UpdateMonitoring")
UpdateReplicationInfo = Action("UpdateReplicationInfo")
UpdateSecurity = Action("UpdateSecurity")
UpdateStorage = Action("UpdateStorage")
