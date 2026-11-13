# Chitalu Malware Analysis and Reverse Engineering Lab

A reproducible research and learning workspace by **Chitalu Software Solutions**.

The goal is a complete, documented analysis workflow: intake, static triage, disassembly, controlled dynamic observation, evidence handling, reporting and detection engineering. This starter contains a working offline static triage tool and benign exercises. It does not install a sandbox, execute samples or claim that a VM boundary has been validated.

## Start here

Requires Python 3.10+ for the included tooling; no third-party packages.
Follow the [first triage exercise](docs/TRIAGE.md) to interpret the result.

```bash
python3 -m unittest discover -s tests -v
python3 tools/triage.py training/hello.txt --output report.json
```

The triage tool calculates SHA-256, Shannon entropy, a coarse file signature and bounded ASCII strings. Results are observations, not a malware verdict. Entropy and a file signature do not establish whether a file is malicious. JSON output escapes non-ASCII and control characters.

Use only the included benign text and source exercises until the VM environment in [docs/LAB_ARCHITECTURE.md](docs/LAB_ARCHITECTURE.md) has been configured and reviewed.

## Repository structure

- tools/triage.py — bounded, offline static metadata collection
- training/ — benign exercises that can be reviewed from source
- tests/ — automated tests using synthetic local fixtures
- docs/LAB_ARCHITECTURE.md — Windows and Linux VM topology and tool plan
- docs/WORKFLOW.md — intake, analysis and reporting procedure
- reports/TEMPLATE.md — reusable report structure
- ROADMAP.md — release scope and implementation milestones

## Workstation and VM plan

The static triage exercise runs without a VM. The planned analysis environment uses separate Windows and Linux guests. The [lab architecture](docs/LAB_ARCHITECTURE.md) explains the isolation and resource plan.

Windows: FLARE-VM, Ghidra, x64dbg, Procmon, Process Explorer, Wireshark, capa, FLOSS and YARA.
Linux: REMnux, Ghidra, GDB, binutils, Python, capa, FLOSS and YARA.
Hypervisor: one with snapshots and a truly isolated internal virtual network.

## Sample handling

Do not commit executable malware, disk or memory images, secrets, victim data or unredacted indicators from private cases. The ignore file is a convenience, not a containment boundary. Automated analysis of untrusted files and even static parsers belong in an isolated analysis guest. Do not submit private samples to public scanning services without permission.

## Status and contribution

Implemented: offline triage, synthetic tests, benign training material, lab procedures and automated repository checks.
Planned: reproducible VM setup evidence, controlled dynamic exercises, detection-rule validation and a report portfolio. See the roadmap.

Keep reproducible observations, limitations, tool versions and hashes with every report. Contributions should improve tools, documentation, exercises or tests; never introduce live samples into the repository.

## Upstream resources

- FLARE-VM: https://github.com/mandiant/flare-vm
- FLARE Learning Hub: https://github.com/mandiant/flare-learning-hub
- REMnux: https://remnux.org/
- Ghidra: https://github.com/NationalSecurityAgency/ghidra
- capa: https://github.com/mandiant/capa
- FLOSS: https://github.com/mandiant/flare-floss
- YARA: https://github.com/VirusTotal/yara
- x64dbg: https://github.com/x64dbg/x64dbg

Original starter code is [MIT licensed](LICENSE). Third-party tools retain their own licenses.

## Maintenance

[Verification](docs/TESTING.md) · [Contributing](CONTRIBUTING.md) · [Security reporting](SECURITY.md)
