import sys
from pathlib import Path

current_path = Path(__file__).parent.parent.parent.resolve()
sys.path.append(str(current_path))


def main():
    try:
        from httpy.core import main

        main()
    except KeyboardInterrupt:
        print(0)
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
