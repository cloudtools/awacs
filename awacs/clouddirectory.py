# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from typing import Optional

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Cloud Directory"
prefix = "clouddirectory"


class Action(BaseAction):
    def __init__(self, action: Optional[str] = None) -> None:
        super().__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource: str = "", region: str = "", account: str = "") -> None:
        super().__init__(
            service=prefix, resource=resource, region=region, account=account
        )


AddFacetToObject = Action("AddFacetToObject")
ApplySchema = Action("ApplySchema")
AttachObject = Action("AttachObject")
AttachPolicy = Action("AttachPolicy")
AttachToIndex = Action("AttachToIndex")
AttachTypedLink = Action("AttachTypedLink")
BatchRead = Action("BatchRead")
BatchWrite = Action("BatchWrite")
CreateDirectory = Action("CreateDirectory")
CreateFacet = Action("CreateFacet")
CreateIndex = Action("CreateIndex")
CreateObject = Action("CreateObject")
CreateSchema = Action("CreateSchema")
CreateTypedLinkFacet = Action("CreateTypedLinkFacet")
DeleteDirectory = Action("DeleteDirectory")
DeleteFacet = Action("DeleteFacet")
DeleteObject = Action("DeleteObject")
DeleteSchema = Action("DeleteSchema")
DeleteTypedLinkFacet = Action("DeleteTypedLinkFacet")
DetachFromIndex = Action("DetachFromIndex")
DetachObject = Action("DetachObject")
DetachPolicy = Action("DetachPolicy")
DetachTypedLink = Action("DetachTypedLink")
DisableDirectory = Action("DisableDirectory")
EnableDirectory = Action("EnableDirectory")
GetAppliedSchemaVersion = Action("GetAppliedSchemaVersion")
GetDirectory = Action("GetDirectory")
GetFacet = Action("GetFacet")
GetLinkAttributes = Action("GetLinkAttributes")
GetObjectAttributes = Action("GetObjectAttributes")
GetObjectInformation = Action("GetObjectInformation")
GetSchemaAsJson = Action("GetSchemaAsJson")
GetTypedLinkFacetInformation = Action("GetTypedLinkFacetInformation")
ListAppliedSchemaArns = Action("ListAppliedSchemaArns")
ListAttachedIndices = Action("ListAttachedIndices")
ListDevelopmentSchemaArns = Action("ListDevelopmentSchemaArns")
ListDirectories = Action("ListDirectories")
ListFacetAttributes = Action("ListFacetAttributes")
ListFacetNames = Action("ListFacetNames")
ListIncomingTypedLinks = Action("ListIncomingTypedLinks")
ListIndex = Action("ListIndex")
ListManagedSchemaArns = Action("ListManagedSchemaArns")
ListObjectAttributes = Action("ListObjectAttributes")
ListObjectChildren = Action("ListObjectChildren")
ListObjectParentPaths = Action("ListObjectParentPaths")
ListObjectParents = Action("ListObjectParents")
ListObjectPolicies = Action("ListObjectPolicies")
ListOutgoingTypedLinks = Action("ListOutgoingTypedLinks")
ListPolicyAttachments = Action("ListPolicyAttachments")
ListPublishedSchemaArns = Action("ListPublishedSchemaArns")
ListTagsForResource = Action("ListTagsForResource")
ListTypedLinkFacetAttributes = Action("ListTypedLinkFacetAttributes")
ListTypedLinkFacetNames = Action("ListTypedLinkFacetNames")
LookupPolicy = Action("LookupPolicy")
PublishSchema = Action("PublishSchema")
PutSchemaFromJson = Action("PutSchemaFromJson")
RemoveFacetFromObject = Action("RemoveFacetFromObject")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFacet = Action("UpdateFacet")
UpdateLinkAttributes = Action("UpdateLinkAttributes")
UpdateObjectAttributes = Action("UpdateObjectAttributes")
UpdateSchema = Action("UpdateSchema")
UpdateTypedLinkFacet = Action("UpdateTypedLinkFacet")
UpgradeAppliedSchema = Action("UpgradeAppliedSchema")
UpgradePublishedSchema = Action("UpgradePublishedSchema")
