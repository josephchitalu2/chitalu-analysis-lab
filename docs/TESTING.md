# Verification

Requires Python 3.10+; no third-party dependencies for these checks. Run from the repository root:

```bash
python3 scripts/check_docs.py

python3 -m unittest discover -s tests -v
python3 tools/triage.py training/hello.txt
```

The lab has eight synthetic-fixture unit tests for its static triage tool. These tests do not establish VM containment, dynamic malware behavior or detection accuracy.

GitHub Actions runs the available checks on pushes and pull requests. Record actual browser, environment, service-integration and recovery tests when those features exist. Do not interpret passing link checks as production or security verification.
