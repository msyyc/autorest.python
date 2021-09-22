# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class FirstParameterGroup(msrest.serialization.Model):
    """Parameter group.

    :ivar header_one:
    :vartype header_one: str
    :ivar query_one: Query parameter with default.
    :vartype query_one: int
    """

    _attribute_map = {
        "header_one": {"key": "header-one", "type": "str"},
        "query_one": {"key": "query-one", "type": "int"},
    }

    def __init__(self, *, header_one: Optional[str] = None, query_one: Optional[int] = 30, **kwargs):
        """
        :keyword header_one:
        :paramtype header_one: str
        :keyword query_one: Query parameter with default.
        :paramtype query_one: int
        """
        super(FirstParameterGroup, self).__init__(**kwargs)
        self.header_one = header_one
        self.query_one = query_one


class ParameterGroupingPostMultiParamGroupsSecondParamGroup(msrest.serialization.Model):
    """Parameter group.

    :ivar header_two:
    :vartype header_two: str
    :ivar query_two: Query parameter with default.
    :vartype query_two: int
    """

    _attribute_map = {
        "header_two": {"key": "header-two", "type": "str"},
        "query_two": {"key": "query-two", "type": "int"},
    }

    def __init__(self, *, header_two: Optional[str] = None, query_two: Optional[int] = 30, **kwargs):
        """
        :keyword header_two:
        :paramtype header_two: str
        :keyword query_two: Query parameter with default.
        :paramtype query_two: int
        """
        super(ParameterGroupingPostMultiParamGroupsSecondParamGroup, self).__init__(**kwargs)
        self.header_two = header_two
        self.query_two = query_two


class ParameterGroupingPostOptionalParameters(msrest.serialization.Model):
    """Parameter group.

    :ivar custom_header:
    :vartype custom_header: str
    :ivar query: Query parameter with default.
    :vartype query: int
    """

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
    }

    def __init__(self, *, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs):
        """
        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        """
        super(ParameterGroupingPostOptionalParameters, self).__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query


class ParameterGroupingPostRequiredParameters(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar custom_header:
    :vartype custom_header: str
    :ivar query: Query parameter with default.
    :vartype query: int
    :ivar path: Required. Path parameter.
    :vartype path: str
    :ivar body: Required.
    :vartype body: int
    """

    _validation = {
        "path": {"required": True},
        "body": {"required": True},
    }

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
        "path": {"key": "path", "type": "str"},
        "body": {"key": "body", "type": "int"},
    }

    def __init__(
        self, *, path: str, body: int, custom_header: Optional[str] = None, query: Optional[int] = 30, **kwargs
    ):
        """
        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        :keyword path: Required. Path parameter.
        :paramtype path: str
        :keyword body: Required.
        :paramtype body: int
        """
        super(ParameterGroupingPostRequiredParameters, self).__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query
        self.path = path
        self.body = body


class ParameterGroupingPostReservedWordsParameters(msrest.serialization.Model):
    """Parameter group.

    :ivar from_property: 'from' is a reserved word. Pass in 'bob' to pass.
    :vartype from_property: str
    :ivar accept: 'accept' is a reserved word. Pass in 'yes' to pass.
    :vartype accept: str
    """

    _attribute_map = {
        "from_property": {"key": "from", "type": "str"},
        "accept": {"key": "accept", "type": "str"},
    }

    def __init__(self, *, from_property: Optional[str] = None, accept: Optional[str] = None, **kwargs):
        """
        :keyword from_property: 'from' is a reserved word. Pass in 'bob' to pass.
        :paramtype from_property: str
        :keyword accept: 'accept' is a reserved word. Pass in 'yes' to pass.
        :paramtype accept: str
        """
        super(ParameterGroupingPostReservedWordsParameters, self).__init__(**kwargs)
        self.from_property = from_property
        self.accept = accept
