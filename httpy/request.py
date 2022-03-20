from typing import Any, Dict, Union

import requests

from .arguments import ArgumentParser


class Request:
    def __init__(
        self,
        method: str,
        url: str,
        header: Union[Dict[str, Any], None] = None,
        body: Union[Dict[str, Any], None] = None,
        queries: Union[Dict[str, Any], None] = None,
        redirect: bool = False,
    ) -> None:

        self.method = method
        self.url = self.__fix_url(url)
        self.header = header
        self.body = body
        self.queries = queries
        self.redirect = redirect

    @classmethod
    def from_args(cls, args: ArgumentParser):
        req = cls(
            args.method,
            args.url,
            args.headers,
            args.body,
            args.query_arguments,
            args.redirect,
        )
        return req

    def make_request(self) -> requests.Response:
        session = requests.Session()
        req = requests.Request(
            self.method, self.url, self.header, json=self.body, params=self.queries
        )
        prepped = req.prepare()
        response = session.send(prepped, allow_redirects=self.redirect)
        return response

    def __fix_url(self, url: str) -> str:
        if not url.startswith("http://") and not url.startswith("https://"):
            return "http://" + url
        return url
