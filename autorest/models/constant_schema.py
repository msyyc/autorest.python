import logging
from .base_schema import BaseSchema
from .primitive_schemas import get_primitive_schema
from typing import Dict, Any, Optional

_LOGGER = logging.getLogger(__name__)

class ConstantSchema(BaseSchema):
    """Schema for constants that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param str value: The actual value of this constant.
    :param schema: The schema for the value of this constant.
    :type schema: ~autorest.models.PrimitiveSchema
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        value: str,
        schema: Optional["PrimitiveSchema"]
    ):
        super(ConstantSchema, self).__init__(yaml_data)
        self.value = value
        self.schema = schema

    def get_serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return self.schema.get_serialization_type()

    def get_python_type(self, namespace: Optional[str] = None) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace. Optional
        """
        return self.schema.get_python_type(namespace)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "ConstantSchema":
        name = yaml_data["language"]["python"]["name"] if yaml_data["language"]["python"].get('name') else ""
        _LOGGER.info("Parsing %s constant", name)
        return cls(
            yaml_data=yaml_data,
            value=yaml_data.get("value", {}).get("value", None),
            schema=get_primitive_schema(yaml_data['valueType'])
        )