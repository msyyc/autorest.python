# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Any, Dict
from pathlib import Path
from jinja2 import Environment, PackageLoader
from .. import Plugin, PluginAutorest
from .._utils import filter_output_uri

_LOGGER = logging.getLogger(__name__)


class MultiClientPlugin(Plugin):  # pylint: disable=abstract-method
    def process(self) -> bool:
        _LOGGER.info("Generating files for multi client")

        env = Environment(
            loader=PackageLoader("autorest.multiclient", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # __init__.py
        template = env.get_template("init.py.jinja2")
        self.write_file(Path("__init__.py"), template.render())

        # _version.py
        template = env.get_template("version.py.jinja2")
        self.write_file(
            Path("_version.py"),
            template.render(module_version=self.find_version_path()),
        )

        # py.typed
        self.write_file(Path("py.typed"), "# Marker file for PEP 561.")

        _LOGGER.info("Generating Done for multi client!")
        return True

    def find_version_path(self) -> str:
        output_folder = filter_output_uri(str(self.options["outputFolderUri"]))
        version_folder = next(output_folder.glob("*/_version.py"))
        module_version = "." + ".".join(version_folder.relative_to(output_folder).parts)
        return module_version.replace(".py", "")


class MultiClientPluginAutorest(MultiClientPlugin, PluginAutorest):
    def get_options(self) -> Dict[str, Any]:
        return {"outputFolderUri": self._autorestapi.get_value("outputFolderUri")}
