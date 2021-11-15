# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def _param_not_set(param_dict, rest_api_name_lower):
    return not any(k for k in param_dict if k.lower() == rest_api_name_lower)
# fmt: off

def build_test_one_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    id = kwargs.pop('id')  # type: int
    message = kwargs.pop('message', None)  # type: Optional[str]

    api_version = "1.0.0"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "id"):
        query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if _param_not_set(query_parameters, "message") and message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    if _param_not_set(query_parameters, "api-version"):
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_test_lro_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lro')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "content-type") and content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_test_lro_and_paging_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/lroAndPaging')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "client-request-id") and client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if _param_not_set(header_parameters, "maxresults") and maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if _param_not_set(header_parameters, "timeout") and timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_test_different_calls_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    greeting_in_english = kwargs.pop('greeting_in_english')  # type: str

    api_version = "1.0.0"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = kwargs.pop("params", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(query_parameters, "api-version"):
        query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {}) or {}  # type: Dict[str, Any]
    if _param_not_set(header_parameters, "greetinginenglish"):
        header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if _param_not_set(header_parameters, "accept"):
        header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class MultiapiServiceClientOperationsMixin(object):

    @distributed_trace
    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """TestOne should be in an FirstVersionOperationsMixin.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        
        request = build_test_one_request(
            id=id,
            message=message,
            template_url=self.test_one.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore


    def _test_lro_initial(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.Product"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Product"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if product is not None:
            _json = self._serialize.body(product, 'Product')
        else:
            _json = None

        request = build_test_lro_request_initial(
            content_type=content_type,
            json=_json,
            template_url=self._test_lro_initial.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _test_lro_initial.metadata = {'url': '/multiapi/lro'}  # type: ignore


    @distributed_trace
    def begin_test_lro(
        self,
        product=None,  # type: Optional["_models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.Product"]
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapi.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~multiapi.v1.models.Product]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Product"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._test_lro_initial(
                product=product,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('Product', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_test_lro.metadata = {'url': '/multiapi/lro'}  # type: ignore

    def _test_lro_and_paging_initial(
        self,
        client_request_id=None,  # type: Optional[str]
        test_lro_and_paging_options=None,  # type: Optional["_models.TestLroAndPagingOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.PagingResult"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _maxresults = None
        _timeout = None
        if test_lro_and_paging_options is not None:
            _maxresults = test_lro_and_paging_options.maxresults
            _timeout = test_lro_and_paging_options.timeout

        request = build_test_lro_and_paging_request_initial(
            client_request_id=client_request_id,
            maxresults=_maxresults,
            timeout=_timeout,
            template_url=self._test_lro_and_paging_initial.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PagingResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _test_lro_and_paging_initial.metadata = {'url': '/multiapi/lroAndPaging'}  # type: ignore


    @distributed_trace
    def begin_test_lro_and_paging(
        self,
        client_request_id=None,  # type: Optional[str]
        test_lro_and_paging_options=None,  # type: Optional["_models.TestLroAndPagingOptions"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[ItemPaged["_models.PagingResult"]]
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group.
        :type test_lro_and_paging_options: ~multiapi.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[~multiapi.v1.models.PagingResult]]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                
                request = build_test_lro_and_paging_request_initial(
                    client_request_id=client_request_id,
                    maxresults=_maxresults,
                    timeout=_timeout,
                    template_url=self.begin_test_lro_and_paging.metadata['url'],
                    headers=kwargs.pop("headers", {}),
                    params=kwargs.pop("params", {}),
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _maxresults = None
                _timeout = None
                if test_lro_and_paging_options is not None:
                    _maxresults = test_lro_and_paging_options.maxresults
                    _timeout = test_lro_and_paging_options.timeout
                
                request = build_test_lro_and_paging_request_initial(
                    client_request_id=client_request_id,
                    maxresults=_maxresults,
                    timeout=_timeout,
                    template_url=next_link,
                    headers=kwargs.pop("headers", {}),
                    params=kwargs.pop("params", {}),
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("PagingResult", pipeline_response)
            list_of_elem = deserialized.values
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PagingResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._test_lro_and_paging_initial(
                client_request_id=client_request_id,
                test_lro_and_paging_options=test_lro_and_paging_options,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            def internal_get_next(next_link=None):
                if next_link is None:
                    return pipeline_response
                else:
                    return get_next(next_link)

            return ItemPaged(
                internal_get_next, extract_data
            )

        if polling is True: polling_method = ARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_test_lro_and_paging.metadata = {'url': '/multiapi/lroAndPaging'}  # type: ignore


    @distributed_trace
    def test_different_calls(
        self,
        greeting_in_english,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test.
        :type greeting_in_english: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        
        request = build_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            template_url=self.test_different_calls.metadata['url'],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {'url': '/multiapi/testDifferentCalls'}  # type: ignore

