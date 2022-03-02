import sys
from pathlib import Path
from typing import Any, Dict, List

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))


class Arguments:
    HEADER_MARK = ":"
    BODY_ARG_MARK = "="
    URL_ARG_MARK = "=="
    METHODS = {
        "GET": "GET",
        "POST": "POST",
        "PUT": "PUT",
        "PATCH": "PATCH",
    }

    def __init__(self, args: List[str]) -> None:
        self.args = args
        self._headers: Dict[str, Any] = dict()
        self._arguments: Dict[str, Any] = dict()
        self._body: Dict[str, Any] = dict()

    @property
    def headers(self) -> Dict[str, Any]:
        for arg in self.args:
            if Arguments.HEADER_MARK in arg:
                val = arg.split(Arguments.HEADER_MARK)
                self._headers[val[0]] = val[1]
        return self._headers

    @property
    def body(self) -> Dict[str, Any]:
        for arg in self.args:
            if Arguments.BODY_ARG_MARK in arg and Arguments.URL_ARG_MARK not in arg:
                val = arg.split(Arguments.BODY_ARG_MARK)
                self._body[val[0]] = val[1]
        return self._body

    @property
    def arguments(self) -> Dict[str, Any]:
        for arg in self.args:
            if Arguments.URL_ARG_MARK in arg:
                val = arg.split(Arguments.URL_ARG_MARK)
                self._arguments[val[0]] = val[1]
        return self._arguments

    @property
    def method(self) -> str:
        for arg in self.args:
            if arg.upper() in Arguments.METHODS:
                return arg.upper()
