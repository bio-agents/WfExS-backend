from logging import Logger
from iteragents import *
from typing import (
    Any,
    Callable,
    Mapping,
    Optional,
    Sequence,
    Tuple,
)
from .exceptions import JSONPathError as JSONPathError

# Inspired by https://stackoverflow.com/a/53639221
JSONVal = (
    None | bool | str | float | int | Sequence["JSONVal"] | Mapping[str, "JSONVal"]
)

FilterFn = Callable[[JSONVal], bool]

logger: Logger
auto_id_field: Optional[str]
NOT_SET: object
LIST_KEY: object

class JSONPath:
    def find(self, data: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def find_or_create(
        self, data: DatumInContext | JSONVal
    ) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def update_or_create(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def child(self, child: This | Root | Child | Any) -> This | Root | Child: ...
    def make_datum(self, value: DatumInContext | JSONVal) -> DatumInContext: ...

class DatumInContext:
    @classmethod
    def wrap(cls, data: DatumInContext | Any) -> DatumInContext: ...
    value: JSONVal
    path: JSONPath
    context: Optional[DatumInContext]
    def __init__(
        self,
        value: JSONVal,
        path: Optional[JSONPath] = ...,
        context: Optional[JSONVal] = ...,
    ) -> None: ...
    def in_context(
        self, context: JSONVal, path: Optional[JSONPath]
    ) -> DatumInContext: ...
    @property
    def full_path(self) -> JSONPath: ...
    @property
    def id_pseudopath(self) -> JSONPath: ...
    def __eq__(self, other: Any) -> bool: ...

class AutoIdForDatum(DatumInContext):
    datum: DatumInContext
    id_field: Optional[str]
    def __init__(
        self, datum: DatumInContext, id_field: Optional[str] = ...
    ) -> None: ...
    @property
    def value(self) -> JSONVal: ...  # type: ignore[override]
    @property
    def path(self) -> JSONPath: ...  # type: ignore[override]
    @property
    def context(self) -> DatumInContext: ...  # type: ignore[override]
    def in_context(
        self, context: JSONVal, path: Optional[JSONPath]
    ) -> AutoIdForDatum: ...
    def __eq__(self, other: Any) -> bool: ...

class Root(JSONPath):
    def find(self, data: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class This(JSONPath):
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Child(JSONPath):
    left: JSONPath
    right: JSONPath
    def __init__(self, left: JSONPath, right: JSONPath) -> None: ...
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def find_or_create(
        self, datum: DatumInContext | JSONVal
    ) -> Sequence[DatumInContext]: ...
    def update_or_create(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Parent(JSONPath):
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def __eq__(self, other: Any) -> bool: ...

class Where(JSONPath):
    left: JSONPath
    right: JSONPath
    def __init__(self, left: JSONPath, right: JSONPath) -> None: ...
    def find(self, data: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Descendants(JSONPath):
    left: JSONPath
    right: JSONPath
    def __init__(self, left: JSONPath, right: JSONPath) -> None: ...
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def is_singular(self) -> bool: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Union(JSONPath):
    left: JSONPath
    right: JSONPath
    def __init__(self, left: JSONPath, right: JSONPath) -> None: ...
    def is_singular(self) -> bool: ...
    def find(self, data: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...

class Intersect(JSONPath):
    left: JSONPath
    right: JSONPath
    def __init__(self, left: JSONPath, right: JSONPath) -> None: ...
    def is_singular(self) -> bool: ...
    def find(self, data: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...

class Fields(JSONPath):
    fields: Tuple[str, ...]
    def __init__(self, *fields: str) -> None: ...
    @staticmethod
    def get_field_datum(
        datum: DatumInContext, field: str, create: bool
    ) -> Optional[DatumInContext]: ...
    def reified_fields(self, datum: DatumInContext) -> Tuple[str, ...]: ...
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def find_or_create(
        self, datum: DatumInContext | JSONVal
    ) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def update_or_create(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Index(JSONPath):
    index: int
    def __init__(self, index: int) -> None: ...
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def find_or_create(
        self, datum: DatumInContext | JSONVal
    ) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def update_or_create(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...

class Slice(JSONPath):
    start: Optional[int]
    end: Optional[int]
    step: Optional[int]
    def __init__(
        self,
        start: Optional[int] = ...,
        end: Optional[int] = ...,
        step: Optional[int] = ...,
    ) -> None: ...
    def find(self, datum: DatumInContext | JSONVal) -> Sequence[DatumInContext]: ...
    def update(self, data: JSONVal, val: JSONVal) -> JSONVal: ...
    def filter(self, fn: FilterFn, data: JSONVal) -> JSONVal: ...
    def __eq__(self, other: Any) -> bool: ...
