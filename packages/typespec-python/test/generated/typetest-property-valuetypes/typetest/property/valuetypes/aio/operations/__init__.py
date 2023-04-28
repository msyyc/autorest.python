# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import BooleanOperations
from ._operations import StringOperations
from ._operations import BytesOperations
from ._operations import IntOperations
from ._operations import FloatOperations
from ._operations import DatetimeOperations
from ._operations import DurationOperations
from ._operations import EnumOperations
from ._operations import ExtensibleEnumOperations
from ._operations import ModelOperations
from ._operations import CollectionsStringOperations
from ._operations import CollectionsIntOperations
from ._operations import CollectionsModelOperations
from ._operations import DictionaryStringOperations
from ._operations import NeverOperations
from ._operations import UnknownStringOperations
from ._operations import UnknownIntOperations
from ._operations import UnknownDictOperations
from ._operations import UnknownArrayOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BooleanOperations",
    "StringOperations",
    "BytesOperations",
    "IntOperations",
    "FloatOperations",
    "DatetimeOperations",
    "DurationOperations",
    "EnumOperations",
    "ExtensibleEnumOperations",
    "ModelOperations",
    "CollectionsStringOperations",
    "CollectionsIntOperations",
    "CollectionsModelOperations",
    "DictionaryStringOperations",
    "NeverOperations",
    "UnknownStringOperations",
    "UnknownIntOperations",
    "UnknownDictOperations",
    "UnknownArrayOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
