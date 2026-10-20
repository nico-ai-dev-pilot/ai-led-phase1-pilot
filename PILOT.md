# Synthetic GitHub collaboration pilot

This directory contains newly authored toy code only. There are no credentials,
customer data, business source code, external dependencies, or model API calls.
The repository's existing README is preserved.

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v
```

The prepared baseline has two tests: 0 -> `0分`, 30 -> `30分`.
The next, separately authorized implementation changes only `duration.py` and
`tests/test_duration.py` to add 60 -> `1時間`, 90 -> `1時間30分` while preserving
both baseline cases. Expected final total: four tests. That implementation has
not started.

CI runs on pull requests to main using standard Ubuntu and Python's standard
library. It has read-only contents permission, no business secrets, no model
API calls, no uploaded artifacts/cache, no deployment, and no merge step.
Local validation does not prove GitHub-side execution or enforcement.
