import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Union

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))


class ArgumentParser(argparse.ArgumentParser):
    HEADER_MARK = ":"
    BODY_ARG_MARK = "="
    QUERY_MARK = "=="

    def __init__(self, args: List[str]) -> None:
        super().__init__()
        self._headers: Dict[str, Any] = dict()
        self._query_arguments: Dict[str, Any] = dict()
        self._body: Dict[str, Any] = dict()

        self.description = """Simple HTTP Cli tool for API. JSON requests,
        downloads, functionality,variables and colorized responses"""
        self.prog = "httpcli"

        self.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.1")
        self.add_argument(
            "method", default="GET", nargs="?", choices=["GET", "POST", "PUT", "DELETE"]
        )
        self.add_argument(
            "-H", "--header", action="store_true", help="show response header only"
        )
        self.add_argument(
            "-B", "--body", action="store_true", help="show response body only"
        )
        self.add_argument(
            "-S", "--status", action="store_true", help="show response status only"
        )
        self.add_argument(
            "-V",
            "--verbose",
            action="store_true",
            help="show request and response in verbose",
        )
        self.add_argument(
            "-r",
            "--allow-redirect",
            action="store_true",
            help="allow requests to be redirected",
        )

        self.args = self.parse_args()

    @property
    def headers(self) -> Union[Dict[str, Any], None]:
        for arg in self.args:
            if ArgumentParser.HEADER_MARK in arg:
                val = arg.split(ArgumentParser.HEADER_MARK)
                self._headers[val[0]] = val[1]
        if self._headers:
            return self._headers
        return None

    @property
    def body(self) -> Dict[str, Any]:
        for arg in self.args:
            if (
                ArgumentParser.BODY_ARG_MARK in arg
                and ArgumentParser.QUERY_MARK not in arg
            ):
                val = arg.split(ArgumentParser.BODY_ARG_MARK)
                self._body[val[0]] = val[1]
        if self._body:
            return self._body
        return None

    @property
    def query_arguments(self) -> Dict[str, Any]:
        for arg in self.args:
            if ArgumentParser.QUERY_MARK in arg:
                val = arg.split(ArgumentParser.QUERY_MARK)
                self._query_arguments[val[0]] = val[1]
        if self._query_arguments:
            return self._query_arguments
        return None


print(ArgumentParser(sys.argv[1:]).args)
