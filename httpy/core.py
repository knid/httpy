import requests
from colorama import init

from httpy.arguments import ArgumentParser
from httpy.command.handler import CommandHandler
from httpy.output.error import write_error
from httpy.output.writer import write
from httpy.request import Request
from httpy.status import ExitStatus


def main() -> ExitStatus:
    args = ArgumentParser()
    req = Request.from_args(args)  # Create request object from arguments

    print()

    init(autoreset=True)  # init coloroma

    if not args.command:
        try:
            res = req.make_request()
        except requests.exceptions.InvalidURL:
            write_error("Invalid URL: ", req.url)
            return ExitStatus.ERROR
        write(args, res)
        return ExitStatus.SUCCESS

    command_handler = CommandHandler(req, args.command)
    reqs = command_handler.builder.build_requests()

    for request in reqs:
        try:
            res = request.make_request()
        except requests.exceptions.InvalidURL:
            write_error("Invalid URL: ", req.url)
            return ExitStatus.ERROR
        write(args, res)
    return ExitStatus.SUCCESS
