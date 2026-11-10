# Analysis Workflow

1. Intake: establish permission, provenance, case ID, handling rules and confidentiality.
2. Preserve: calculate SHA-256; record size, acquisition timestamp and custody; work from a copy.
3. Static triage: collect signatures, strings and entropy using the included tool inside an analysis guest.
4. Disassembly: inspect entry points, imports, strings and control flow; annotate evidence and uncertainty.
5. Controlled dynamics: only after isolation verification, observe processes, files, registry and simulated network traffic.
6. Memory analysis: collect a memory image where the exercise permits; record acquisition method and integrity.
7. Detection engineering: write YARA or behavior rules from observed facts; test against benign and relevant positive fixtures.
8. Report: distinguish observations, hypotheses and conclusions. Record indicators, limitations and reproducible steps.
9. Restore: revert the guest and verify the clean snapshot before the next case.

Do not upload a private sample, memory dump or case report to a public scanning service. Reports intended for GitHub must be redacted and authorized for release.
