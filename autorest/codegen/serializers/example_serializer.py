# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Tuple
from jinja2 import Environment

from ..models import CodeModel


class ExampleSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group_name: str,
        operation_name: str,
        parameters: List[Tuple]
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group_name = operation_group_name
        self.operation_name = operation_name
        self.parameters = parameters

    def serialize(self) -> str:

        template = self.env.get_template("example.py.jinja2")
        return template.render(
            code_model=self.code_model,
            operation_group_name=self.operation_group_name,
            operation_name=self.operation_name,
            parameters=self.parameters,
        )
