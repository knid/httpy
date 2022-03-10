import requests

from httpy.arguments import ArgumentParser
from httpy.command.handler import CommandHandler  # noqa: F401
from httpy.output.error import print_error
from httpy.output.writer import write
from httpy.request import Request
from httpy.status import ExitStatus


def main() -> ExitStatus:
    args = ArgumentParser()
    req = Request.from_args(args)

    print()

    if not args.command:
        try:
            res = req.make_request()  # noqa: F841
        except requests.exceptions.InvalidURL:
            print_error("Invalid URL: ", req.url)
            return ExitStatus.ERROR
        write(args, res)
        return ExitStatus.SUCCESS
