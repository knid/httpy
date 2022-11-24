import sys

from httpy.output.colors import Colors


def write_error(title: str, content: str) -> None:
    sys.stderr.write(
        Colors.RED + "[ERROR] " + Colors.ENDC + title + Colors.ENDC + content + "\n"
    )
