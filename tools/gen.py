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

aws_url = \
    "https://awsiamconsole.s3.amazonaws.com/iam/assets/js/bundles/policies.js"

header = """\
# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action

"""

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
    if (isinstance(node, ast.Identifier)
            and node.value == 'PolicyEditorConfig'):
        flag = True
    elif flag:
        policy_editor_config = visitor.visit(node)
        break

d = json.loads(policy_editor_config)

try:
    os.mkdir(basedir)
except OSError:
    pass

for serviceName, serviceValue in d['serviceMap'].items():
    prefix = serviceValue['StringPrefix']
    filename = prefix
    # Handle prefix such as "directconnect:"
    if prefix[-1] == ':':
        filename = prefix[:-1]
    filename = ''.join([basedir, "/", filename, ".py"])
    with open(filename, "a") as fp:
        fp.write(header)
        fp.write("service_name = '%s'\n" % (serviceName,))
        fp.write("prefix = '%s'\n" % (prefix,))
        fp.write("\n")
        for action in serviceValue['Actions']:
            # Wrap lines for pep8
            if len(action) > 25:
                format = "%s = \\\n    Action(prefix, '%s')\n"
            else:
                format = "%s = Action(prefix, '%s')\n"
            fp.write(format % (action, action))
