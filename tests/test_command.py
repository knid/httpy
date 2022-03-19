import sys
from pathlib import Path

import pytest

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))

from httpy.command.handler import CommandHandler  # noqa: E402
from httpy.command.operation import Operation  # noqa: E402
from httpy.request import Request  # noqa: E402


@pytest.fixture
def req():
    r = Request("GET", "example.com")
    return r


def test_find_command_increment(req):

    cmd = CommandHandler(req, "i:++")
    assert cmd.operation == Operation.INCREMENT


def test_find_command_deincrement(req):

    cmd = CommandHandler(req, "i:--:15")
    assert cmd.operation == Operation.DEINCREMENT


def test_find_command_rand(req):

    cmd = CommandHandler(req, "i:rand(1,5):13")
    assert cmd.operation == Operation.RAND


def test_find_command_read(req):

    cmd = CommandHandler(req, "i:read(paTh/tO/fiLe):15")
    assert cmd.operation == Operation.READ


def test_find_command_list(req):

    cmd = CommandHandler(req, "i:john,13,mikey:12")
    assert cmd.operation == Operation.LIST


def test_find_command_text(req):

    cmd = CommandHandler(req, "i:fas(/!'^)DfasdbkfjeA/(!'^:11")
    assert cmd.operation == Operation.TEXT
