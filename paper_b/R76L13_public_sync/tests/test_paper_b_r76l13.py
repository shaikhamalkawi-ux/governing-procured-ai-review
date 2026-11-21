"""Small public-safe package test (no independent full-text verification)."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/'scripts'/'verify_public_release.py'
spec=importlib.util.spec_from_file_location('paper_b_r76l13_verify',SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ReleaseValidation(unittest.TestCase):
    def test_release(self):
        module.validate()

if __name__=='__main__':
    unittest.main()
