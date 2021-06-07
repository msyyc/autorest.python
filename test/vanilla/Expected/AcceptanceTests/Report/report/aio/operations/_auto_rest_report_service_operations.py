# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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

from ... import _rest, models as _models

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestReportServiceOperationsMixin:
    @distributed_trace_async
    async def get_report(self, qualifier: Optional[str] = None, **kwargs: Any) -> Dict[str, int]:
        """Get test coverage report.

        :param qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5' in
         for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :type qualifier: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to int, or the result of cls(response)
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_report_request(
            qualifier=qualifier, template_url=self.get_report.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{int}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_report.metadata = {"url": "/report"}  # type: ignore

    @distributed_trace_async
    async def get_optional_report(self, qualifier: Optional[str] = None, **kwargs: Any) -> Dict[str, int]:
        """Get optional test coverage report.

        :param qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5' in
         for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :type qualifier: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to int, or the result of cls(response)
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_optional_report_request(
            qualifier=qualifier, template_url=self.get_optional_report.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{int}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_optional_report.metadata = {"url": "/report/optional"}  # type: ignore
