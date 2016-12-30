# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import json
import re
import types

__version__ = "0.6.1"


valid_names = re.compile(r'^[a-zA-Z0-9]+$')


class AWSObject(object):
    def __init__(self, name, type=None, dictname=None, props={}, **kwargs):
        self.name = name
        self.props = props
        # Cache the keys for validity checks
        self.propnames = props.keys()

        # unset/None is also legal
        if name and not valid_names.match(name):
            raise ValueError('Name not alphanumeric')

        # Create the list of properties set on this object by the user
        self.properties = {}
        if dictname:
            self.resource = {
                dictname: self.properties,
            }
        else:
            self.resource = self.properties
        self.__initialized = True

        # Now that it is initialized, populate it with the kwargs
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __getattr__(self, name):
        try:
            return self.properties.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if '_AWSObject__initialized' not in self.__dict__:
            return dict.__setattr__(self, name, value)
        elif name in self.propnames:
            # Check the type of the object and compare against what we were
            # expecting.
            expected_type = self.props[name][0]

            # If it's a function, call it...
            if isinstance(expected_type, types.FunctionType):
                value = expected_type(value)
                return self.properties.__setitem__(name, value)

            # If it's a list of types, check against those types...
            elif isinstance(expected_type, list):
                # If we're expecting a list, then make sure it is a list
                if not isinstance(value, list):
                    self._raise_type(name, value, expected_type)

                # Iterate over the list and make sure it matches our
                # type checks
                for v in value:
                    if not isinstance(v, tuple(expected_type)):
                        self._raise_type(name, v, expected_type)
                # Validated so assign it
                return self.properties.__setitem__(name, value)

            # Single type so check the type of the object and compare against
            # what we were expecting. Special case AWS helper functions.
            elif isinstance(value, expected_type) or \
                    isinstance(value, AWSHelperFn):
                return self.properties.__setitem__(name, value)
            else:
                self._raise_type(name, value, expected_type)

        raise AttributeError("%s object does not support attribute %s" %
                             (self.type, name))

    def _raise_type(self, name, value, expected_type):
        raise TypeError('%s is %s, expected %s' %
                        (name, type(value), expected_type))

    def validate(self):
        pass

    def JSONrepr(self):
        for k, v in self.props.items():
            if v[1] and k not in self.properties:
                raise ValueError("Resource %s required in type %s" %
                                 (k, self.type))
        self.validate()
        return self.resource


class AWSProperty(AWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    def __init__(self, **kwargs):
        sup = super(AWSProperty, self)
        sup.__init__(None, props=self.props, **kwargs)


class AWSHelperFn(object):
    def getdata(self, data):
        if isinstance(data, AWSObject):
            return data.name
        else:
            return data


class awsencode(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'JSONrepr'):
            return obj.JSONrepr()
        return json.JSONEncoder.default(self, obj)
