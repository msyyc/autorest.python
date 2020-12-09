# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ContantsOperations:
    """ContantsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~constants.models
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
    async def put_no_model_as_string_no_required_two_value_no_default(
        self,
        input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_no_required_two_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_no_default.metadata = {'url': '/constants/putNoModelAsStringNoRequiredTwoValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_two_value_default(
        self,
        input: Optional[Union[str, "_models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.NoModelAsStringNoRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_no_required_two_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_two_value_default.metadata = {'url': '/constants/putNoModelAsStringNoRequiredTwoValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_no_default(
        self,
        input: Optional[str] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_no_required_one_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_no_default.metadata = {'url': '/constants/putNoModelAsStringNoRequiredOneValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_no_required_one_value_default(
        self,
        input: Optional[str] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_no_required_one_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_no_required_one_value_default.metadata = {'url': '/constants/putNoModelAsStringNoRequiredOneValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_no_default(
        self,
        input: Union[str, "_models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum"],
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_required_two_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_no_default.metadata = {'url': '/constants/putNoModelAsStringRequiredTwoValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_two_value_default(
        self,
        input: Union[str, "_models.NoModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.NoModelAsStringRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_no_model_as_string_required_two_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_two_value_default.metadata = {'url': '/constants/putNoModelAsStringRequiredTwoValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_no_default(
        self,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        input = "value1"

        # Construct URL
        url = self.put_no_model_as_string_required_one_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_no_default.metadata = {'url': '/constants/putNoModelAsStringRequiredOneValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_no_model_as_string_required_one_value_default(
        self,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        input = "value1"

        # Construct URL
        url = self.put_no_model_as_string_required_one_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_no_model_as_string_required_one_value_default.metadata = {'url': '/constants/putNoModelAsStringRequiredOneValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_no_default(
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_no_required_two_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_no_default.metadata = {'url': '/constants/putModelAsStringNoRequiredTwoValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_two_value_default(
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredTwoValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringNoRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_no_required_two_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_two_value_default.metadata = {'url': '/constants/putModelAsStringNoRequiredTwoValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_no_default(
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum"]] = None,
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_no_required_one_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_no_default.metadata = {'url': '/constants/putModelAsStringNoRequiredOneValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_no_required_one_value_default(
        self,
        input: Optional[Union[str, "_models.ModelAsStringNoRequiredOneValueDefaultOpEnum"]] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringNoRequiredOneValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_no_required_one_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if input is not None:
            query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_no_required_one_value_default.metadata = {'url': '/constants/putModelAsStringNoRequiredOneValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_no_default(
        self,
        input: Union[str, "_models.ModelAsStringRequiredTwoValueNoDefaultOpEnum"],
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_required_two_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_no_default.metadata = {'url': '/constants/putModelAsStringRequiredTwoValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_two_value_default(
        self,
        input: Union[str, "_models.ModelAsStringRequiredTwoValueDefaultOpEnum"] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredTwoValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_required_two_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_two_value_default.metadata = {'url': '/constants/putModelAsStringRequiredTwoValueDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_no_default(
        self,
        input: Union[str, "_models.ModelAsStringRequiredOneValueNoDefaultOpEnum"],
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueNoDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_required_one_value_no_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_no_default.metadata = {'url': '/constants/putModelAsStringRequiredOneValueNoDefault'}  # type: ignore

    @distributed_trace_async
    async def put_model_as_string_required_one_value_default(
        self,
        input: Union[str, "_models.ModelAsStringRequiredOneValueDefaultOpEnum"] = "value1",
        **kwargs: Any
    ) -> None:
        """Puts constants to the testserver.

        Puts constants to the testserver.

        :param input:
        :type input: str or ~constants.models.ModelAsStringRequiredOneValueDefaultOpEnum
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.put_model_as_string_required_one_value_default.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['input'] = self._serialize.query("input", input, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_model_as_string_required_one_value_default.metadata = {'url': '/constants/putModelAsStringRequiredOneValueDefault'}  # type: ignore
