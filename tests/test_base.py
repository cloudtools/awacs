import json
import unittest

import awacs
from awacs.aws import Action, PolicyDocument


class AWSHelperFn(object):
    """Mock class to test classes with non-awacs AWSHelperFn parent."""

    def to_json(self, indent=4, sort_keys=True):
        p = self
        return json.dumps(p, cls=awacs.awsencode, indent=indent,
                          sort_keys=sort_keys)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.to_json() == other.to_json()
        else:
            return False


class AWSHelperFnChild(AWSHelperFn):
    """Child class of non-awacs AWSHelperFn."""

    def __init__(self, **kwargs):
        """Instantiate class."""
        for key, val in kwargs.items():
            setattr(self, key, val)

    def JSONrepr(self):
        """JSON serialization."""
        return self.__dict__


class TypeValidationObject(awacs.AWSProperty):
    """Subclass the AWSObject to test its functionality."""

    props = {
        'ExpectList': (list, False)
    }


class TestAWSObject(unittest.TestCase):
    def test_invalid_property(self):
        with self.assertRaises(AttributeError) as exc:
            # statement should be Statement
            PolicyDocument(Version='2012-10-17', statement=[])

        self.assertEqual(
            exc.exception.args[0],
            "'awacs.aws.PolicyDocument' object does not support attribute "
            "'statement'"
        )


class TestAWSProperty(unittest.TestCase):
    def test_prop_value_type_mismatch_expect_list(self):
        class InvalidClass(object):
            """Class of invalid type."""

        tests_values = [
            'val',
            {'key': 'val'},
            {'val'},
            tuple('val'),
            InvalidClass()
        ]

        for val in tests_values:
            with self.assertRaises(TypeError) as exc:
                TypeValidationObject(ExpectList=val)
            self.assertEqual(
                exc.exception.args[0],
                "ExpectList is %s, expected %s" % (type(val), type(list()))
            )

    def test_prop_value_type_expect_list(self):
        tests_values = [
            ['val'],
            Action('s3', '*'),
            AWSHelperFnChild(key='val')
        ]

        for val in tests_values:
            self.assertEqual(TypeValidationObject(ExpectList=val).ExpectList,
                             val)
