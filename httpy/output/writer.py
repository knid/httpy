import requests

from httpy.arguments import ArgumentParser
from httpy.output.http import print_body, print_headers, print_status


def write(args: ArgumentParser, res: requests.Response):
    if args.filter:
        if args.show_status:
            print_status(res)
        if args.show_header:
            print_headers(res)
        if args.show_body:
            print_body(res)
    else:
        print_status(res)
        print_headers(res)
        print_body(res)
