#!/usr/bin/env python3

import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES – COMMUNICATION SYSTEM ===\n")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


def main() -> None:
    ft_stream_management()


if __name__ == "__main__":
    main()
