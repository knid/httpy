import re
from enum import Enum

from httpcli.core.request import Request


class Commands(Enum):
    INCREMENT = 1
    DEINCREMENT = 2
    LIST = 3
    RAND = 4
    READ = 5
    TEXT = 6


class CommandHandler:
    _SEPARATOR = r":"
    _LIST = r".*[,].*"
    _INCREMENT = r"\+{2}"
    _DEINCREMENT = r"-{2}"
    _RAND = r"rand[(][0-9]*[,][0-9]*[)]"
    _READ = r"read[(][a-zA-Z0-9/\\\.]*[)]"
    _TEXT = r".*"

    def __init__(self, request: Request, command: str) -> None:
        self.request = request
        self.raw_command = command
        self.command = command.split(CommandHandler._SEPARATOR)
        self.variable = self.command[0]
        self.operation = self.command[1]
        self.max_run = self.command[2] if len(self.command) > 2 else 1

    def __find_operation(self) -> Enum:
        ops = {
            CommandHandler._INCREMENT: Commands.INCREMENT,
            CommandHandler._DEINCREMENT: Commands.DEINCREMENT,
            CommandHandler._RAND: Commands.RAND,
            CommandHandler._READ: Commands.READ,
            CommandHandler._LIST: Commands.LIST,
            CommandHandler._TEXT: Commands.TEXT,
        }
        for op in ops.keys():
            if re.search(op, self.operation):
                return ops[op]
