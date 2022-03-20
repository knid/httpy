import json

import requests
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import HtmlLexer, JsonLexer

ENCODING = "ISO-8859-1"


def print_html(res: requests.Response):
    for html in res.iter_lines():
        decoded = html.decode(ENCODING)
        highlighted_html = highlight(decoded, HtmlLexer(), TerminalFormatter())
        print(highlighted_html, end="")
    print()


def print_json(res: requests.Response):
    highlighted_json = highlight(
        json.dumps(res.json(), indent=4, sort_keys=True),
        JsonLexer(),
        TerminalFormatter(),
    )
    print(highlighted_json)
