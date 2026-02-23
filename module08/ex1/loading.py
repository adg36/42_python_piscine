import sys
import importlib


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    libraries = [
            ("pandas", "Data manipulation"),
            ("matplotlib", "Visualization"),
            ("matplotlib.pyplot", "Plotting"),
            ("numpy", "Numerical computations")
    ]

    modules = {}

    for library, purpose in libraries:
        try:
            modules[library] = importlib.import_module(library)
            version = getattr(modules[library], "__version__", "unknown")
            print(f"[OK] {library} ({version}) - {purpose} ready")
        except ImportError:
            print(f"[MISSING] {library}\n"
                  "\nTo install it with pip:\n"
                  "pip install -r requirements.txt\n"
                  "\nTo install it with Poetry:\n"
                  "poetry install\n")
            sys.exit(1)

    print("\nAnalyzing Matrix data...")
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = modules["matplotlib.pyplot"]
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    df = pd.DataFrame(arr)
    print(f"Processing {df.shape[0]} data points...")
    mean = df.mean()
    print("Generating visualization...")
    plt.plot(mean)
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!\n"
          "Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
