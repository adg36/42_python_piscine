#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES – DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    
    try:
        file = open("ancient_fragment.txt")
        print("Connection established...\n"
              "\nRECOVERED DATA:")
        print(file.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


def main() -> None:
    ft_ancient_text()


if __name__ == "__main__":
    main()
