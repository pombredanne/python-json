import unittest

from hgicommon.serialization.models import PropertyMapping
from hgicommon.tests.serialization._serializers import SimpleModelSerializer, SimpleModelDeserializer


class TestPropertyMapping(unittest.TestCase):
    """
    Tests for `PropertyMapping`.
    """
    def test_init_with_constructor_name_and_object_property_setter(self):
        self.assertRaises(ValueError, PropertyMapping, object_constructor_parameter_name="a",
                          serialized_property_getter=lambda: None, object_property_setter=lambda: None)

    def test_init_with_constructor_name_but_no_serialized_property_getter_or_name(self):
        self.assertRaises(ValueError, PropertyMapping, object_constructor_parameter_name="a")

    def test_init_with_object_property_name_and_getter_and_setter(self):
        self.assertRaises(ValueError, PropertyMapping, object_property_name="a",
                          object_property_getter=lambda: None, object_property_setter=lambda: None)

    def test_init_with_no_arguments(self):
        property_mapping = PropertyMapping()
        self.assertIsNone(property_mapping.object_property_getter)
        self.assertIsNone(property_mapping.object_property_setter)
        self.assertIsNone(property_mapping.serialized_property_getter)
        self.assertIsNone(property_mapping.serialized_property_setter)
        self.assertIsNone(property_mapping.object_constructor_parameter_name)

    def test_init_with_object__names(self):
        property_mapping = PropertyMapping("a", "constructor_a", serialized_property_getter=lambda: None)
        self.assertIsNotNone(property_mapping.object_property_getter)
        self.assertIsNone(property_mapping.object_property_setter)
        self.assertIsNotNone(property_mapping.object_constructor_parameter_name)

    def test_init_with_object_and_serialized_getters_and_setters(self):
        property_mapping = PropertyMapping(
                serialized_property_getter=lambda: None, serialized_property_setter=lambda: None,
                object_property_getter=lambda: None, object_property_setter=lambda: None)
        self.assertIsNotNone(property_mapping.object_property_getter)
        self.assertIsNotNone(property_mapping.object_property_setter)
        self.assertIsNotNone(property_mapping.serialized_property_getter)
        self.assertIsNotNone(property_mapping.serialized_property_setter)
        self.assertIsNone(property_mapping.object_constructor_parameter_name)


if __name__ == "__main__":
    unittest.main()