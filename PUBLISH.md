# Publishing analysis lab changes

This starter contains a tested offline triage tool, benign exercises and lab documentation. It is not a provisioned analysis VM.

```bash
git clone https://github.com/josephchitalu2/chitalu-analysis-lab.git
cd chitalu-analysis-lab
python3 -m unittest discover -s tests -v
python3 tools/triage.py training/hello.txt
```

Run the checks in [the verification guide](docs/TESTING.md) and review the staged files before opening a pull request. Publish source, benign fixtures and approved, redacted reports. Keep malware, private evidence, passwords and environment secrets out of the repository.
