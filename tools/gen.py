#!/usr/bin/env python
#
# Generate Actions from AWS static configuration
#
import json
import os
import urllib2

aws_url = "http://awspolicygen.s3.amazonaws.com/config.json"

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
d = json.loads(config)

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
