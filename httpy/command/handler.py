import re
from enum import Enum
from typing import List, Union

from httpy.command.builder import RequestBuilder
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

        self.builder = RequestBuilder(self)

    def __find_operation(self, raw_cmd) -> Enum:
        ops = {
            CommandRegexs.INCREMENT: Operation.INCREMENT,
            CommandRegexs.DEINCREMENT: Operation.DEINCREMENT,
            CommandRegexs.RAND: Operation.RAND,
            CommandRegexs.READ: Operation.READ,
            CommandRegexs.LIST: Operation.LIST,
            CommandRegexs.TEXT: Operation.TEXT,
        }
        for op in ops:
            if re.search(op, raw_cmd):
                return ops[op]

    def __find_value(self, raw_cmd) -> Union[Union[str, List], None]:
        if self.operation == Operation.READ or self.operation == Operation.RAND:
            r = r"[(].*[)]"
            val = re.search(r, raw_cmd).group()[1:-1]
            return val
        elif self.operation == Operation.LIST:
            return raw_cmd.split(",")
        elif self.operation == Operation.TEXT:
            return raw_cmd
        return None
