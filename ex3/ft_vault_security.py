def secure_archive(
    filename: str,
    operation: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        with open(filename, operation) as file:
            if operation == "r":
                return (True, file.read())
            file.write(content)
            return (True, "Content successfully written to file")
    except Exception as err:
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))


if __name__ == "__main__":
    main()
