from logging import Logger
from typing import (
    Any,
    Iterable,
    Optional,
    Sequence,
    Tuple,
)
from jsonpath_ng.jsonpath import (
    JSONPath,
    DatumInContext,
    AutoIdForDatum,
    Root,
    This,
    Child,
    Parent,
    Where,
    Descendants,
    Union,
    Intersect,
    Fields,
    Index,
    Slice,
)
from jsonpath_ng.exceptions import JsonPathParserError as JsonPathParserError
from jsonpath_ng.jsonpath import (
    JSONPath,
)
from jsonpath_ng.lexer import (
    JsonPathLexer as JsonPathLexer,
)
from ply.lex import LexToken  # type: ignore[import]

logger: Logger

def parse(string: str) -> JSONPath: ...

class JsonPathParser:
    tokens: Sequence[str]
    debug: bool
    lexer_class: type[JsonPathLexer]
    def __init__(
        self, debug: bool = ..., lexer_class: Optional[type[JsonPathLexer]] = ...
    ) -> None: ...
    def parse(self, string: str, lexer: Optional[JsonPathLexer] = ...) -> Any: ...
    def parse_token_stream(
        self, token_iterator: Iterable[LexToken], start_symbol: str = ...
    ) -> Any: ...
    precedence: Sequence[Tuple[str, str] | Tuple[str, str, str]]
    def p_error(self, t: LexToken) -> None: ...
    def p_jsonpath_binop(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_fields(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_named_operator(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_root(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_idx(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_slice(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_fieldbrackets(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_child_fieldbrackets(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_child_idxbrackets(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_child_slicebrackets(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_jsonpath_parens(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_fields_or_any(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_fields_id(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_fields_comma(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_idx(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_slice_any(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_slice(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_maybe_int(self, p: Sequence[JSONPath | str]) -> None: ...
    def p_empty(self, p: Sequence[JSONPath | str]) -> None: ...

class IteratorToTokenStream:
    iterator: Iterable[LexToken]
    def __init__(self, iterator: Iterable[LexToken]) -> None: ...
    def token(self) -> Optional[LexToken]: ...
