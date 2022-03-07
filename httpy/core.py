def main():

    from httpy.arguments import ArgumentParser
    from httpy.command.handler import CommandHandler  # noqa: F401
    from httpy.request import Request

    args = ArgumentParser()

    req: Request = Request.from_args(args)

    if not args.command:
        print(req.make_request().status)


main()
