# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
from typing import List, Optional, Tuple, Dict, Any
from autorest.codegen.models.credential_types import TokenCredentialType
from autorest.codegen.models.imports import FileImport, ImportType
from autorest.codegen.serializers.import_serializer import FileImportSerializer
from jinja2 import Environment
from ..models import CodeModel


class SampleSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group_name: str,
        operation_name: str,
        client_params: Dict[Any, Any],
        operation_params: Dict[Any, Any],
        imports: FileImport,
        annotation: str,
        origin_file: Optional[str],
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group_name = operation_group_name
        self.operation_name = operation_name
        self.client_params = client_params
        self.operation_params = operation_params
        self.imports = imports
        self.annotation = annotation
        self.origin_file = origin_file

    def serialize(self) -> str:
        template = self.env.get_template("sample.py.jinja2")
        return template.render(
            code_model=self.code_model,
            operation_group_name=self.operation_group_name,
            operation_name=self.operation_name,
            client_params=self.client_params,
            operation_params=self.operation_params,
            origin_file=self.origin_file,
            imports=FileImportSerializer(self.imports, True),
            annotation=self.annotation,
        )
