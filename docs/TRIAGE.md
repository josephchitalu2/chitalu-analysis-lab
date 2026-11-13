# First static triage exercise

Start with `training/hello.txt`, a known benign file. From the repository root:

```bash
python3 tools/triage.py training/hello.txt
```

The command prints JSON to the terminal. Use `--output report.json` to save it to a
new file instead. The tool refuses to overwrite a report; choose a new filename
for a second run.

| Field | What to look for in this exercise |
| --- | --- |
| `size_bytes` | The checked-in fixture is 115 bytes. |
| `sha256` | Compare the hash before and after moving the file. A filename change does not change the hash. |
| `coarse_type` | `Unknown`: the file does not start with any of the signatures the tool checks. |
| `shannon_entropy_bits_per_byte` | A summary of byte distribution. Use it as an observation, not a verdict. |
| `ascii_strings` | Each string has a byte offset. The output is bounded and does not contain all possible strings. |

The [example report](../reports/benign-triage-example.json) shows the JSON format.
Try running the same command on `training/intro.c` and describe one difference in
the results using the [report template](../reports/TEMPLATE.md).

The default read limit is 64 MiB. To practise handling a rejected input safely,
run `python3 tools/triage.py training/hello.txt --max-bytes 32`. The file is larger
than that limit, so the command exits with a clear error.

Use these fixtures to learn the workflow. Follow the [lab isolation plan](LAB_ARCHITECTURE.md)
and the [sample handling procedure](WORKFLOW.md) before inspecting an untrusted file.
