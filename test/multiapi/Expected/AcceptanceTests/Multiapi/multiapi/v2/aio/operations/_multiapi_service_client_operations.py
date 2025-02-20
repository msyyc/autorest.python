# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._multiapi_service_client_operations import build_test_different_calls_request, build_test_one_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin:

    @distributed_trace_async
    async def test_one(
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ModelTwo":
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ModelTwo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_test_one_request(
            id=id,
            message=message,
            template_url=self.test_one.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ModelTwo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore


    @distributed_trace_async
    async def test_different_calls(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test.
        :type greeting_in_chinese: str
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

        
        request = build_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            greeting_in_chinese=greeting_in_chinese,
            template_url=self.test_different_calls.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

