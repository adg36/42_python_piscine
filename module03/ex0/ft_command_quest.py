#!/usr/bin/env python3

import sys


def main() -> None:
    name = f"Program name: {sys.argv[0]}"
    total = f"Total arguments: {len(sys.argv)}"

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(f"No arguments provided!\n{name}\n{total}")
    else:
        print(f"{name}\n"
              f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"{total}")


if __name__ == "__main__":
    main()
