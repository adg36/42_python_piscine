#!/usr/bin/env python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES – VAULT SECURITY SYSTEM ===\n")

    file = "classified_data.txt"

    print("Initiating secure vault access...")

    try:
        with open(file, "r") as f:
            print("Vault connection established with failsafe protocols\n"
                  "\nSECURE EXTRACTION:")
            print(f.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found.\n")

    with open(file, "a+") as f:
        print("\nSECURE PRESERVATION:")
        line = "[CLASSIFIED] New security protocols archived\n"
        f.write(line)
        print(line, end="")

    print("Vault automatically sealed upon completion.\n")
    print("All vault operations completed with maximum security.")


def main() -> None:
    ft_vault_security()


if __name__ == "__main__":
    main()
