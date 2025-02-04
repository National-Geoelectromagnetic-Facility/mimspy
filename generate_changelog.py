"""Generate the changelog for the next release in GitHub Actions.

Extract the latest entry in the History.rst file and write it to the
changelog.rst file. This is used to populate the changelog in the release.
"""

import re
from pathlib import Path


def generate(pth: str | Path):
    """Generate the changelog.rst file."""
    with open(pth) as fle:
        lines = fle.readlines()

    start = 0
    end = 0
    for i, line in enumerate(lines):
        if re.match(r"\d+.\d+.\d+", line):
            if start == 0:
                start = i
            else:
                end = i
                break

    with open("CHANGELOG.rst", "w") as fle:
        fle.writelines(lines[start:end])


if __name__ == "__main__":
    history_path = "HISTORY.rst"
    generate(history_path)
