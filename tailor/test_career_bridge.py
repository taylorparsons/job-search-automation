#!/usr/bin/env python3
"""Focused tests for the local career-bank bridge. Run: python3 -m unittest tailor.test_career_bridge"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("reverse_recruiter_tailor", ROOT / "tailor.py")
assert SPEC and SPEC.loader
tailor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tailor)


FAKE_CLI = '''
from dataclasses import dataclass
@dataclass
class Achievement:
    score: float
    company: str
    exp_id: str
    ach_id: str
    text: str
    tags: list[str]
def tailor(bank, jd, top_n):
    return [Achievement(0.91, "Example Co", "exp-1", "ach-1", "Built a reliable AI platform.", ["platform"])]
def render_resume_markdown(bank, selected, title=None):
    return f"# {title}\\n\\n" + selected[0].text + "\\n"
def render_resume_docx_bytes(bank, selected, title=None):
    return b"DOCX"
'''


class CareerBridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "career_cli.py").write_text(FAKE_CLI, encoding="utf-8")
        (self.root / "bank.json").write_text(json.dumps({"person": {}}), encoding="utf-8")
        (self.root / "graph.json").write_text(json.dumps({"nodes": [], "edges": [
            {"from": "achievement:ach-1", "to": "tag:platform", "type": "tagged"}
        ]}), encoding="utf-8")
        self.role_path = self.root / "role.json"
        self.role_path.write_text(json.dumps({"company": "Example Co", "title": "AI PM", "job_description": "AI platform role"}), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_generates_resume_and_graph_tagged_evidence(self):
        out = self.root / "out"
        out.mkdir()
        resume, evidence, docx = tailor.build_career_materials(
            career_cli_path=str(self.root / "career_cli.py"),
            career_bank_path=str(self.root / "bank.json"),
            career_graph_path=str(self.root / "graph.json"),
            role=json.loads(self.role_path.read_text()),
            role_path=self.role_path,
            outdir=out,
            write_docx=True,
            top=12,
        )
        self.assertIn("Built a reliable AI platform.", resume.read_text())
        self.assertIn("Tags: platform", evidence.read_text())
        self.assertEqual(docx.read_bytes(), b"DOCX")
        self.assertFalse((self.root / "role.jd.txt").exists())

    def test_requires_a_job_description(self):
        with self.assertRaises(SystemExit) as error:
            tailor._load_job_description({}, self.role_path)
        self.assertIn("job_description", str(error.exception))

    def test_rejects_invalid_graph_shape(self):
        bad_graph = self.root / "bad-graph.json"
        bad_graph.write_text("{}", encoding="utf-8")
        with self.assertRaises(SystemExit) as error:
            tailor._graph_tags(str(bad_graph))
        self.assertIn("edges", str(error.exception))


if __name__ == "__main__":
    unittest.main()
