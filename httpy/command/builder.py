import re
from random import randint
from typing import List

from httpy.command.operation import Operation
from httpy.output.error import write_error
from httpy.request import Request


class RequestBuilder:
    def __init__(self, handler) -> None:
        self.handler = handler

    def build_requests(self) -> List[Request]:
        if self.handler.operation is Operation.INCREMENT:
            for run in range(self.handler.max_run):
                yield self._build_request(run)
        elif self.handler.operation is Operation.DEINCREMENT:
            value = 0
            for run in range(self.handler.max_run):
                yield self._build_request(value)
                value -= 1
        elif self.handler.operation is Operation.LIST:
            if self.handler.max_run == 1:
                for item in self.handler.value:
                    yield self._build_request(item)
            else:
                run = 0
                for _ in range(self.handler.max_run):
                    try:
                        yield self._build_request(self.handler.value[run])
                        run += 1
                    except IndexError:
                        run = 0
                        yield self._build_request(self.handler.value[run])
        elif self.handler.operation is Operation.TEXT:
            for run in range(self.handler.max_run):
                yield self._build_request(self.handler.value)
        elif self.handler.operation is Operation.RAND:
            value = self.handler.value.split(",")
            for run in range(self.handler.max_run):
                random = randint(int(value[0]), int(value[1]))
                yield self._build_request(random)
        elif self.handler.operation is Operation.READ:
            try:
                with open(self.handler.value, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        yield self._build_request(line.strip())
            except FileNotFoundError as e:
                write_error("File Not Found: ", f"'{e.filename}'")

    def _build_item(self, item: str, value: str) -> str:
        variable = "{" + self.handler.variable + "}"
        r = r"[{]" + self.handler.variable + r"[}]"

        list_item = list(item)
        counter = 0
        for match in re.finditer(r, item):
            diff = (len(variable) - len(str(value))) * counter
            span = match.span()
            list_item[span[0] - diff : span[1] - diff] = str(value)  # noqa: E203
            counter += 1

        return "".join(list_item)

    def _build_iterable_item(self, item: dict, value: str) -> dict:
        val = dict()
        if item is not None:
            for k, v in item.items():
                val[k] = self._build_item(v, value)
        return val

    def _build_request(self, value: str) -> Request:
        return Request(
            self.handler.request.method,
            self._build_item(self.handler.request.url, value),
            self._build_iterable_item(self.handler.request.header, value),
            self._build_iterable_item(self.handler.request.body, value),
            self._build_iterable_item(self.handler.request.queries, value),
            self.handler.request.redirect,
        )
