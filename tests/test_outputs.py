import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    with REPORT.open() as f:
        return json.load(f)


def test_success_criterion_1():
    """Success criterion 1: valid JSON with required keys."""
    report = load()
    assert set(report) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_success_criterion_2():
    """Success criterion 2: correct total request count."""
    report = load()
    assert report["total_requests"] == 6


def test_success_criterion_3():
    """Success criterion 3: correct number of unique IPs."""
    report = load()
    assert report["unique_ips"] == 3


def test_success_criterion_4():
    """Success criterion 4: correct top path."""
    report = load()
    assert report["top_path"] == "/index.html"
