#!/usr/bin/env python3

import sys


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    filenames = ["lost_archive.txt",
                 "classified_vault.txt", "standard_archive.txt"]

    for filename in filenames:
        error_message = f"CRISIS ALERT: Attempting access to '{filename}'...\n"
        try:
            with open(filename) as f:
                data = f.read()
        except FileNotFoundError:
            print(error_message, end="", file=sys.stderr)
            print("RESPONSE: Archive not found in storage matrix\n"
                  "STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print(error_message, end="", file=sys.stderr)
            print("RESPONSE: Security protocols deny access\n"
                  "STATUS: Crisis handled, security maintained\n")
        except Exception as e:
            print(error_message, end="", file=sys.stderr)
            print(f"RESPONSE: Unexpected system anomaly ({e})\n"
                  "STATUS: Crisis handled, anomaly contained\n")
        else:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered – ''{data}''\n"
                  "STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")


def main() -> None:
    ft_crisis_response()


if __name__ == "__main__":
    main()
