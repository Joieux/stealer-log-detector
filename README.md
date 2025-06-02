# Stealer‑Log Detector 🚨

[![CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Joieux/stealer-log-detector/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/Joieux/stealer-log-detector)](https://github.com/Joieux/stealer-log-detector/commits/main)

A fast, lightweight CLI tool to scan directories for credential‑stealer log archives (ZIP, RAR, 7z, tar/gz) produced by common infostealer malware such as RedLine, Raccoon, Vidar, and others.  
Stealer‑Log Detector works recursively, identifies high-value artifacts (like `Passwords.txt`, browser `Cookies/`, crypto wallets, etc.), and outputs JSON reports suitable for SIEM ingestion.  
No external services, no telemetry – just efficient, signature-based detection for infosec professionals, threat analysts, and incident responders.

---

## Features

- Signature‑based detection of high‑value artefacts: `Passwords.txt`, `Cookies/`, `wallets/`, and more.
- Supports **ZIP**, **RAR**, **7z**, **tar.gz** formats without extracting files to disk.
- Severity scoring: **CONFIRMED** (≥ 2 high‑confidence hits) vs **LIKELY**.
- Fast, fully local scanning—no external requests.
- JSON reporting for integration into SIEM and automation pipelines.
- MIT‑licensed, open source, and easy to extend.

---

## Installation

```bash
python -m pip install -r requirements.txt
