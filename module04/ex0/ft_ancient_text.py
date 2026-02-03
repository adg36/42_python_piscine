#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES – DATA RECOVERY SYSTEM ===\n")

    file = "ancient_fragment.txt"

    print(f"Accessing Storage Vault: {file}")

    try:
        with open(file) as f:
            print("Connection established...\n"
                  "\nRECOVERED DATA:")
            print(f.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    print("\nData recovery complete. Storage unit disconnected.")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
