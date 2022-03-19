from httpy.output.colors import Colors


def print_error(title: str, content: str) -> None:
    print(Colors.RED + "[ERROR] " + Colors.ENDC + title + Colors.ENDC + content)
