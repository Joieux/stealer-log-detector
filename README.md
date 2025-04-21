# Stealer‑Log Detector 🚨

A lightweight CLI tool that scans folders (recursively) for **credential‑stealer log archives** (ZIP, RAR, 7z, tar/gz) produced by common infostealer malware families such as RedLine, Raccoon, Vidar, Lumma, and more.

| CI | License |
|----|---------|
| ![CI](https://img.shields.io/badge/build-passing-brightgreen) | MIT |

## Features

* Signature‑based detection of high‑value artefacts (`Passwords.txt`, `Cookies/`, `wallets/`, etc.).
* Supports **ZIP**, **RAR**, **7z**, **tar/gz** without extracting files to disk.
* Severity scoring: **CONFIRMED** (≥ 2 high‑confidence hits) vs **LIKELY**.
* JSON reporting for SIEM ingestion.
* MIT‑licensed, zero external services.

## Installation

```bash
python -m pip install -r requirements.txt
```

(ZIP support only? You can skip `rarfile`/`py7zr`.)

## Usage

```bash
# Find likely and confirmed logs:
python stealer_log_detector.py --path ~/Downloads

# Emit only confirmed and save JSON:
python stealer_log_detector.py -p C:\ --confirmed-only --report hits.json
```

## Updating signatures

Edit the `HIGH_CONF_SIGS` and `MEDIUM_CONF_SIGS` regex lists in `stealer_log_detector.py` as new stealer families emerge.

## Contributing

1. Fork ➜ Fix ➜ PR  
2. Add unit tests for new functionality  
3. Respect the [Code of Conduct](CODE_OF_CONDUCT.md)

## Disclaimer

This software is provided **“as is”**. Use it only on systems you own or have explicit permission to audit. The authors are **not** responsible for misuse or data loss.

## License

[MIT](LICENSE)
