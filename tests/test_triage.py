import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

module_path = Path(__file__).resolve().parents[1] / "tools" / "triage.py"
spec = importlib.util.spec_from_file_location("triage", module_path)
triage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(triage)

class TriageTests(unittest.TestCase):
    def test_known_digest(self):
        self.assertEqual(triage.summarize(b"abc")["sha256"],
                         hashlib.sha256(b"abc").hexdigest())

    def test_entropy_extremes(self):
        self.assertEqual(triage.entropy(b""), 0)
        self.assertEqual(triage.entropy(b"aaaa"), 0)
        self.assertAlmostEqual(triage.entropy(bytes(range(256))), 8)

    def test_coarse_type_does_not_claim_valid_pe(self):
        self.assertIn("not verified", triage.coarse_type(b"MZfake"))
        self.assertEqual(triage.coarse_type(b"\x7fELF"), "ELF signature")

    def test_string_offsets_and_control_exclusion(self):
        result = triage.summarize(b"\0hello\0world\x1b\0")
        self.assertEqual(result["ascii_strings"][0]["offset"], 1)
        self.assertEqual(result["ascii_strings"][0]["text"], "hello")
        self.assertNotIn("\x1b", "".join(x["text"] for x in result["ascii_strings"]))

    def test_string_count_and_length_bounded(self):
        data = b"x" * 600 + b"\0" + b"abcde\0" * 500
        result = triage.summarize(data)["ascii_strings"]
        self.assertEqual(len(result), 200)
        self.assertEqual(len(result[0]["text"]), 240)
        self.assertTrue(result[0]["truncated"])

    def test_maximum_input_size_enforced(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(b"hello")
            with self.assertRaises(ValueError):
                triage.analyze_file(path, max_bytes=4)

    def test_file_is_read_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "benign.txt"
            path.write_bytes(b"#!/bin/sh\nnot a script to run\n")
            result = triage.analyze_file(path)
            self.assertEqual(result["size_bytes"], path.stat().st_size)
            self.assertEqual(path.read_bytes(), b"#!/bin/sh\nnot a script to run\n")

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            original = Path(directory) / "a.txt"
            original.write_text("hello")
            link = Path(directory) / "link"
            try:
                link.symlink_to(original)
            except OSError:
                self.skipTest("symlinks unavailable")
            with self.assertRaises(ValueError):
                triage.analyze_file(link)

if __name__ == "__main__":
    unittest.main()
