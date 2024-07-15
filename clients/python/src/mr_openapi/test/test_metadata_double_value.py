"""Model Registry REST API.

REST API for Model Registry to create and manage ML model metadata

The version of the OpenAPI document: v1alpha3
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from mr_openapi.models.metadata_double_value import MetadataDoubleValue


class TestMetadataDoubleValue(unittest.TestCase):
    """MetadataDoubleValue unit test stubs."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataDoubleValue:
        """Test MetadataDoubleValue
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included.
        """
        # uncomment below to create an instance of `MetadataDoubleValue`
        """
        model = MetadataDoubleValue()
        if include_optional:
            return MetadataDoubleValue(
                double_value = 1.337,
                metadata_type = 'MetadataDoubleValue'
            )
        else:
            return MetadataDoubleValue(
                double_value = 1.337,
                metadata_type = 'MetadataDoubleValue',
        )
        """

    def testMetadataDoubleValue(self):
        """Test MetadataDoubleValue."""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()