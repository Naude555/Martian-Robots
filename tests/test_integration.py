import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_sample_input_produces_expected_output():
    sample_input = (PROJECT_ROOT / "sample.txt").read_text()
    expected_output = (PROJECT_ROOT / "sample_expected_output.txt").read_text()

    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=PROJECT_ROOT,
        input=sample_input,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout.splitlines() == expected_output.splitlines()
