# Working with this repository

This starter contains a tested offline triage tool, benign exercises and lab documentation. It is not a provisioned analysis VM.

```bash
git clone https://github.com/josephchitalu2/chitalu-analysis-lab.git
cd chitalu-analysis-lab
python3 -m unittest discover -s tests -v
python3 tools/triage.py training/hello.txt
```

After reviewing changes, commit and push through your own authenticated GitHub environment or the authorized connector. Do not commit malware, private evidence, passwords or environment secrets.
