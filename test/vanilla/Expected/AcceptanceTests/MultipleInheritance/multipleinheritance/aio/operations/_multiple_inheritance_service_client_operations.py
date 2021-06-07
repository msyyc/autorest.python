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


class MultipleInheritanceServiceClientOperationsMixin:
    @distributed_trace_async
    async def get_horse(self, **kwargs: Any) -> "_models.Horse":
        """Get a horse with name 'Fred' and isAShowHorse true.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Horse, or the result of cls(response)
        :rtype: ~multipleinheritance.models.Horse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Horse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_horse_request(template_url=self.get_horse.metadata["url"], **kwargs)._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Horse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_horse.metadata = {"url": "/multipleInheritance/horse"}  # type: ignore

    @distributed_trace_async
    async def put_horse(self, horse: "_models.Horse", **kwargs: Any) -> str:
        """Put a horse with name 'General' and isAShowHorse false.

        :param horse: Put a horse with name 'General' and isAShowHorse false.
        :type horse: ~multipleinheritance.models.Horse
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(horse, "Horse")

        request = _rest.build_put_horse_request(
            json=json, content_type=content_type, template_url=self.put_horse.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_horse.metadata = {"url": "/multipleInheritance/horse"}  # type: ignore

    @distributed_trace_async
    async def get_pet(self, **kwargs: Any) -> "_models.Pet":
        """Get a pet with name 'Peanut'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet, or the result of cls(response)
        :rtype: ~multipleinheritance.models.Pet
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Pet"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_pet_request(template_url=self.get_pet.metadata["url"], **kwargs)._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_pet.metadata = {"url": "/multipleInheritance/pet"}  # type: ignore

    @distributed_trace_async
    async def put_pet(self, name: str, **kwargs: Any) -> str:
        """Put a pet with name 'Butter'.

        :param name:
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        _pet = _models.Pet(name=name)
        json = None
        json = self._serialize.body(_pet, "Pet")

        request = _rest.build_put_pet_request(
            json=json, content_type=content_type, template_url=self.put_pet.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_pet.metadata = {"url": "/multipleInheritance/pet"}  # type: ignore

    @distributed_trace_async
    async def get_feline(self, **kwargs: Any) -> "_models.Feline":
        """Get a feline where meows and hisses are true.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Feline, or the result of cls(response)
        :rtype: ~multipleinheritance.models.Feline
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Feline"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_feline_request(
            template_url=self.get_feline.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Feline", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_feline.metadata = {"url": "/multipleInheritance/feline"}  # type: ignore

    @distributed_trace_async
    async def put_feline(self, feline: "_models.Feline", **kwargs: Any) -> str:
        """Put a feline who hisses and doesn't meow.

        :param feline: Put a feline who hisses and doesn't meow.
        :type feline: ~multipleinheritance.models.Feline
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(feline, "Feline")

        request = _rest.build_put_feline_request(
            json=json, content_type=content_type, template_url=self.put_feline.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_feline.metadata = {"url": "/multipleInheritance/feline"}  # type: ignore

    @distributed_trace_async
    async def get_cat(self, **kwargs: Any) -> "_models.Cat":
        """Get a cat with name 'Whiskers' where likesMilk, meows, and hisses is true.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Cat, or the result of cls(response)
        :rtype: ~multipleinheritance.models.Cat
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Cat"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_cat_request(template_url=self.get_cat.metadata["url"], **kwargs)._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Cat", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_cat.metadata = {"url": "/multipleInheritance/cat"}  # type: ignore

    @distributed_trace_async
    async def put_cat(self, cat: "_models.Cat", **kwargs: Any) -> str:
        """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

        :param cat: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.
        :type cat: ~multipleinheritance.models.Cat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(cat, "Cat")

        request = _rest.build_put_cat_request(
            json=json, content_type=content_type, template_url=self.put_cat.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_cat.metadata = {"url": "/multipleInheritance/cat"}  # type: ignore

    @distributed_trace_async
    async def get_kitten(self, **kwargs: Any) -> "_models.Kitten":
        """Get a kitten with name 'Gatito' where likesMilk and meows is true, and hisses and eatsMiceYet
        is false.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Kitten, or the result of cls(response)
        :rtype: ~multipleinheritance.models.Kitten
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Kitten"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = _rest.build_get_kitten_request(
            template_url=self.get_kitten.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Kitten", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_kitten.metadata = {"url": "/multipleInheritance/kitten"}  # type: ignore

    @distributed_trace_async
    async def put_kitten(self, kitten: "_models.Kitten", **kwargs: Any) -> str:
        """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
        true.

        :param kitten: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
         eatsMiceYet is true.
        :type kitten: ~multipleinheritance.models.Kitten
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")
        json = None
        json = self._serialize.body(kitten, "Kitten")

        request = _rest.build_put_kitten_request(
            json=json, content_type=content_type, template_url=self.put_kitten.metadata["url"], **kwargs
        )._internal_request
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_kitten.metadata = {"url": "/multipleInheritance/kitten"}  # type: ignore
