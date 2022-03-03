import pytest

from httpcli.core.command import CommandHandler, Commands
from httpcli.core.request import Request


@pytest.fixture
def req():
    r = Request("GET", "example.com")
    return r


def test_find_command_increment(req):

    cmd = CommandHandler(req, "i:++")._CommandHandler__find_operation()
    assert cmd == Commands.INCREMENT


def test_find_command_deincrement(req):

    cmd = CommandHandler(req, "i:--:15")._CommandHandler__find_operation()
    assert cmd == Commands.DEINCREMENT


def test_find_command_rand(req):

    cmd = CommandHandler(req, "i:rand(1,5):13")._CommandHandler__find_operation()
    assert cmd == Commands.RAND


def test_find_command_read(req):

    cmd = CommandHandler(
        req, "i:read(paTh/tO/fiLe):15"
    )._CommandHandler__find_operation()
    assert cmd == Commands.READ


def test_find_command_list(req):

    cmd = CommandHandler(req, "i:john,13,mikey:12")._CommandHandler__find_operation()
    assert cmd == Commands.LIST


def test_find_command_text(req):

    cmd = CommandHandler(
        req, "i:fas(/!'^)DfasdbkfjeA/(!'^:11"
    )._CommandHandler__find_operation()
    assert cmd == Commands.TEXT
