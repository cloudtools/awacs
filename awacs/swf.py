# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

service_name = 'Amazon Simple Workflow Service'
prefix = 'swf'

CancelTimer = Action(prefix, 'CancelTimer')
CancelWorkflowExecution = Action(prefix, 'CancelWorkflowExecution')
CompleteWorkflowExecution = Action(prefix, 'CompleteWorkflowExecution')
ContinueAsNewWorkflowExecution = \
    Action(prefix, 'ContinueAsNewWorkflowExecution')
CountClosedWorkflowExecutions = \
    Action(prefix, 'CountClosedWorkflowExecutions')
CountOpenWorkflowExecutions = \
    Action(prefix, 'CountOpenWorkflowExecutions')
CountPendingActivityTasks = Action(prefix, 'CountPendingActivityTasks')
CountPendingDecisionTasks = Action(prefix, 'CountPendingDecisionTasks')
DeprecateActivityType = Action(prefix, 'DeprecateActivityType')
DeprecateDomain = Action(prefix, 'DeprecateDomain')
DeprecateWorkflowType = Action(prefix, 'DeprecateWorkflowType')
DescribeActivityType = Action(prefix, 'DescribeActivityType')
DescribeDomain = Action(prefix, 'DescribeDomain')
DescribeWorkflowExecution = Action(prefix, 'DescribeWorkflowExecution')
DescribeWorkflowType = Action(prefix, 'DescribeWorkflowType')
FailWorkflowExecution = Action(prefix, 'FailWorkflowExecution')
GetWorkflowExecutionHistory = \
    Action(prefix, 'GetWorkflowExecutionHistory')
ListActivityTypes = Action(prefix, 'ListActivityTypes')
ListClosedWorkflowExecutions = \
    Action(prefix, 'ListClosedWorkflowExecutions')
ListDomains = Action(prefix, 'ListDomains')
ListOpenWorkflowExecutions = \
    Action(prefix, 'ListOpenWorkflowExecutions')
ListWorkflowTypes = Action(prefix, 'ListWorkflowTypes')
PollForActivityTask = Action(prefix, 'PollForActivityTask')
PollForDecisionTask = Action(prefix, 'PollForDecisionTask')
RecordActivityTaskHeartbeat = \
    Action(prefix, 'RecordActivityTaskHeartbeat')
RecordMarker = Action(prefix, 'RecordMarker')
RegisterActivityType = Action(prefix, 'RegisterActivityType')
RegisterDomain = Action(prefix, 'RegisterDomain')
RegisterWorkflowType = Action(prefix, 'RegisterWorkflowType')
RequestCancelActivityTask = Action(prefix, 'RequestCancelActivityTask')
RequestCancelExternalWorkflowExecution = \
    Action(prefix, 'RequestCancelExternalWorkflowExecution')
RequestCancelWorkflowExecution = \
    Action(prefix, 'RequestCancelWorkflowExecution')
RespondActivityTaskCanceled = \
    Action(prefix, 'RespondActivityTaskCanceled')
RespondActivityTaskCompleted = \
    Action(prefix, 'RespondActivityTaskCompleted')
RespondActivityTaskFailed = Action(prefix, 'RespondActivityTaskFailed')
RespondDecisionTaskCompleted = \
    Action(prefix, 'RespondDecisionTaskCompleted')
ScheduleActivityTask = Action(prefix, 'ScheduleActivityTask')
SignalExternalWorkflowExecution = \
    Action(prefix, 'SignalExternalWorkflowExecution')
SignalWorkflowExecution = Action(prefix, 'SignalWorkflowExecution')
StartChildWorkflowExecution = \
    Action(prefix, 'StartChildWorkflowExecution')
StartTimer = Action(prefix, 'StartTimer')
StartWorkflowExecution = Action(prefix, 'StartWorkflowExecution')
TerminateWorkflowExecution = \
    Action(prefix, 'TerminateWorkflowExecution')
