from typing import Any

from django.utils.functional import LazyObject


# required for plugin to be able to distinguish this specific instance of LazySettings from others
class _DjangoConfLazyObject(LazyObject): ...


class LazySettings(_DjangoConfLazyObject):
    configured: bool
    def configure(self, default_settings: Any = ..., **options: Any) -> Any: ...

settings: LazySettings = ...