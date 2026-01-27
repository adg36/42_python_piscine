import sys


def ft_command_quest() -> None:
    name = f"Program name: {sys.argv[0]}"
    total = f"Total arguments: {len(sys.argv)}"

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(f"No arguments provided!\n{name}\n{total}")
    else:
        print(f"{name}\n"
              f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"{total}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    main()
