"""Mock outputs."""
from typing import Dict, Generator, Generic, List, Optional, Tuple, TypeVar

from sparv.api.classes import Annotation, BaseAnnotation, Output  # type: ignore [import-untyped]
from sparv.core import log_handler  # type: ignore [import-untyped] # noqa: F401


T = TypeVar("T")


class MemoryOutput(Output, Generic[T]):
    def __init__(self) -> None:
        self.values: List[T] = []

    def write(
        self,
        values: List[T],
        *,
        append: bool = False,
        allow_newlines: bool = False,
        source_file: Optional[str] = None,
    ) -> None:
        """Write an annotation to file. Existing annotation will be overwritten.

        'values' should be a list of values.
        """
        if append:
            self.values.extend(values)
        else:
            self.values = values