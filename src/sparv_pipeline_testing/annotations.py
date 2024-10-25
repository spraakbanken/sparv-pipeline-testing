"""Mock annotations."""

from collections.abc import Generator
from typing import Optional

from sparv.api.classes import Annotation, BaseAnnotation  # type: ignore [import-untyped]
from sparv.core import log_handler  # type: ignore [import-untyped] # noqa: F401


class MockAnnotation(Annotation):
    """Mock Annotation class for testing a 'sparv.annotator'."""

    def __init__(  # noqa: D107
        self,
        name: str = "",
        source_file: Optional[str] = None,  # noqa: ARG002
        values: Optional[list[str]] = None,
        children: Optional[dict[str, list[list[int]]]] = None,
        spans: Optional[list[tuple[int, int]]] = None,
    ) -> None:
        super().__init__(name)
        self._values = values or []
        self._children = children or {}
        self._spans = spans or []

    def read(self, allow_newlines: bool = False) -> Generator[str, None, None]:  # noqa: ARG002
        """Yield each line from the annotation."""
        if not self._values:
            return
        yield from self._values

    def read_spans(
        self,
        decimals=False,  # noqa: ARG002
        with_annotation_name=False,  # noqa: ARG002
    ) -> Generator[tuple[int, int], None, None]:
        """Yield the spans of the annotation."""
        if not self._spans:
            return
        yield from self._spans

    def get_children(
        self,
        child: BaseAnnotation,
        *,
        orphan_alert: bool = False,  # noqa: ARG002
        preserve_parent_annotation_order: bool = False,  # noqa: ARG002
    ) -> tuple[list, list]:
        """Return two lists.

        The first one is a list with n (= total number of parents) elements where
        every element is a list of indices in the child annotation.
        The second one is a list of orphans, i.e. containing indices in the child annotation
        that have no parent.
        Both parents and children are sorted according to their position in the source file,
        unless 'preserve_parent_annotation_order' is set to True, in which case the parents keep
        the order from the parent annotation.
        """
        return self._children[child.name], []

    def create_empty_attribute(self) -> list:
        """Create an empty attribute with the size of this annotation."""
        if self._values:
            return [None] * len(self._values)
        return [None] * max(len(val) for val in self._children.values())
