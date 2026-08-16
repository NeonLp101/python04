import sys
from typing import IO


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        filestream: IO[str] = open(filename, "r")
        try:
            content: str = filestream.read()
        finally:
            filestream.close()
    except Exception as read_err:
        print(f"Error opening file '{filename}': {read_err}")
        return

    print("---\n")
    print(content)
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
