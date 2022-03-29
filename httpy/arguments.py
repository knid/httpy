import argparse
from typing import Any, Dict, Union

import httpy


class ArgumentParser(argparse.ArgumentParser):
    HEADER_MARK = ":"
    BODY_ARG_MARK = "="
    QUERY_MARK = "=="

    def __init__(self) -> None:
        super().__init__()
        self._headers: Dict[str, Any] = dict()
        self._query_arguments: Dict[str, Any] = dict()
        self._body: Dict[str, Any] = dict()

        self.description = """Simple HTTP Cli tool for API. JSON requests,
        downloads, functionality, variables and colorized responses"""
        self.prog = "httpy"

        self.add_argument("URL")
        self.add_argument(
            "-v", "--version", action="version", version="%(prog)s " + httpy.__version__
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
        self.add_argument("-x", "--exec", metavar="CMD", help="execute httpcli command")
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

        self.args, self.extra_args = self.parse_known_intermixed_args()

    @property
    def url(self):
        return self.args.URL

    @property
    def headers(self) -> Union[Dict[str, Any], None]:
        for arg in self.extra_args:
            if ArgumentParser.HEADER_MARK in arg:
                val = arg.split(ArgumentParser.HEADER_MARK)
                self._headers[val[0]] = val[1]
        if self._headers:
            return self._headers
        return None

    @property
    def body(self) -> Union[Dict[str, Any], None]:
        for arg in self.extra_args:
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
    def query_arguments(self) -> Union[Dict[str, Any], None]:
        for arg in self.extra_args:
            if ArgumentParser.QUERY_MARK in arg:
                val = arg.split(ArgumentParser.QUERY_MARK)
                self._query_arguments[val[0]] = val[1]
        if self._query_arguments:
            return self._query_arguments
        return None

    @property
    def method(self) -> Dict[str, Any]:
        methods = ["get", "post", "put", "delete"]
        for arg in self.extra_args:
            for method in methods:
                if arg.lower() == method:
                    return method.upper()
        return methods[0]

    @property
    def command(self) -> Union[str, None]:
        if self.args.exec:
            return self.args.exec
        return None

    @property
    def redirect(self) -> bool:
        return self.args.allow_redirect

    @property
    def show_status(self) -> bool:
        return self.args.status

    @property
    def show_header(self) -> bool:
        return bool(self.args.header)

    @property
    def show_body(self) -> bool:
        return bool(self.args.body)

    @property
    def verbose(self) -> bool:
        return bool(self.args.verbose)

    @property
    def filter(self) -> bool:
        return self.show_status or self.show_header or self.show_body
