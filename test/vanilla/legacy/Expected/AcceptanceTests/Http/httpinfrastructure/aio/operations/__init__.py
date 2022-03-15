# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._http_failure_operations import HttpFailureOperations
from ._http_success_operations import HttpSuccessOperations
from ._http_redirects_operations import HttpRedirectsOperations
from ._http_client_failure_operations import HttpClientFailureOperations
from ._http_server_failure_operations import HttpServerFailureOperations
from ._http_retry_operations import HttpRetryOperations
from ._multiple_responses_operations import MultipleResponsesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "HttpFailureOperations",
    "HttpSuccessOperations",
    "HttpRedirectsOperations",
    "HttpClientFailureOperations",
    "HttpServerFailureOperations",
    "HttpRetryOperations",
    "MultipleResponsesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
