#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open("ancient_fragment.txt")
        print("Connection established...\n"
              "\nRECOVERED DATA:")
        print(file.read())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ft_ancient_text()
