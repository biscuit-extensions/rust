from __future__ import annotations

import typing

import subprocess as sp
import typing

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class Rust:
    def __init__(self, api):
        self.api = api

    def install(self):
        try:
            sp.check_call(["rustup", "component", "add", "rust-analyzer"])
        except sp.CalledProcessError:
            self.api.notifications.warning(
                "Rust extension requires rust-analyzer to be installed & in your PATH."
            )
        self.api.register_langserver("Rust", "rust-analyzer")
