import compileall
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON_FILES = [
    ROOT / "medilink_contract.py",
    ROOT / "config.py",
    ROOT / "demo_summary.py",
    *sorted((ROOT / "tests").glob("*.py")),
    *sorted((ROOT / "scripts").glob("*.py")),
]


def main() -> int:
    compilation_failed = False
    for path in PYTHON_FILES:
        if not compileall.compile_file(str(path), quiet=1):
            compilation_failed = True

    if compilation_failed:
        return 1

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-v",
        ],
        cwd=ROOT,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
