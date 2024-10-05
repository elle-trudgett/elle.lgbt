import datetime
import glob
import os
from pathlib import Path



def get_modified_date(file_path):
    mod_time = os.path.getmtime(file_path)
    mod_datetime = datetime.datetime.fromtimestamp(mod_time)
    return mod_datetime.strftime("%Y-%m-%d")


def assemble():
    path = Path(r"deploy")

    for fn in path.glob("**/*.html"):
        with open(fn, "r") as f:
            lines = f.readlines()

        m_date = get_modified_date(fn)

        lines = [
            line.replace(";modified_date;", m_date)
            for line in lines
        ]

        with open(fn, "w") as f:
            f.writelines(lines)

        print(f"Assembled {fn} with modified date {m_date}")


def main():
    assemble()


if __name__ == '__main__':
    main()