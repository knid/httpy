import sys
from pathlib import Path


def main():
    current_path = Path(__file__).parent.parent.resolve()
    sys.path.append(str(current_path))
    try:
        from httpy.core import main

        exit_status = main()
    except KeyboardInterrupt:
        from httpy.status import ExitStatus

        exit_status = ExitStatus.KEYBOARD_INTERRUPT
    print()
    return exit_status.value


if __name__ == "__main__":
    sys.exit(main())
