import re
from enum import Enum
from typing import Dict, Iterator, List, Union

from httpy.request import Request

from .operation import Operation
from .regexs import CommandRegexs


class CommandHandler:
    _SEPARATOR = ":"

    def __init__(self, request: Request, command: str) -> None:
        self.request = request
        self.raw_command = command
        self.command = command.split(CommandHandler._SEPARATOR)
        self.variable = self.command[0]
        self.operation = self.__find_operation(self.command[1])
        self.value = self.__find_value(self.command[1])
        self.positions = self.__find_variable_positions()
        self.max_run = int(self.command[2]) if len(self.command) > 2 else 1

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

    def __find_variable_positions(self) -> Dict[str, Iterator]:
        t = "{" + self.variable + "}"
        r = r"[{]" + self.variable + r"[}]"

        pos = dict()
        pos["url"] = list()
        pos["headers"] = list()
        pos["body"] = list()
        pos["queries"] = list()

        get_span = lambda g: [i.span() for i in re.finditer(r, g)]  # noqa: E731
        add_position = (
            lambda k, v: [
                pos[k].append({i: get_span(v[i])}) for i in v if t in v.values()
            ]
            if v
            else 0
        )

        pos["url"].append(get_span(self.request.url))
        add_position("headers", self.request.header)
        add_position("body", self.request.body)
        add_position("queries", self.request.queries)
        return pos
