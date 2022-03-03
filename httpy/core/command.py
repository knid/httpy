import re
from enum import Enum

from .operation import Operation
from .regexs import CommandRegexs
from .request import Request


class CommandHandler:
    _SEPARATOR = ":"

    def __init__(self, request: Request, command: str) -> None:
        self.request = request
        self.raw_command = command
        self.command = command.split(CommandHandler._SEPARATOR)
        self.variable = self.command[0]
        self.operation = self.__find_operation(self.command[1])
        self.value = self.__find_value(self.command[1])
        self.max_run = self.command[2] if len(self.command) > 2 else 1

    def __find_operation(self, raw_cmd) -> Enum:
        ops = {
            CommandRegexs._INCREMENT: Operation.INCREMENT,
            CommandRegexs._DEINCREMENT: Operation.DEINCREMENT,
            CommandRegexs._RAND: Operation.RAND,
            CommandRegexs._READ: Operation.READ,
            CommandRegexs._LIST: Operation.LIST,
            CommandRegexs._TEXT: Operation.TEXT,
        }
        for op in ops.keys():
            if re.search(op, raw_cmd):
                return ops[op]

    def __find_value(self, raw_cmd):
        if self.operation == Operation.READ or self.operation == Operation.RAND:
            r = r"[(].*[)]"
            val = re.search(r, raw_cmd).group()[1:-1]
            return val
        elif self.operation == Operation.LIST:
            return raw_cmd.split(",")
        return None
