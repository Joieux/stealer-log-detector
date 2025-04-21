#!/usr/bin/env python3
"""
Stealer‑Log Detector
Detects credential‑stealer log archives by inspecting their internal filenames.

:copyright: (c) 2025, Joyce Johnson
:license: MIT, see LICENSE for more details.
"""

import os, re, json, argparse, hashlib, logging
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile, BadZipFile
from typing import List, Dict, Tuple

try:
    import rarfile
except ImportError:
    rarfile = None
try:
    import py7zr
except ImportError:
    py7zr = None

logging.basicConfig(level=logging.WARNING, format="%(levelname)s ▸ %(message)s")

HIGH_CONF_SIGS = [
    re.compile(r"(?i)^Passwords\.txt$"),
    re.compile(r"(?i)^Cookies\.txt$"),
    re.compile(r"(?i)^Autofill\.txt$"),
    re.compile(r"(?i)[/\\]wallets?[/\\]"),
    re.compile(r"(?i)^Information[/\\]System info\.txt$"),
    re.compile(r"(?i)^Discord_token\.txt$"),
]
MEDIUM_CONF_SIGS = [
    re.compile(r"(?i)^Steam[/\\]"),
    re.compile(r"(?i)^Telegram Desktop[/\\]"),
    re.compile(r"(?i)^History\.txt$"),
    re.compile(r"(?i)^VPN[/\\]"),
    re.compile(r"(?i)\.ldb$"),
]

ARCHIVE_EXTS = {".zip", ".rar", ".7z", ".gz", ".tar", ".tgz"}

def hash_path(p: Path) -> str:
    return hashlib.sha1(str(p).encode()).hexdigest()[:10]

def list_archive_files(path: Path) -> List[str]:
    names: List[str] = []
    ext = path.suffix.lower()
    try:
        if ext == ".zip":
            with ZipFile(path) as zf:
                names = zf.namelist()
        elif ext == ".rar" and rarfile:
            with rarfile.RarFile(path) as rf:
                names = rf.namelist()
        elif ext == ".7z" and py7zr:
            with py7zr.SevenZipFile(path, mode="r") as sz:
                names = sz.getnames()
        elif ext in {".gz", ".tgz", ".tar"}:
            names = ["<single-file-archive>"]
    except Exception as e:
        logging.debug(f"Cannot open {path}: {e}")
    return names

def score_names(names: List[str]) -> Tuple[int, int]:
    high = sum(1 for n in names if any(rx.search(n) for rx in HIGH_CONF_SIGS))
    medium = sum(1 for n in names if any(rx.search(n) for rx in MEDIUM_CONF_SIGS))
    return high, medium

def scan_path(root: Path, min_severity: str = "likely") -> List[Dict]:
    hits = []
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in ARCHIVE_EXTS:
            continue
        names = list_archive_files(p)
        if not names:
            continue
        high, med = score_names(names)
        severity = None
        if high >= 2:
            severity = "confirmed"
        elif high == 1 or med >= 3:
            severity = "likely"
        if severity and (severity == "confirmed" or min_severity == "likely"):
            hits.append({
                "file": str(p),
                "sha1": hash_path(p),
                "high_hits": high,
                "medium_hits": med,
                "severity": severity,
                "size_kb": round(p.stat().st_size / 1024, 1),
                "detected": datetime.utcnow().isoformat() + "Z",
            })
    return hits

def main():
    ap = argparse.ArgumentParser(description="Detect credential‑stealer log archives")
    ap.add_argument("-p", "--path", required=True, help="Directory to scan")
    ap.add_argument("-r", "--report", help="Save results to JSON file")
    ap.add_argument("-e", "--confirmed-only", action="store_true",
                    help="Only show CONFIRMED logs (hide 'likely')")
    args = ap.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists():
        ap.error(f"{root} does not exist")

    severity_floor = "confirmed" if args.confirmed_only else "likely"
    results = scan_path(root, severity_floor)
    if args.report:
        Path(args.report).write_text(json.dumps(results, indent=2))
        print(f"[+] Report saved to {args.report} ({len(results)} hits)")
    else:
        for r in results:
            print(f"[{r['severity'].upper():9}] {r['file']} "
                  f"(high={r['high_hits']} med={r['medium_hits']}, {r['size_kb']} KB)")

if __name__ == "__main__":
    main()