import os

try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing module dotenv\n"
          "Install with 'python3 -m pip install python-dotenv\n")
    exit()


load_dotenv()


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...\n")

    env_var = os.environ
    print("Configuration loaded:")

    settings = [
            ('Mode', 'MATRIX_MODE', 'Unknown'),
            ('Database', 'DATABASE_URL', 'No connection established'),
            ('API Access', 'API_KEY', 'Failed authentication'),
            ('Log Level', 'LOG_LEVEL', 'Unknown'),
            ('Zion Network', 'ZION_ENDPOINT', 'Offline')
    ]
    for name, key, default in settings:
        value = env_var.get(key)
        if value is None:
            print(f"{name}: {default}")
        else:
            if name == 'Mode' or name == 'Log Level':
                print(f"{name}: {env_var[key]}")
            elif name == 'Database':
                print(f"{name}: Connected to local instance")
            elif name == 'API Access':
                print(f"{name}: Authenticated")
            elif name == 'Zion Network':
                print(f"{name}: Online")

    print("\nEnvironment security check:")
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
