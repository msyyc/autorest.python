# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.rest import HttpRequest

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, IO, Optional, TypeVar, Union

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_head_no_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Head request, no params. Initially has no query parameters. After evolution, a new optional
    query parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword new_parameter: I'm a new input optional parameter. Default value is None.
    :paramtype new_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    new_parameter = kwargs.pop('new_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if new_parameter is not None:
        _query_parameters['new_parameter'] = _SERIALIZER.query("new_parameter", new_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="HEAD",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.
     Initially only has one required Query Parameter. After evolution, a new optional query
    parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword parameter: I am a required parameter.
    :paramtype parameter: str
    :keyword new_parameter: I'm a new input optional parameter. Default value is None.
    :paramtype new_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    parameter = kwargs.pop('parameter')  # type: str
    new_parameter = kwargs.pop('new_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['parameter'] = _SERIALIZER.query("parameter", parameter, 'str')
    if new_parameter is not None:
        _query_parameters['new_parameter'] = _SERIALIZER.query("new_parameter", new_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_put_required_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Initially has one required query parameter and one optional query parameter.  After evolution,
    a new optional query parameter is added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword required_param: I am a required parameter.
    :paramtype required_param: str
    :keyword optional_param: I am an optional parameter. Default value is None.
    :paramtype optional_param: str
    :keyword new_parameter: I'm a new input optional parameter. Default value is None.
    :paramtype new_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    required_param = kwargs.pop('required_param')  # type: str
    optional_param = kwargs.pop('optional_param', None)  # type: Optional[str]
    new_parameter = kwargs.pop('new_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['requiredParam'] = _SERIALIZER.query("required_param", required_param, 'str')
    if optional_param is not None:
        _query_parameters['optionalParam'] = _SERIALIZER.query("optional_param", optional_param, 'str')
    if new_parameter is not None:
        _query_parameters['new_parameter'] = _SERIALIZER.query("new_parameter", new_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_post_parameters_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """POST a JSON or a JPEG.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. I am a body parameter with a new content type. My only
     valid JSON entry is { url: "http://example.org/myimage.jpeg" }. Default value is None.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). I am a body parameter with a new content type. My only valid
     JSON entry is { url: "http://example.org/myimage.jpeg" }. Default value is None.
    :paramtype content: any
    :keyword content_type: Media type of the body sent to the API. Possible values are:
     "application/json" or "image/jpeg". Default value is None.
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "url": "str"  # Required.
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/parameters"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_delete_parameters_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Delete something.
     Initially the path exists but there is no delete method. After evolution this is a new method
    in a known path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    _url = "/serviceDriven/parameters"

    return HttpRequest(
        method="DELETE",
        url=_url,
        **kwargs
    )


def build_get_optional_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.
     Initially has one optional query parameter. After evolution, a new optional query parameter is
    added.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword optional_param: I am an optional parameter. Default value is None.
    :paramtype optional_param: str
    :keyword new_parameter: I'm a new input optional parameter. Default value is None.
    :paramtype new_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    optional_param = kwargs.pop('optional_param', None)  # type: Optional[str]
    new_parameter = kwargs.pop('new_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/moreParameters"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if optional_param is not None:
        _query_parameters['optionalParam'] = _SERIALIZER.query("optional_param", optional_param, 'str')
    if new_parameter is not None:
        _query_parameters['new_parameter'] = _SERIALIZER.query("new_parameter", new_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_new_operation_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """I'm a new operation.
     Initiallty neither path or method exist for this operation. After evolution, this is a new
    method in a new path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/serviceDriven/newPath"

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )
