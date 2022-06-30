# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Any, Dict
import black

from .. import Plugin, PluginAutorest
from .._utils import filter_output_uri

_LOGGER = logging.getLogger(__name__)

_BLACK_MODE = black.Mode()
_BLACK_MODE.line_length = 120


class BlackScriptPlugin(Plugin):  # pylint: disable=abstract-method
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        output_folder_uri = self.options["outputFolderUri"]
        self.output_folder = filter_output_uri(output_folder_uri)

    def process(self) -> bool:
        # apply format_file on every file in the output folder
        list(
            map(
                self.format_file,
                [f for f in self.output_folder.glob("**/*") if f.is_file()],
            )
        )
        return True

    def format_file(self, full_path) -> None:
        file = full_path.relative_to(self.output_folder)
        file_content = self.read_file(file)
        if not file.suffix == ".py":
            self.write_file(file, file_content)
            return
        try:
            file_content = black.format_file_contents(
                file_content, fast=True, mode=_BLACK_MODE
            )
        except black.NothingChanged:
            pass
        self.write_file(file, file_content)


class BlackScriptPluginAutorest(BlackScriptPlugin, PluginAutorest):
    def get_options(self) -> Dict[str, Any]:
        return {"outputFolderUri": self._autorestapi.get_value("outputFolderUri")}
