import sys
from pathlib import Path
from typing import List

import pytest

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))

from httpy.command.builder import RequestBuilder  # noqa: E402
from httpy.command.handler import CommandHandler  # noqa: E402
from httpy.request import Request  # noqa: E402


@pytest.fixture
def req():
    return Request("GET", r"httpbin.org/get?value={i}", {"X-API-Token": r"{i}"})


@pytest.fixture
def handler(req):
    return CommandHandler(req, "i:VALUE")


@pytest.fixture
def builder(handler):
    return RequestBuilder(handler)


def test_command_builder_build_item(
    builder: RequestBuilder, req: Request, handler: CommandHandler
):
    builded = builder._build_item(req.url, handler.value)
    assert builded == f"http://httpbin.org/get?value={handler.value}"


def test_command_builder_build_iterable_item(
    builder: RequestBuilder, req: Request, handler: CommandHandler
):
    builded = builder._build_iterable_item(req.header, handler.value)
    assert builded == {"X-API-Token": f"{handler.value}"}


def test_command_builder_build_request(
    builder: RequestBuilder, req: Request, handler: CommandHandler
):
    builded = builder._build_request(handler.value)
    assert builded.url == f"http://httpbin.org/get?value={handler.value}"
    assert builded.header == {"X-API-Token": f"{handler.value}"}


@pytest.fixture
def builder_increment_3times(req):
    handler = CommandHandler(req, "i:++:3")
    return RequestBuilder(handler)


@pytest.fixture
def builder_deincrement_3times(req):
    handler = CommandHandler(req, "i:--:3")
    return RequestBuilder(handler)


@pytest.fixture
def builder_list(req):
    handler = CommandHandler(req, "i:item1,item2")
    return RequestBuilder(handler)


@pytest.fixture
def builder_text(req):
    handler = CommandHandler(req, "i:text")
    return RequestBuilder(handler)


@pytest.fixture
def builder_rand_3times(req):
    handler = CommandHandler(req, "i:rand(0,5):3")
    return RequestBuilder(handler)


@pytest.fixture
def builder_read(req):
    handler = CommandHandler(req, "i:read(tests/test_file.txt)")
    return RequestBuilder(handler)


def test_command_builder_build_requests_increment(
    builder_increment_3times: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_increment_3times.build_requests())

    assert builded[0].url == "http://httpbin.org/get?value=0"
    assert builded[1].url == "http://httpbin.org/get?value=1"
    assert builded[2].url == "http://httpbin.org/get?value=2"
    assert builded[0].header == {"X-API-Token": "0"}
    assert builded[1].header == {"X-API-Token": "1"}
    assert builded[2].header == {"X-API-Token": "2"}


def test_command_builder_build_requests_deincrement(
    builder_deincrement_3times: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_deincrement_3times.build_requests())

    assert builded[0].url == "http://httpbin.org/get?value=0"
    assert builded[1].url == "http://httpbin.org/get?value=-1"
    assert builded[2].url == "http://httpbin.org/get?value=-2"
    assert builded[0].header == {"X-API-Token": "0"}
    assert builded[1].header == {"X-API-Token": "-1"}
    assert builded[2].header == {"X-API-Token": "-2"}


def test_command_builder_build_requests_list(
    builder_list: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_list.build_requests())

    assert builded[0].url == "http://httpbin.org/get?value=item1"
    assert builded[1].url == "http://httpbin.org/get?value=item2"
    assert builded[0].header == {"X-API-Token": "item1"}
    assert builded[1].header == {"X-API-Token": "item2"}


def test_command_builder_build_requests_text(
    builder_text: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_text.build_requests())

    assert builded[0].url == "http://httpbin.org/get?value=text"
    assert builded[0].header == {"X-API-Token": "text"}


def test_command_builder_build_requests_random(
    builder_rand_3times: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_rand_3times.build_requests())

    assert builded[0].url.endswith(("0", "1", "2", "3", "4", "5"))
    assert builded[1].url.endswith(("0", "1", "2", "3", "4", "5"))
    assert builded[2].url.endswith(("0", "1", "2", "3", "4", "5"))


def test_command_builder_build_requests_read_file(
    builder_read: RequestBuilder, req: Request, handler: CommandHandler
):
    builded: List[Request] = list(builder_read.build_requests())

    with open("tests/test_file.txt", "r") as f:
        lines = f.readlines()
        counter = 0
        for line in lines:
            assert (
                builded[counter].url == f"http://httpbin.org/get?value={line.strip()}"
            )
            counter += 1
