# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Audit Manager'
prefix = 'auditmanager'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AssociateAssessmentReportEvidenceFolder = \
    Action('AssociateAssessmentReportEvidenceFolder')
BatchAssociateAssessmentReportEvidence = \
    Action('BatchAssociateAssessmentReportEvidence')
BatchCreateDelegationByAssessment = \
    Action('BatchCreateDelegationByAssessment')
BatchDeleteDelegationByAssessment = \
    Action('BatchDeleteDelegationByAssessment')
BatchDisassociateAssessmentReportEvidence = \
    Action('BatchDisassociateAssessmentReportEvidence')
BatchImportEvidenceToAssessmentControl = \
    Action('BatchImportEvidenceToAssessmentControl')
CreateAssessment = Action('CreateAssessment')
CreateAssessmentFramework = Action('CreateAssessmentFramework')
CreateAssessmentReport = Action('CreateAssessmentReport')
CreateControl = Action('CreateControl')
DeleteAssessment = Action('DeleteAssessment')
DeleteAssessmentFramework = Action('DeleteAssessmentFramework')
DeleteAssessmentReport = Action('DeleteAssessmentReport')
DeleteControl = Action('DeleteControl')
DeregisterAccount = Action('DeregisterAccount')
DeregisterOrganizationAdminAccount = \
    Action('DeregisterOrganizationAdminAccount')
DisassociateAssessmentReportEvidenceFolder = \
    Action('DisassociateAssessmentReportEvidenceFolder')
GetAccountStatus = Action('GetAccountStatus')
GetAssessment = Action('GetAssessment')
GetAssessmentFramework = Action('GetAssessmentFramework')
GetAssessmentReportUrl = Action('GetAssessmentReportUrl')
GetChangeLogs = Action('GetChangeLogs')
GetControl = Action('GetControl')
GetDelegations = Action('GetDelegations')
GetEvidence = Action('GetEvidence')
GetEvidenceByEvidenceFolder = Action('GetEvidenceByEvidenceFolder')
GetEvidenceFolder = Action('GetEvidenceFolder')
GetEvidenceFoldersByAssessment = Action('GetEvidenceFoldersByAssessment')
GetEvidenceFoldersByAssessmentControl = \
    Action('GetEvidenceFoldersByAssessmentControl')
GetOrganizationAdminAccount = Action('GetOrganizationAdminAccount')
GetServicesInScope = Action('GetServicesInScope')
GetSettings = Action('GetSettings')
ListAssessmentFrameworks = Action('ListAssessmentFrameworks')
ListAssessmentReports = Action('ListAssessmentReports')
ListAssessments = Action('ListAssessments')
ListControls = Action('ListControls')
ListKeywordsForDataSource = Action('ListKeywordsForDataSource')
ListNotifications = Action('ListNotifications')
ListTagsForResource = Action('ListTagsForResource')
RegisterAccount = Action('RegisterAccount')
RegisterOrganizationAdminAccount = \
    Action('RegisterOrganizationAdminAccount')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateAssessment = Action('UpdateAssessment')
UpdateAssessmentControl = Action('UpdateAssessmentControl')
UpdateAssessmentControlSetStatus = \
    Action('UpdateAssessmentControlSetStatus')
UpdateAssessmentFramework = Action('UpdateAssessmentFramework')
UpdateAssessmentStatus = Action('UpdateAssessmentStatus')
UpdateControl = Action('UpdateControl')
UpdateSettings = Action('UpdateSettings')
ValidateAssessmentReportIntegrity = \
    Action('ValidateAssessmentReportIntegrity')
