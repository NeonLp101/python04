"""Stream Management: same archive tool, driven through the three channels."""

import sys
from typing import IO


def main() -> None:
    """Process a file using direct stream management (no input())."""
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        filestream: IO[str] = open(filename, "r")
        try:
            content: str = filestream.read()
        finally:
            filestream.close()
    except Exception as read_err:
        print(
            f"[STDERR] Error opening file '{filename}': {read_err}",
            file=sys.stderr,
        )
        return

    print("---\n")
    print(content)
    print("---")
    print(f"File '{filename}' closed.")

    print("\nTransform data:")
    lines: list[str] = content.splitlines()
    modified_lines: list[str] = [line + "#" for line in lines]
    new_content: str = "\n".join(modified_lines) + "\n"
    print("---\n")
    print(new_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name: str = sys.stdin.readline().rstrip("\r\n")

    if new_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    try:
        writestream: IO[str] = open(new_name, "w")
        try:
            writestream.write(new_content)
        finally:
            writestream.close()
    except Exception as write_err:
        print(
            f"[STDERR] Error opening file '{new_name}': {write_err}",
            file=sys.stderr,
        )
        print("Data not saved.")
        return

    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
