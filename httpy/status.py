from enum import Enum, unique


@unique
class ExitStatus(Enum):
    SUCCESS = 0
    ERROR = 1
    KEYBOARD_INTERRUPT = 130
