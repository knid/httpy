from typing import Any, Dict, Union
from urllib.parse import urlencode

from urllib3 import PoolManager
from urllib3.response import HTTPResponse


class Request(PoolManager):
    def __init__(
        self,
        method: str,
        url: str,
        header: Union[Dict[str, Any], None] = None,
        body: Union[Dict[str, Any], None] = None,
        queris: Union[Dict[str, Any], None] = None,
    ) -> None:
        self.method = method
        self.url = url
        self.header = header
        self.body = body
        self.queries = queris

    def make_request(self) -> HTTPResponse:
        if self.method == "GET" or self.method == "DELETE":
            return self.__get_delete_requests()
        return self.__post_put_requests()

    def __get_delete_requests(self) -> HTTPResponse:
        return self.request(self.method, self.url, self.queries, self.header)

    def __post_put_requests(self) -> HTTPResponse:
        if self.queries:
            return self.request(
                self.method,
                f"{self.url}?{urlencode(self.queries)}",
                self.body,
                self.header,
            )
        return self.request(self.method, self.url, self.body, self.header)
