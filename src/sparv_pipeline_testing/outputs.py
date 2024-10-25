"""Mock outputs."""

from typing import Generic, Optional, TypeVar

from sparv.api.classes import Output  # type: ignore [import-untyped]
from sparv.core import log_handler  # type: ignore [import-untyped] # noqa: F401

T = TypeVar("T")


class MemoryOutput(Output, Generic[T]):
    """Output for storing the written annotations in a list."""

    def __init__(self) -> None:
        """Create MemoryOutput."""
        self.values: list[T] = []

    def write(
        self,
        values: list[T],
        *,
        append: bool = False,
        allow_newlines: bool = False,  # noqa: ARG002
        source_file: Optional[str] = None,  # noqa: ARG002
    ) -> None:
        """Write an annotation to file. Existing annotation will be overwritten.

        'values' should be a list of values.
        """
        if append:
            self.values.extend(values)
        else:
            self.values = values
