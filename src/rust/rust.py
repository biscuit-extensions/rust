from __future__ import annotations

import subprocess as sp
import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class Rust(Extension):
    def __init__(self, api: ExtensionsAPI):
        self.api = api

    def install(self):
        # assumes rustup & rust is installed
        try:
            sp.check_call(["rustup", "component", "add", "rust-analyzer"])
        except sp.CalledProcessError:
            self.api.notifications.warning(
                "Rust extension requires rust-analyzer to be installed & in your PATH."
            )

        self.api.register_langserver("Rust", "rust-analyzer")
