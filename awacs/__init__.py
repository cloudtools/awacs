# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import inspect
import json
import re
import types
from typing import Any, KeysView, NoReturn, Optional, TypeVar, Union

__version__ = "2.5.0"

valid_names = re.compile(r"^[a-zA-Z0-9]+$")


class AWSObject:
    def __init__(
        self,
        name: Optional[str],
        type: Optional[Any] = None,
        dictname: Optional[Any] = None,
        props: Optional[dict] = None,
        **kwargs: Any
    ) -> None:
        self.name = name
        self.props = props or {}

        # unset/None is also legal
        if name and not valid_names.match(name):
            raise ValueError("Name not alphanumeric")

        # Create the list of properties set on this object by the user
        self.properties: dict = {}
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

    @property
    def propnames(self) -> KeysView[str]:
        # For backwards compatibility; should be removed in v3
        return self.props.keys()

    def __getattr__(self, name: str) -> Any:
        try:
            return self.properties.__getitem__(name)
        except KeyError as exc:
            raise AttributeError(name) from exc

    def __setattr__(self, name: str, value: Any) -> Any:
        if "_AWSObject__initialized" not in self.__dict__:
            return dict.__setattr__(self, name, value)
        elif name in self.props:
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
            # what we were expecting. Special case AWS helper functions and its
            # sub classes. Also handles AWS helper functions from other
            # libraries like cloudtools/troposphere.
            elif isinstance(value, expected_type) or "AWSHelperFn" in [
                c.__name__ for c in inspect.getmro(type(value))
            ]:
                return self.properties.__setitem__(name, value)
            else:
                self._raise_type(name, value, expected_type)

        full_class_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        raise AttributeError(
            "'%s' object does not support attribute '%s'" % (full_class_name, name)
        )

    def _raise_type(self, name: str, value: Any, expected_type: Any) -> NoReturn:
        raise TypeError("%s is %s, expected %s" % (name, type(value), expected_type))

    def validate(self) -> None:
        pass

    def JSONrepr(self) -> dict:
        for k, v in self.props.items():
            if v[1] and k not in self.properties:
                raise ValueError("Resource %s required in type %s" % (k, type(self)))
        self.validate()
        return self.resource

    def to_json(self, indent: int = 4, sort_keys: bool = True) -> str:
        p = self.properties
        return json.dumps(p, cls=awsencode, indent=indent, sort_keys=sort_keys)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.to_json() == other.to_json()
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self.to_json())


class AWSProperty(AWSObject):
    """
    Used for CloudFormation Resource Property objects
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
    aws-product-property-reference.html
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(None, props=self.props, **kwargs)


T = TypeVar("T")


class AWSHelperFn:
    def getdata(self, data: Union[AWSObject, T]) -> Union[str, None, T]:
        if isinstance(data, AWSObject):
            return data.name
        else:
            return data

    def to_json(self, indent: int = 4, sort_keys: bool = True) -> str:
        p = self
        return json.dumps(p, cls=awsencode, indent=indent, sort_keys=sort_keys)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.to_json() == other.to_json()
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self.to_json())


class awsencode(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if hasattr(obj, "JSONrepr"):
            return obj.JSONrepr()
        return json.JSONEncoder.default(self, obj)
