# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._request_builders_py3 import build_get_model_request
    from ._request_builders_py3 import build_post_model_request
    from ._request_builders_py3 import build_get_pages_request
    from ._request_builders_py3 import build_lro_request
except (SyntaxError, ImportError):
    from ._request_builders import build_get_model_request  # type: ignore
    from ._request_builders import build_post_model_request  # type: ignore
    from ._request_builders import build_get_pages_request  # type: ignore
    from ._request_builders import build_lro_request  # type: ignore

__all__ = [
    "build_get_model_request",
    "build_post_model_request",
    "build_get_pages_request",
    "build_lro_request",
]
