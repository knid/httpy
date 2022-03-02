import pytest

from httpcli.core.arguments import Arguments


@pytest.fixture
def example_args():
    args = Arguments(
        [
            "POST",
            "Content-Type:application/json",
            "email=example@mail.com",
            "password=testpass123",
            "id==312",
        ],
    )
    return args


def test_header(example_args):
    headers = example_args.headers
    assert headers == {"Content-Type": "application/json"}


def test_body_arg(example_args):
    body = example_args.body
    assert body == {"email": "example@mail.com", "password": "testpass123"}


def test_url_arg(example_args):
    arguments = example_args.arguments
    assert arguments == {"id": "312"}


def test_method(example_args):
    method = example_args.method
    assert method == Arguments.METHODS["POST"]
