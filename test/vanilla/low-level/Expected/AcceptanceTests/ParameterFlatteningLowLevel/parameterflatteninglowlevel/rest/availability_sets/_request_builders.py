# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)


# fmt: off

def build_update_request(
    resource_group_name,  # type: str
    avset,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Updates the tags for an availability set.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param avset: The name of the storage availability set.
    :type avset: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. The tags.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). The tags.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "tags": {
                    "str": "str"  # Required. A set of tags. A description about the set of tags.
                }
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/parameterFlattening/{resourceGroupName}/{availabilitySetName}')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "availabilitySetName": _SERIALIZER.url("avset", avset, 'str', max_length=80, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "content-type") and content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        headers=header_parameters,
        **kwargs
    )
