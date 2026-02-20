import sys
import os
import site


def main() -> None:
    
    is_virtual_env = sys.prefix != sys.base_prefix

    if not is_virtual_env:
        print("MATRIX STATUS: You're still plugged in\n"
              f"\nCurrent Python: {sys.executable}\n"
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
                    f"Virtual Environment: {os.path.basename(os.environ.get("VIRTUAL_ENV", ""))}\n"
                    f"Environment Path: {sys.prefix}\n"
                    "\nSUCCESS: you're in an isolated environment!\n"
                    "Safe to install packages without affecting\n"
                    "the global system.\n"
                    "\nPackage installation path:\n"
                    f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
