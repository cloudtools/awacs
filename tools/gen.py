#!/usr/bin/env python
#
# Generate Actions from AWS static configuration
#
import json
import os
import urllib2
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit.visitors.ecmavisitor import ECMAVisitor
from slimit import ast


header = """\
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN
"""

extra_classes = """\
class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)
"""

arn = """\
class %(upper)s_ARN(ARN):
    def __init__(self, *args, **kwargs):
        super(%(upper)s_ARN, self).__init__(*args, **kwargs)
        warnings.warn("This class is going away. Use %(lower)s.ARN instead.",
                      FutureWarning)
"""

legacy_arns = ['iam', 's3', 'sdb', 'sns', 'sqs']

aws_url = \
    "https://awsiamconsole.s3.amazonaws.com/iam/assets/js/bundles/policies.js"

basedir = 'generated'

response = urllib2.urlopen(aws_url)
config = response.read()


class JSONVisitor(ECMAVisitor):
    def visit_Identifier(self, node):
        return '"%s"' % node.value

    def visit_Number(self, node):
        return '"%s"' % node.value

    def visit_UnaryOp(self, node):
        s = self.visit(node.value)
        if node.op == '!' and s == 0:
            return '"true"'
        else:
            return s


visitor = JSONVisitor()
parser = Parser()
tree = parser.parse(config)

flag = False
policy_editor_config = ""
for node in nodevisitor.visit(tree):
    if (isinstance(node, ast.Identifier) and
            node.value == 'PolicyEditorConfig'):
        flag = True
    elif flag:
        policy_editor_config = visitor.visit(node)
        break

d = json.loads(policy_editor_config)

try:
    os.mkdir(basedir)
except OSError:
    pass

filename_seen = {}
for serviceName, serviceValue in d['serviceMap'].items():
    prefix = serviceValue['StringPrefix']
    filename = prefix
    # Handle prefix such as "directconnect:"
    if prefix[-1] == ':':
        filename = prefix[:-1]
    filename = filename.replace("-", "_")
    filename = ''.join([basedir, "/", filename, ".py"])
    with open(filename, "a") as fp:
        if filename not in filename_seen:
            filename_seen[filename] = True
            if prefix in legacy_arns:
                fp.write("import warnings\n")
            fp.write(header)
            fp.write("\n")
            fp.write("service_name = '%s'\n" % (serviceName,))
            fp.write("prefix = '%s'\n" % (prefix,))
            fp.write("\n\n")
            fp.write(extra_classes)
            fp.write("\n\n")
            if prefix in legacy_arns:
                fp.write(arn % {
                    'lower': prefix,
                    'upper': prefix.upper(),
                })
                fp.write("\n\n")
        for action in serviceValue['Actions']:
            action = action.strip()
            # Handle action such as "ReEncrypt*"
            if action[-1] == '*':
                action = action[:-1]
            # Wrap lines for pep8
            if len(action) > 30:
                format = "%s = \\\n    Action('%s')\n"
            else:
                format = "%s = Action('%s')\n"
            fp.write(format % (action, action))
