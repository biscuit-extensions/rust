from __future__ import annotations

import typing

from .rust import Rust

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: ExtensionsAPI) -> None:
    api.register("rust", Rust(api))
