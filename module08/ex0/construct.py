import sys
import os
import site


def main() -> None:

    # sys.prefix points to virtual env when running on a virtual env
    # sys.base_prefix always points to the base Python installation
    # if they are different, it means we are on a virtual environment

    is_virtual_env = sys.prefix != sys.base_prefix

    if not is_virtual_env:
        print("MATRIX STATUS: You're still plugged in\n"
              f"\nCurrent Python: {sys.executable}\n"
              # prints absolute path of the binary for the Python interpreter
              "Virtual Environment: None detected\n"
              "\nWARNING: You're still in the global environment!\n"
              "The machines can see everything you install.\n"
              "\nTo enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate    #On Windows\n"
              "\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n"
              f"\nCurrent Python: {sys.executable}\n"
              # prints the env variable called VIRTUAL_ENV
              # from the base name of path
              "Virtual Environment: "
              f"{os.path.basename(os.environ.get("VIRTUAL_ENV", ""))}\n"
              f"Environment Path: {sys.prefix}\n"
              "\nSUCCESS: you're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n"
              "\nPackage installation path:\n"
              # returns a list of site packages directories
              f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
