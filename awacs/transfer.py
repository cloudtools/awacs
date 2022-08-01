# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Transfer Family"
prefix = "transfer"


class Action(BaseAction):
    def __init__(self, action: str = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


CreateAccess = Action("CreateAccess")
CreateAgreement = Action("CreateAgreement")
CreateConnector = Action("CreateConnector")
CreateProfile = Action("CreateProfile")
CreateServer = Action("CreateServer")
CreateUser = Action("CreateUser")
CreateWorkflow = Action("CreateWorkflow")
DeleteAccess = Action("DeleteAccess")
DeleteAgreement = Action("DeleteAgreement")
DeleteCertificate = Action("DeleteCertificate")
DeleteConnector = Action("DeleteConnector")
DeleteProfile = Action("DeleteProfile")
DeleteServer = Action("DeleteServer")
DeleteSshPublicKey = Action("DeleteSshPublicKey")
DeleteUser = Action("DeleteUser")
DeleteWorkflow = Action("DeleteWorkflow")
DescribeAccess = Action("DescribeAccess")
DescribeAgreeement = Action("DescribeAgreeement")
DescribeCertificate = Action("DescribeCertificate")
DescribeConnector = Action("DescribeConnector")
DescribeExecution = Action("DescribeExecution")
DescribeProfile = Action("DescribeProfile")
DescribeSecurityPolicy = Action("DescribeSecurityPolicy")
DescribeServer = Action("DescribeServer")
DescribeUser = Action("DescribeUser")
DescribeWorkflow = Action("DescribeWorkflow")
ImportCertificate = Action("ImportCertificate")
ImportSshPublicKey = Action("ImportSshPublicKey")
ListAccesses = Action("ListAccesses")
ListAgreements = Action("ListAgreements")
ListCertificates = Action("ListCertificates")
ListConnectors = Action("ListConnectors")
ListExecutions = Action("ListExecutions")
ListProfiles = Action("ListProfiles")
ListSecurityPolicies = Action("ListSecurityPolicies")
ListServers = Action("ListServers")
ListTagsForResource = Action("ListTagsForResource")
ListUsers = Action("ListUsers")
ListWorkflows = Action("ListWorkflows")
SendWorkflowStepState = Action("SendWorkflowStepState")
StartServer = Action("StartServer")
StopServer = Action("StopServer")
TagResource = Action("TagResource")
TestIdentityProvider = Action("TestIdentityProvider")
UntagResource = Action("UntagResource")
UpdateAccess = Action("UpdateAccess")
UpdateAgreement = Action("UpdateAgreement")
UpdateCertificate = Action("UpdateCertificate")
UpdateConnector = Action("UpdateConnector")
UpdateProfile = Action("UpdateProfile")
UpdateServer = Action("UpdateServer")
UpdateUser = Action("UpdateUser")
