# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from .parameter import Parameter, ParameterLocation, ParameterStyle

class RequestParameter(Parameter):

    @property
    def in_method_signature(self) -> bool:
        if self.serialized_name == "field":
            a = "b"
        return not(
            # If I only have one value, I can't be set, so no point being in signature
            self.constant
            # If i'm not in the method code, no point in being in signature
            or not self.in_method_code
            # If I'm grouped, my grouper will be on signature, not me
            or self.target_property_name
            or self.grouped_by
            # If I'm a kwarg, don't include in the signature
            or self.is_kwarg
        )

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Parameter":
        http_protocol = yaml_data["protocol"].get("http", {"in": ParameterLocation.Other})
        name = yaml_data["language"]["default"]["name"]
        location = ParameterLocation(http_protocol["in"])
        if location == ParameterLocation.Body:
            name = "body"
        return cls(
            yaml_data=yaml_data,
            schema=yaml_data.get("schema", None),  # FIXME replace by operation model
            # See also https://github.com/Azure/autorest.modelerfour/issues/80
            rest_api_name=yaml_data["language"]["default"].get(
                "serializedName", name
            ),
            serialized_name=name,
            description=yaml_data["language"]["python"]["description"],
            implementation=yaml_data["implementation"],
            required=yaml_data.get("required", False),
            location=location,
            skip_url_encoding=yaml_data.get("extensions", {}).get("x-ms-skip-url-encoding", False),
            constraints=[],  # FIXME constraints
            target_property_name=id(yaml_data["targetProperty"]) if yaml_data.get("targetProperty") else None,
            style=ParameterStyle(http_protocol["style"]) if "style" in http_protocol else None,
            explode=http_protocol.get("explode", False),
            grouped_by=yaml_data.get("groupedBy", None),
            original_parameter=yaml_data.get("originalParameter", None),
            flattened=yaml_data.get("flattened", False),
            client_default_value=yaml_data.get("clientDefaultValue"),
        )