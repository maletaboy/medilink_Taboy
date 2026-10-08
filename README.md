# MediLink Integration CI Lab

A small Python project for practicing Git branches, focused commits, pull
requests, GitHub Actions, configuration through environment variables, and
contract tests.

## Local setup (Windows PowerShell)

From this project folder, create and activate a virtual environment:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Run the demonstration and tests:

```powershell
python demo_summary.py
python -m unittest discover -s tests -v
python scripts/run_ci_checks.py
```

No third-party Python packages are required.

## Environment configuration

Copy `.env.example` to `.env` as a reference for local values. The application
reads environment variables directly and does not automatically load `.env`.
Set values for the current PowerShell session like this:

```powershell
$env:MEDILINK_API_KEY = "local-demo-only"
$env:REQUEST_TIMEOUT = "5"
```

Never commit `.env` or a real credential. In GitHub, add the disposable lab
value as the `MEDILINK_API_KEY` Actions repository secret.

## CI

`.github/workflows/integration-ci.yml` runs syntax checks and unit tests for
pushes to `main`, `feature/**`, and `fix/**`, and for pull requests targeting
`main`.
