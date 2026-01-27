import sys


def ft_command_quest() -> None:
    name = f"Program name: {sys.argv[0]}\n"

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(f"No arguments provided!\n{name}"
              f"Total arguments: {len(sys.argv)}")
    else:
        print(f"{name}"
              f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    main()
