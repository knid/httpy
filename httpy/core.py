from httpy.arguments import ArgumentParser
from httpy.command.handler import CommandHandler  # noqa: F401
from httpy.request import Request
from httpy.status import ExitStatus


def main() -> ExitStatus:
    args = ArgumentParser()
    req = Request.from_args(args)

    if not args.command:
        res = req.make_request()  # noqa: F841
        return ExitStatus.SUCCESS
