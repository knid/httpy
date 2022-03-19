import re
from enum import Enum
from typing import List, Union

from httpy.command.operation import Operation
from httpy.command.regexs import CommandRegexs
from httpy.request import Request


class CommandHandler:
    _SEPARATOR = ":"

    def __init__(self, request: Request, command: str) -> None:
        self.request = request
        self.raw_command = command
        self.command = command.split(CommandHandler._SEPARATOR)
        self.variable = self.command[0]
        self.operation = self.__find_operation(self.command[1])
        self.value = self.__find_value(self.command[1])
        self.max_run = int(self.command[2]) if len(self.command) > 2 else 1

    def build_requests(self) -> List[Request]:
        if self.operation is Operation.INCREMENT:
            for run in range(self.max_run):
                yield self._build_request(run)
        elif self.operation is Operation.DEINCREMENT:
            value = 0
            for run in range(self.max_run):
                yield self._build_request(value)
                value -= 1
        elif self.operation is Operation.LIST:
            pass

        elif self.operation is Operation.TEXT:
            pass

        elif self.operation is Operation.RAND:
            pass

        elif self.operation is Operation.READ:
            pass

    def _build_item(self, item: str, value: str) -> str:
        variable = "{" + self.variable + "}"
        r = r"[{]" + self.variable + r"[}]"

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
                item[k] = self._build_item(v, value)
        return val

    def _build_request(self, value: str) -> Request:
        return Request(
            self.request.method,
            self._build_item(self.request.url, value),
            self._build_iterable_item(self.request.header, value),
            self._build_iterable_item(self.request.body, value),
            self._build_iterable_item(self.request.queries, value),
            self.request.redirect,
        )

    def __find_operation(self, raw_cmd) -> Enum:
        ops = {
            CommandRegexs.INCREMENT: Operation.INCREMENT,
            CommandRegexs.DEINCREMENT: Operation.DEINCREMENT,
            CommandRegexs.RAND: Operation.RAND,
            CommandRegexs.READ: Operation.READ,
            CommandRegexs.LIST: Operation.LIST,
            CommandRegexs.TEXT: Operation.TEXT,
        }
        for op in ops.keys():
            if re.search(op, raw_cmd):
                return ops[op]

    def __find_value(self, raw_cmd) -> Union[Union[str, List], None]:
        if self.operation == Operation.READ or self.operation == Operation.RAND:
            r = r"[(].*[)]"
            val = re.search(r, raw_cmd).group()[1:-1]
            return val
        elif self.operation == Operation.LIST:
            return raw_cmd.split(",")
        return None
