#!/usr/bin/env python3
"""Offline static triage. Reads bytes only; never loads or executes a sample."""
import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
import re
import stat

DEFAULT_MAX = 64 * 1024 * 1024
MAX_STRINGS = 200
MAX_STRING_LENGTH = 240

def entropy(data):
    if not data:
        return 0.0
    total = len(data)
    return -sum((n / total) * math.log2(n / total)
                for n in collections.Counter(data).values())

def coarse_type(data):
    if data.startswith(b"\x7fELF"):
        return "ELF signature"
    if data.startswith(b"MZ"):
        return "DOS MZ signature (PE format not verified)"
    if data.startswith(b"PK\x03\x04"):
        return "ZIP local-file signature"
    if data.startswith(b"%PDF-"):
        return "PDF signature"
    return "Unknown"

def summarize(data, name="sample"):
    strings = []
    for match in re.finditer(rb"[\x20-\x7e]{5,}", data):
        strings.append({
            "offset": match.start(),
            "text": match.group()[:MAX_STRING_LENGTH].decode("ascii"),
            "truncated": len(match.group()) > MAX_STRING_LENGTH,
        })
        if len(strings) == MAX_STRINGS:
            break
    return {
        "schema_version": 1,
        "sample_name": name,
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "coarse_type": coarse_type(data),
        "shannon_entropy_bits_per_byte": round(entropy(data), 6),
        "ascii_strings": strings,
        "strings_limit": MAX_STRINGS,
        "analysis": "Static bytes only; no execution, uploads or network requests.",
        "limits": "Signatures, strings and entropy do not establish maliciousness.",
    }

def analyze_file(path, max_bytes=DEFAULT_MAX):
    if max_bytes < 1:
        raise ValueError("max_bytes must be positive")
    path = Path(path)
    if path.is_symlink():
        raise ValueError("Symbolic links are not accepted")
    with path.open("rb") as handle:
        metadata = __import__("os").fstat(handle.fileno())
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError("Input must be a regular file")
        if metadata.st_size > max_bytes:
            raise ValueError("Sample exceeds byte limit")
        data = handle.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("Sample grew beyond byte limit while reading")
    return summarize(data, path.name)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sample", type=Path)
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX,
                        help="Maximum bytes to read (default 64 MiB)")
    parser.add_argument("--output", type=Path,
                        help="New JSON report file; existing files are not overwritten")
    args = parser.parse_args()
    try:
        report = analyze_file(args.sample, args.max_bytes)
        result = json.dumps(report, indent=2, ensure_ascii=True) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(result)
        else:
            print(result, end="")
    except (OSError, ValueError) as exc:
        parser.exit(2, "Triage failed: " + ascii(str(exc)) + "\n")

if __name__ == "__main__":
    main()
