import argparse

import pytest

from httpcli.core.arguments import ArgumentParser


@pytest.fixture
def example_args():
    parser = ArgumentParser()
    return parser.parse_args(
        namespace=argparse.Namespace(
            # URL='example.com', Set default=test.com and nargs='?' in URL in ArgumentParser !!!
            header={"Content-Type": "application/json"},
            body={"email": "example@mail.com", "password": "testpass123"},
            query_arguments={"id": "312"},
            allow_redirect=True,
        )
    )


def test_header(example_args):
    print(example_args)
    headers = example_args.header
    assert headers == {"Content-Type": "application/json"}


def test_body_arg(example_args):
    body = example_args.body
    assert body == {"email": "example@mail.com", "password": "testpass123"}


def test_url_arg(example_args):
    arguments = example_args.query_arguments
    assert arguments == {"id": "312"}


def test_method(example_args):
    method = example_args.method
    assert method == "GET"
