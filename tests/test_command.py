import sys
from pathlib import Path

import pytest

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))

from httpy.core.command import CommandHandler  # noqa: E402
from httpy.core.operation import Operation  # noqa: E402
from httpy.core.request import Request  # noqa: E402


@pytest.fixture
def req():
    r = Request("GET", "example.com")
    return r


def test_find_command_increment(req):

    cmd = CommandHandler(req, "i:++").operation
    assert cmd == Operation.INCREMENT


def test_find_command_deincrement(req):

    cmd = CommandHandler(req, "i:--:15").operation
    assert cmd == Operation.DEINCREMENT


def test_find_command_rand(req):

    cmd = CommandHandler(req, "i:rand(1,5):13").operation
    assert cmd == Operation.RAND


def test_find_command_read(req):

    cmd = CommandHandler(req, "i:read(paTh/tO/fiLe):15").operation
    assert cmd == Operation.READ


def test_find_command_list(req):

    cmd = CommandHandler(req, "i:john,13,mikey:12").operation
    assert cmd == Operation.LIST


def test_find_command_text(req):

    cmd = CommandHandler(req, "i:fas(/!'^)DfasdbkfjeA/(!'^:11").operation
    assert cmd == Operation.TEXT
