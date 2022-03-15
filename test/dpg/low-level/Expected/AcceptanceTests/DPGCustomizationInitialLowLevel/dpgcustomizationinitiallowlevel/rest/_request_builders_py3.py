# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.rest import HttpRequest

from .._vendor import _format_url_section

T = TypeVar("T")
JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_model_request(mode: str, **kwargs: Any) -> HttpRequest:
    """Get models that you will either return to end users as a raw body, or with a model added during
    grow up.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "received": "str"  # Required. Possible values include: "raw", "model".
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_post_model_request(mode: str, *, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
    take a model instead, and put in 'model' as mode.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users.
    :type mode: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Please put {'hello': 'world!'}. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Please put {'hello': 'world!'}. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "hello": "str"  # Required.
            }

            # response body for status code(s): 200
            response.json() == {
                "received": "str"  # Required. Possible values include: "raw", "model".
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_header_parameters, json=json, content=content, **kwargs)


def build_get_pages_request(mode: str, **kwargs: Any) -> HttpRequest:
    """Get pages that you will either return to users in pages of raw bodies, or pages of models
    following growup.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str",  # Optional.
                "values": [
                    {
                        "received": "str"  # Required. Possible values include:
                          "raw", "model".
                    }
                ]
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/customization/paging/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_header_parameters, **kwargs)


def build_lro_request(mode: str, **kwargs: Any) -> HttpRequest:
    """Long running put request that will either return to end users a final payload of a raw body, or
    a final payload of a model after the SDK has grown up.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
     with the raw body, and 'model' if you are going to convert the raw body to a customized body
     before returning to users.
    :type mode: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "provisioningState": "str",  # Required.
                "received": "str"  # Required. Possible values include: "raw", "model".
            }
    """

    accept = "application/json"
    # Construct URL
    _url = "/customization/lro/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_header_parameters, **kwargs)
