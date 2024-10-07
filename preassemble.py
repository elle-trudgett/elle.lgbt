from pathlib import Path


def preassemble():
    path = Path(r"deploy")

    for fn in path.glob("**/*.html"):
        # Make a backup of the original file
        with open(str(fn) + ".old", "w") as f:
            with open(fn, "r") as f2:
                f.writelines(f2.readlines())


def main():
    preassemble()


if __name__ == '__main__':
    main()