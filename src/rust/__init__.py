from __future__ import annotations

import typing

from .rust import Rust

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: ExtensionsAPI) -> None:
    """Defines the entrypoint to the extension.

    Normally, `api.register(id, instance)` is called within `setup`
    if you are expecting it to communicate with other loaded extensions."""

    api.register("rust", Rust(api))
