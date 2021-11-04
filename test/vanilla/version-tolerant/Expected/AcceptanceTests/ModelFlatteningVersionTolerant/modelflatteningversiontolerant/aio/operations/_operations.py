# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
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

from ...operations._operations import (
    build_get_array_request,
    build_get_dictionary_request,
    build_get_resource_collection_request,
    build_get_wrapped_array_request,
    build_post_flattened_simple_product_request,
    build_put_array_request,
    build_put_dictionary_request,
    build_put_resource_collection_request,
    build_put_simple_product_request,
    build_put_simple_product_with_grouping_request,
    build_put_wrapped_array_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestResourceFlatteningTestServiceOperationsMixin:
    @distributed_trace_async
    async def put_array(self, resource_array: Optional[List[JSONType]] = None, **kwargs: Any) -> None:
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[JSONType]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_array = [
                    {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_array is not None:
            json = resource_array
        else:
            json = None

        request = build_put_array_request(
            content_type=content_type,
            json=json,
            template_url=self.put_array.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def get_array(self, **kwargs: Any) -> List[JSONType]:
        """Get External Resource as an Array.

        :return: list of JSON object
        :rtype: list[JSONType]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == [
                    {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List[JSONType]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_array_request(
            template_url=self.get_array.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_array.metadata = {"url": "/model-flatten/array"}  # type: ignore

    @distributed_trace_async
    async def put_wrapped_array(self, resource_array: Optional[List[JSONType]] = None, **kwargs: Any) -> None:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :param resource_array: External Resource as an Array to put.
        :type resource_array: list[JSONType]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_array = [
                    {
                        "value": "str"  # Optional. the product value.
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_array is not None:
            json = resource_array
        else:
            json = None

        request = build_put_wrapped_array_request(
            content_type=content_type,
            json=json,
            template_url=self.put_wrapped_array.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def get_wrapped_array(self, **kwargs: Any) -> List[JSONType]:
        """No need to have a route in Express server for this operation. Used to verify the type flattened
        is not removed if it's referenced in an array.

        :return: list of JSON object
        :rtype: list[JSONType]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == [
                    {
                        "property": {
                            "value": "str"  # Optional. the product value.
                        }
                    }
                ]
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[List[JSONType]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_wrapped_array_request(
            template_url=self.get_wrapped_array.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_wrapped_array.metadata = {"url": "/model-flatten/wrappedarray"}  # type: ignore

    @distributed_trace_async
    async def put_dictionary(self, resource_dictionary: Optional[Dict[str, JSONType]] = None, **kwargs: Any) -> None:
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put.
        :type resource_dictionary: dict[str, JSONType]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_dictionary = {
                    "str": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_dictionary is not None:
            json = resource_dictionary
        else:
            json = None

        request = build_put_dictionary_request(
            content_type=content_type,
            json=json,
            template_url=self.put_dictionary.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def get_dictionary(self, **kwargs: Any) -> Dict[str, JSONType]:
        """Get External Resource as a Dictionary.

        :return: dict mapping str to JSON object
        :rtype: dict[str, JSONType]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, JSONType]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_dictionary_request(
            template_url=self.get_dictionary.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_dictionary.metadata = {"url": "/model-flatten/dictionary"}  # type: ignore

    @distributed_trace_async
    async def put_resource_collection(self, resource_complex_object: JSONType = None, **kwargs: Any) -> None:
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a ResourceCollection to put.
        :type resource_complex_object: JSONType
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                resource_complex_object = {
                    "arrayofresources": [
                        {
                            "id": "str",  # Optional. Resource Id.
                            "location": "str",  # Optional. Resource Location.
                            "name": "str",  # Optional. Resource Name.
                            "properties": {
                                "p.name": "str",  # Optional.
                                "provisioningState": "str",  # Optional.
                                "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                                "type": "str"  # Optional.
                            },
                            "tags": {
                                "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                            },
                            "type": "str"  # Optional. Resource Type.
                        }
                    ],
                    "dictionaryofresources": {
                        "str": {
                            "id": "str",  # Optional. Resource Id.
                            "location": "str",  # Optional. Resource Location.
                            "name": "str",  # Optional. Resource Name.
                            "properties": {
                                "p.name": "str",  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                                "provisioningState": "str",  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                                "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                                "type": "str"  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                            },
                            "tags": {
                                "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                            },
                            "type": "str"  # Optional. Resource Type.
                        }
                    },
                    "productresource": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional. Flattened product.
                            "provisioningState": "str",  # Optional. Flattened product.
                            "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                            "type": "str"  # Optional. Flattened product.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if resource_complex_object is not None:
            json = resource_complex_object
        else:
            json = None

        request = build_put_resource_collection_request(
            content_type=content_type,
            json=json,
            template_url=self.put_resource_collection.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def get_resource_collection(self, **kwargs: Any) -> JSONType:
        """Get External Resource as a ResourceCollection.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "arrayofresources": [
                        {
                            "id": "str",  # Optional. Resource Id.
                            "location": "str",  # Optional. Resource Location.
                            "name": "str",  # Optional. Resource Name.
                            "properties": {
                                "p.name": "str",  # Optional.
                                "provisioningState": "str",  # Optional.
                                "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                                "type": "str"  # Optional.
                            },
                            "tags": {
                                "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                            },
                            "type": "str"  # Optional. Resource Type.
                        }
                    ],
                    "dictionaryofresources": {
                        "str": {
                            "id": "str",  # Optional. Resource Id.
                            "location": "str",  # Optional. Resource Location.
                            "name": "str",  # Optional. Resource Name.
                            "properties": {
                                "p.name": "str",  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                                "provisioningState": "str",  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                                "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                                "type": "str"  # Optional. Dictionary of :code:`<FlattenedProduct>`.
                            },
                            "tags": {
                                "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                            },
                            "type": "str"  # Optional. Resource Type.
                        }
                    },
                    "productresource": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional. Flattened product.
                            "provisioningState": "str",  # Optional. Flattened product.
                            "provisioningStateValues": "str",  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                            "type": "str"  # Optional. Flattened product.
                        },
                        "tags": {
                            "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_resource_collection_request(
            template_url=self.get_resource_collection.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_resource_collection.metadata = {"url": "/model-flatten/resourcecollection"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product(self, simple_body_product: JSONType = None, **kwargs: Any) -> JSONType:
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put.
        :type simple_body_product: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_put_simple_product_request(
            content_type=content_type,
            json=json,
            template_url=self.put_simple_product.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def post_flattened_simple_product(self, simple_body_product: JSONType = None, **kwargs: Any) -> JSONType:
        """Put Flattened Simple Product with client flattening true on the parameter.

        :param simple_body_product: Simple body product to post.
        :type simple_body_product: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_post_flattened_simple_product_request(
            content_type=content_type,
            json=json,
            template_url=self.post_flattened_simple_product.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_flattened_simple_product.metadata = {"url": "/model-flatten/customFlattening"}  # type: ignore

    @distributed_trace_async
    async def put_simple_product_with_grouping(
        self, name: str, simple_body_product: JSONType = None, **kwargs: Any
    ) -> JSONType:
        """Put Simple Product with client flattening true on the model.

        :param name: Product name with value 'groupproduct'.
        :type name: str
        :param simple_body_product: Simple body product to put.
        :type simple_body_product: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                simple_body_product = {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }

                # response body for status code(s): 200
                response.json() == {
                    "base_product_description": "str",  # Optional. Description of product.
                    "base_product_id": "str",  # Required. Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles.
                    "details": {
                        "max_product_capacity": "Large",  # Default value is "Large". Capacity of product. For example, 4 people. Has constant value: "Large".
                        "max_product_display_name": "str",  # Required. Display name of product.
                        "max_product_image": {
                            "@odata.value": "str",  # Optional. URL value.
                            "generic_value": "str"  # Optional. Generic URL value.
                        }
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if simple_body_product is not None:
            json = simple_body_product
        else:
            json = None

        request = build_put_simple_product_with_grouping_request(
            name=name,
            content_type=content_type,
            json=json,
            template_url=self.put_simple_product_with_grouping.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_simple_product_with_grouping.metadata = {"url": "/model-flatten/customFlattening/parametergrouping/{name}/"}  # type: ignore
