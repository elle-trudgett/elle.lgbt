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
        old_fn = str(fn) + ".old"
        old_lines = []
        if os.path.exists(old_fn):
            with open(old_fn, "r") as f:
                old_lines = f.readlines()
            for line in old_lines:
                if ";modified_date;" in line:
                    old_lines = []
                    break
        with open(fn, "r") as f:
            new_pandoc_lines = f.readlines()

        m_date = get_modified_date(fn)

        lines_to_write = [
            line.replace(";modified_date;", m_date)
            for line in new_pandoc_lines
        ]

        # if the only difference is the date line, revert it
        different_lines = set(old_lines) ^ set(new_pandoc_lines)
        for l in different_lines:
            if "updated" and "time" in l:
                continue
            else:
                print(f"✅ Change detected to {fn}")
                break
        else:
            # only the date line is different, revert
            lines_to_write = old_lines
            print(f"No change detected to {fn}")

        with open(fn, "w") as f:
            f.writelines(lines_to_write)

        print(f"Assembled {fn} with modified date {m_date}")


def remove_old():
    path = Path(r"deploy")

    for fn in path.glob("**/*.old"):
        os.remove(fn)
        print(f"Removed {fn}")


def main():
    assemble()
    remove_old()


if __name__ == '__main__':
    main()