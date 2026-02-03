#!/usr/bin/env python3

def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES – PRESERVATION SYSTEM ===")

    file = "new_discovery.txt"

    with open(file, "w") as f:
        file = "new_discovery.txt"
        print(f"\nInitializing new storage unit: {file}")
        print("Storage unit created successfully...\n"
              "\nInscribing preservation data...")
        f.write("[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee\n")

    with open(file, "r") as f:
        print(f.read())

    print("Data inscription complete. Storage unit sealed.\n"
          f"Archive '{file}' ready for long-term preservation.")


def main() -> None:
    ft_archive_creation()


if __name__ == "__main__":
    main()
