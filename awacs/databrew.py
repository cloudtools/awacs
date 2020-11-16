# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Glue DataBrew'
prefix = 'databrew'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


BatchDeleteRecipeVersion = Action('BatchDeleteRecipeVersion')
CreateDataset = Action('CreateDataset')
CreateProfileJob = Action('CreateProfileJob')
CreateProject = Action('CreateProject')
CreateRecipe = Action('CreateRecipe')
CreateRecipeJob = Action('CreateRecipeJob')
CreateSchedule = Action('CreateSchedule')
DeleteDataset = Action('DeleteDataset')
DeleteJob = Action('DeleteJob')
DeleteProject = Action('DeleteProject')
DeleteRecipeVersion = Action('DeleteRecipeVersion')
DeleteSchedule = Action('DeleteSchedule')
DescribeDataset = Action('DescribeDataset')
DescribeJob = Action('DescribeJob')
DescribeProject = Action('DescribeProject')
DescribeRecipe = Action('DescribeRecipe')
DescribeSchedule = Action('DescribeSchedule')
ListDatasets = Action('ListDatasets')
ListJobRuns = Action('ListJobRuns')
ListJobs = Action('ListJobs')
ListProjects = Action('ListProjects')
ListRecipeVersions = Action('ListRecipeVersions')
ListRecipes = Action('ListRecipes')
ListSchedules = Action('ListSchedules')
ListTagsForResource = Action('ListTagsForResource')
PublishRecipe = Action('PublishRecipe')
SendProjectSessionAction = Action('SendProjectSessionAction')
StartJobRun = Action('StartJobRun')
StartProjectSession = Action('StartProjectSession')
StopJobRun = Action('StopJobRun')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateDataset = Action('UpdateDataset')
UpdateProfileJob = Action('UpdateProfileJob')
UpdateProject = Action('UpdateProject')
UpdateRecipe = Action('UpdateRecipe')
UpdateRecipeJob = Action('UpdateRecipeJob')
UpdateSchedule = Action('UpdateSchedule')
