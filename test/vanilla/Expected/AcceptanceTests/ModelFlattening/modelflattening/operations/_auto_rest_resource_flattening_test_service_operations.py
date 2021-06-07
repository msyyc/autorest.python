# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import _rest, models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class AutoRestResourceFlatteningTestServiceOperationsMixin(object):
    @distributed_trace
    def put_array(
        self,
        resource_array=None,  # type: Optional[List["_models.Resource"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.Resource]
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
        if resource_array is not None:
            json = self._serialize.body(resource_array, "[Resource]")

        request = _rest.build_put_array_request(
            json=json, content_type=content_type, template_url=self.put_array.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace
    def get_array(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.FlattenedProduct"]
        """Get External Resource as an Array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of FlattenedProduct, or the result of cls(response)
        :rtype: list[~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.FlattenedProduct"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_array_request(template_url=self.get_array.metadata["url"], **kwargs)._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("[FlattenedProduct]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace
    def put_wrapped_array(
        self,
        resource_array=None,  # type: Optional[List["_models.WrappedProduct"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[~modelflattening.models.WrappedProduct]
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
        if resource_array is not None:
            json = self._serialize.body(resource_array, "[WrappedProduct]")

        request = _rest.build_put_wrapped_array_request(
            json=json, content_type=content_type, template_url=self.put_wrapped_array.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace
    def get_wrapped_array(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.ProductWrapper"]
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ProductWrapper, or the result of cls(response)
        :rtype: list[~modelflattening.models.ProductWrapper]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List["_models.ProductWrapper"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_wrapped_array_request(
            template_url=self.get_wrapped_array.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("[ProductWrapper]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace
    def put_dictionary(
        self,
        resource_dictionary=None,  # type: Optional[Dict[str, "_models.FlattenedProduct"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, ~modelflattening.models.FlattenedProduct]
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
        if resource_dictionary is not None:
            json = self._serialize.body(resource_dictionary, "{FlattenedProduct}")

        request = _rest.build_put_dictionary_request(
            json=json, content_type=content_type, template_url=self.put_dictionary.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace
    def get_dictionary(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Dict[str, "_models.FlattenedProduct"]
        """Get External Resource as a Dictionary.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: dict mapping str to FlattenedProduct, or the result of cls(response)
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, "_models.FlattenedProduct"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_dictionary_request(
            template_url=self.get_dictionary.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("{FlattenedProduct}", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace
    def put_resource_collection(
        self,
        resource_complex_object=None,  # type: Optional["_models.ResourceCollection"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: ~modelflattening.models.ResourceCollection
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
        if resource_complex_object is not None:
            json = self._serialize.body(resource_complex_object, "ResourceCollection")

        request = _rest.build_put_resource_collection_request(
            json=json, content_type=content_type, template_url=self.put_resource_collection.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace
    def get_resource_collection(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ResourceCollection"
        """Get External Resource as a ResourceCollection.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ResourceCollection, or the result of cls(response)
        :rtype: ~modelflattening.models.ResourceCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ResourceCollection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_resource_collection_request(
            template_url=self.get_resource_collection.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("ResourceCollection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace
    def put_simple_product(
        self,
        simple_body_product=None,  # type: Optional["_models.SimpleProduct"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        if simple_body_product is not None:
            json = self._serialize.body(simple_body_product, "SimpleProduct")

        request = _rest.build_put_simple_product_request(
            json=json, content_type=content_type, template_url=self.put_simple_product.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace
    def post_flattened_simple_product(
        self,
        product_id,  # type: str
        description=None,  # type: Optional[str]
        max_product_display_name=None,  # type: Optional[str]
        generic_value=None,  # type: Optional[str]
        odata_value=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SimpleProduct"
        """Put Flattened Simple Product with client flattening true on the parameter.

        :param product_id: Unique identifier representing a specific product for a given latitude &
         longitude. For example, uberX in San Francisco will have a different product_id than uberX in
         Los Angeles.
        :type product_id: str
        :param description: Description of product.
        :type description: str
        :param max_product_display_name: Display name of product.
        :type max_product_display_name: str
        :param generic_value: Generic URL value.
        :type generic_value: str
        :param odata_value: URL value.
        :type odata_value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        _simple_body_product = _models.SimpleProduct(
            product_id=product_id,
            description=description,
            max_product_display_name=max_product_display_name,
            generic_value=generic_value,
            odata_value=odata_value,
        )
        json = None
        if _simple_body_product is not None:
            json = self._serialize.body(_simple_body_product, "SimpleProduct")

        request = _rest.build_post_flattened_simple_product_request(
            json=json,
            content_type=content_type,
            template_url=self.post_flattened_simple_product.metadata["url"],
            **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_flattened_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace
    def put_simple_product_with_grouping(
        self,
        flatten_parameter_group,  # type: "_models.FlattenParameterGroup"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SimpleProduct"
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Parameter group.
        :type flatten_parameter_group: ~modelflattening.models.FlattenParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimpleProduct, or the result of cls(response)
        :rtype: ~modelflattening.models.SimpleProduct
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.SimpleProduct"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        _name = None
        _simple_body_product = None
        _product_id = None
        _description = None
        _max_product_display_name = None
        _generic_value = None
        _odata_value = None
        if flatten_parameter_group is not None:
            _name = flatten_parameter_group.name
            _simple_body_product = flatten_parameter_group.simple_body_product
            _product_id = flatten_parameter_group.product_id
            _description = flatten_parameter_group.description
            _max_product_display_name = flatten_parameter_group.max_product_display_name
            _generic_value = flatten_parameter_group.generic_value
            _odata_value = flatten_parameter_group.odata_value
        _simple_body_product = _models.SimpleProduct(
            product_id=_product_id,
            description=_description,
            max_product_display_name=_max_product_display_name,
            generic_value=_generic_value,
            odata_value=_odata_value,
        )
        json = None
        if _simple_body_product is not None:
            json = self._serialize.body(_simple_body_product, "SimpleProduct")

        request = _rest.build_put_simple_product_with_grouping_request(
            name=_name,
            json=json,
            content_type=content_type,
            template_url=self.put_simple_product_with_grouping.metadata["url"],
            **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimpleProduct", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product_with_grouping.metadata = {"url": "/model-flatten/customFlattening/parametergrouping/{name}/"}  # type: ignore
