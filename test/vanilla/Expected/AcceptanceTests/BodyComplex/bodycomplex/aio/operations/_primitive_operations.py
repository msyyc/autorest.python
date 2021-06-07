# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._rest import primitive as rest_primitive

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PrimitiveOperations:
    """PrimitiveOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_int(self, **kwargs: Any) -> "_models.IntWrapper":
        """Get complex types with integer properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.IntWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.IntWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_int_request(
            template_url=self.get_int.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("IntWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_int.metadata = {"url": "/complex/primitive/integer"}  # type: ignore

    @distributed_trace_async
    async def put_int(self, complex_body: "_models.IntWrapper", **kwargs: Any) -> None:
        """Put complex types with integer properties.

        :param complex_body: Please put -1 and 2.
        :type complex_body: ~bodycomplex.models.IntWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "IntWrapper")

        request = rest_primitive.build_put_int_request(
            json=json, content_type=content_type, template_url=self.put_int.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_int.metadata = {"url": "/complex/primitive/integer"}  # type: ignore

    @distributed_trace_async
    async def get_long(self, **kwargs: Any) -> "_models.LongWrapper":
        """Get complex types with long properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LongWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.LongWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.LongWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_long_request(
            template_url=self.get_long.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("LongWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_long.metadata = {"url": "/complex/primitive/long"}  # type: ignore

    @distributed_trace_async
    async def put_long(self, complex_body: "_models.LongWrapper", **kwargs: Any) -> None:
        """Put complex types with long properties.

        :param complex_body: Please put 1099511627775 and -999511627788.
        :type complex_body: ~bodycomplex.models.LongWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "LongWrapper")

        request = rest_primitive.build_put_long_request(
            json=json, content_type=content_type, template_url=self.put_long.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_long.metadata = {"url": "/complex/primitive/long"}  # type: ignore

    @distributed_trace_async
    async def get_float(self, **kwargs: Any) -> "_models.FloatWrapper":
        """Get complex types with float properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FloatWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.FloatWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.FloatWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_float_request(
            template_url=self.get_float.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("FloatWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_float.metadata = {"url": "/complex/primitive/float"}  # type: ignore

    @distributed_trace_async
    async def put_float(self, complex_body: "_models.FloatWrapper", **kwargs: Any) -> None:
        """Put complex types with float properties.

        :param complex_body: Please put 1.05 and -0.003.
        :type complex_body: ~bodycomplex.models.FloatWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "FloatWrapper")

        request = rest_primitive.build_put_float_request(
            json=json, content_type=content_type, template_url=self.put_float.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_float.metadata = {"url": "/complex/primitive/float"}  # type: ignore

    @distributed_trace_async
    async def get_double(self, **kwargs: Any) -> "_models.DoubleWrapper":
        """Get complex types with double properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DoubleWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.DoubleWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DoubleWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_double_request(
            template_url=self.get_double.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DoubleWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_double.metadata = {"url": "/complex/primitive/double"}  # type: ignore

    @distributed_trace_async
    async def put_double(self, complex_body: "_models.DoubleWrapper", **kwargs: Any) -> None:
        """Put complex types with double properties.

        :param complex_body: Please put 3e-100 and
         -0.000000000000000000000000000000000000000000000000000000005.
        :type complex_body: ~bodycomplex.models.DoubleWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "DoubleWrapper")

        request = rest_primitive.build_put_double_request(
            json=json, content_type=content_type, template_url=self.put_double.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_double.metadata = {"url": "/complex/primitive/double"}  # type: ignore

    @distributed_trace_async
    async def get_bool(self, **kwargs: Any) -> "_models.BooleanWrapper":
        """Get complex types with bool properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BooleanWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.BooleanWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.BooleanWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_bool_request(
            template_url=self.get_bool.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("BooleanWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_bool.metadata = {"url": "/complex/primitive/bool"}  # type: ignore

    @distributed_trace_async
    async def put_bool(self, complex_body: "_models.BooleanWrapper", **kwargs: Any) -> None:
        """Put complex types with bool properties.

        :param complex_body: Please put true and false.
        :type complex_body: ~bodycomplex.models.BooleanWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "BooleanWrapper")

        request = rest_primitive.build_put_bool_request(
            json=json, content_type=content_type, template_url=self.put_bool.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_bool.metadata = {"url": "/complex/primitive/bool"}  # type: ignore

    @distributed_trace_async
    async def get_string(self, **kwargs: Any) -> "_models.StringWrapper":
        """Get complex types with string properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StringWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.StringWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.StringWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_string_request(
            template_url=self.get_string.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("StringWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_string.metadata = {"url": "/complex/primitive/string"}  # type: ignore

    @distributed_trace_async
    async def put_string(self, complex_body: "_models.StringWrapper", **kwargs: Any) -> None:
        """Put complex types with string properties.

        :param complex_body: Please put 'goodrequest', '', and null.
        :type complex_body: ~bodycomplex.models.StringWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "StringWrapper")

        request = rest_primitive.build_put_string_request(
            json=json, content_type=content_type, template_url=self.put_string.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_string.metadata = {"url": "/complex/primitive/string"}  # type: ignore

    @distributed_trace_async
    async def get_date(self, **kwargs: Any) -> "_models.DateWrapper":
        """Get complex types with date properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DateWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.DateWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DateWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_date_request(
            template_url=self.get_date.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DateWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_date.metadata = {"url": "/complex/primitive/date"}  # type: ignore

    @distributed_trace_async
    async def put_date(self, complex_body: "_models.DateWrapper", **kwargs: Any) -> None:
        """Put complex types with date properties.

        :param complex_body: Please put '0001-01-01' and '2016-02-29'.
        :type complex_body: ~bodycomplex.models.DateWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "DateWrapper")

        request = rest_primitive.build_put_date_request(
            json=json, content_type=content_type, template_url=self.put_date.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_date.metadata = {"url": "/complex/primitive/date"}  # type: ignore

    @distributed_trace_async
    async def get_date_time(self, **kwargs: Any) -> "_models.DatetimeWrapper":
        """Get complex types with datetime properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatetimeWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.DatetimeWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DatetimeWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_date_time_request(
            template_url=self.get_date_time.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DatetimeWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_date_time.metadata = {"url": "/complex/primitive/datetime"}  # type: ignore

    @distributed_trace_async
    async def put_date_time(self, complex_body: "_models.DatetimeWrapper", **kwargs: Any) -> None:
        """Put complex types with datetime properties.

        :param complex_body: Please put '0001-01-01T12:00:00-04:00' and '2015-05-18T11:38:00-08:00'.
        :type complex_body: ~bodycomplex.models.DatetimeWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "DatetimeWrapper")

        request = rest_primitive.build_put_date_time_request(
            json=json, content_type=content_type, template_url=self.put_date_time.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_date_time.metadata = {"url": "/complex/primitive/datetime"}  # type: ignore

    @distributed_trace_async
    async def get_date_time_rfc1123(self, **kwargs: Any) -> "_models.Datetimerfc1123Wrapper":
        """Get complex types with datetimeRfc1123 properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Datetimerfc1123Wrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.Datetimerfc1123Wrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Datetimerfc1123Wrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_date_time_rfc1123_request(
            template_url=self.get_date_time_rfc1123.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Datetimerfc1123Wrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_date_time_rfc1123.metadata = {"url": "/complex/primitive/datetimerfc1123"}  # type: ignore

    @distributed_trace_async
    async def put_date_time_rfc1123(self, complex_body: "_models.Datetimerfc1123Wrapper", **kwargs: Any) -> None:
        """Put complex types with datetimeRfc1123 properties.

        :param complex_body: Please put 'Mon, 01 Jan 0001 12:00:00 GMT' and 'Mon, 18 May 2015 11:38:00
         GMT'.
        :type complex_body: ~bodycomplex.models.Datetimerfc1123Wrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(complex_body, "Datetimerfc1123Wrapper")

        request = rest_primitive.build_put_date_time_rfc1123_request(
            json=json, content_type=content_type, template_url=self.put_date_time_rfc1123.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_date_time_rfc1123.metadata = {"url": "/complex/primitive/datetimerfc1123"}  # type: ignore

    @distributed_trace_async
    async def get_duration(self, **kwargs: Any) -> "_models.DurationWrapper":
        """Get complex types with duration properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DurationWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.DurationWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DurationWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_duration_request(
            template_url=self.get_duration.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DurationWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_duration.metadata = {"url": "/complex/primitive/duration"}  # type: ignore

    @distributed_trace_async
    async def put_duration(self, field: Optional[datetime.timedelta] = None, **kwargs: Any) -> None:
        """Put complex types with duration properties.

        :param field:
        :type field: ~datetime.timedelta
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        _complex_body = _models.DurationWrapper(field=field)
        json = None
        json = self._serialize.body(_complex_body, "DurationWrapper")

        request = rest_primitive.build_put_duration_request(
            json=json, content_type=content_type, template_url=self.put_duration.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_duration.metadata = {"url": "/complex/primitive/duration"}  # type: ignore

    @distributed_trace_async
    async def get_byte(self, **kwargs: Any) -> "_models.ByteWrapper":
        """Get complex types with byte properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ByteWrapper, or the result of cls(response)
        :rtype: ~bodycomplex.models.ByteWrapper
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ByteWrapper"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_primitive.build_get_byte_request(
            template_url=self.get_byte.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ByteWrapper", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_byte.metadata = {"url": "/complex/primitive/byte"}  # type: ignore

    @distributed_trace_async
    async def put_byte(self, field: Optional[bytearray] = None, **kwargs: Any) -> None:
        """Put complex types with byte properties.

        :param field:
        :type field: bytearray
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        _complex_body = _models.ByteWrapper(field=field)
        json = None
        json = self._serialize.body(_complex_body, "ByteWrapper")

        request = rest_primitive.build_put_byte_request(
            json=json, content_type=content_type, template_url=self.put_byte.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_byte.metadata = {"url": "/complex/primitive/byte"}  # type: ignore
