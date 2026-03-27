import sys
import importlib


def main() -> None:

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    libraries = [
            ("pandas", "Data manipulation"),
            ("numpy", "Numerical computations"),
            ("matplotlib", "Visualization")
    ]

    modules = {}

    failed = False
    for library, purpose in libraries:
        try:
            modules[library] = importlib.import_module(library)
        except (ImportError, AttributeError):
            failed = True
            print(f"[MISSING] {library}")
        else:
            version = getattr(modules[library], "__version__", "unknown")
            print(f"[OK] {library} ({version}) - {purpose} ready")
    if failed:
        print("\nTo install the dependencies with pip:\n"
              "pip install -r requirements.txt\n"
              "\nTo install them with Poetry:\n"
              "poetry install\n")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    import matplotlib.pyplot as plt
    np = modules["numpy"]
    pd = modules["pandas"]
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    df = pd.DataFrame(arr)
    print(f"Processing {np.sum(arr)} data points...")
    mean = df.mean()
    print("Generating visualization...")
    plt.plot(mean)
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!\n"
          "Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
