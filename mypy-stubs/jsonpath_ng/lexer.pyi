from logging import Logger
from typing import (
    Mapping,
    Sequence,
    Tuple,
)
from ply.lex import LexToken  # type: ignore[import]
from collections.abc import Generator
from jsonpath_ng.exceptions import JsonPathLexerError as JsonPathLexerError

logger: Logger

class JsonPathLexer:
    debug: bool
    def __init__(self, debug: bool = ...) -> None: ...
    def tokenize(self, string: str) -> Generator[LexToken, None, None]: ...
    literals: Sequence[str]
    reserved_words: Mapping[str, str]
    tokens: Sequence[str]
    states: Sequence[Tuple[str, str]]
    t_DOUBLEDOT: str
    t_ignore: str
    def t_ID(self, t: LexToken) -> LexToken: ...
    def t_NUMBER(self, t: LexToken) -> LexToken: ...
    t_singlequote_ignore: str
    def t_singlequote(self, t: LexToken) -> None: ...
    def t_singlequote_content(self, t: LexToken) -> None: ...
    def t_singlequote_escape(self, t: LexToken) -> None: ...
    def t_singlequote_end(self, t: LexToken) -> LexToken: ...
    def t_singlequote_error(self, t: LexToken) -> None: ...
    t_doublequote_ignore: str
    def t_doublequote(self, t: LexToken) -> None: ...
    def t_doublequote_content(self, t: LexToken) -> None: ...
    def t_doublequote_escape(self, t: LexToken) -> None: ...
    def t_doublequote_end(self, t: LexToken) -> LexToken: ...
    def t_doublequote_error(self, t: LexToken) -> None: ...
    t_backquote_ignore: str
    def t_backquote(self, t: LexToken) -> None: ...
    def t_backquote_escape(self, t: LexToken) -> None: ...
    def t_backquote_content(self, t: LexToken) -> None: ...
    def t_backquote_end(self, t: LexToken) -> LexToken: ...
    def t_backquote_error(self, t: LexToken) -> None: ...
    def t_newline(self, t: LexToken) -> None: ...
    def t_error(self, t: LexToken) -> None: ...
