Certainly! Here is the improved `README.md` file for your project. You can copy and paste this directly into your repository:

```markdown
# Stealer‑Log Detector 🚨

[![CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Joieux/stealer-log-detector/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/Joieux/stealer-log-detector)](https://github.com/Joieux/stealer-log-detector/commits/main)

> **Fast, signature-based CLI scanner for credential-stealer logs.**  
> Ideal for incident response, threat analysis, and infosec automation.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Output Example](#output-example)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Related Resources](#related-resources)
- [License](#license)

---

## Overview

Stealer‑Log Detector is a lightweight, high-speed command-line tool that recursively scans directories for log archives (ZIP, RAR, 7z, tar/gz) commonly produced by infostealer malware such as RedLine, Raccoon, Vidar, and others.

It identifies high-value artifacts (e.g., `Passwords.txt`, browser `Cookies/`, crypto wallets), and outputs results in a JSON format suitable for SIEM ingestion. No external services, no telemetry—just efficient, signature-based detection for infosec professionals and responders.

---

## Features

- Signature‑based detection of high‑value artifacts: `Passwords.txt`, `Cookies/`, crypto `wallets/`, and more
- Supports **ZIP**, **RAR**, **7z**, and **tar.gz** formats without extracting to disk
- Severity scoring: **CONFIRMED** (≥2 high-confidence hits) vs **LIKELY**
- Fast, fully local scanning—no network requests
- JSON reporting for SIEM and automation pipelines
- MIT‑licensed, open source, and easy to extend

---

## Getting Started

### Installation

#### 1. Clone the repository:
```bash
git clone https://github.com/Joieux/stealer-log-detector.git
cd stealer-log-detector
```

#### 2. (Optional but recommended) Set up a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

#### Requirements

- Python 3.7+
- Supported platforms: Linux, Windows, macOS

---

### Usage

To scan a directory:
```bash
python stealer_log_detector.py --scan /path/to/directory
```

#### Common Options

- `--scan <path>`: Path to the directory to scan (required)
- `--output <file>`: Write JSON report to the specified file
- `--verbose`: Enable verbose output
- `--help`: Show all command-line options

For more options and help, run:
```bash
python stealer_log_detector.py --help
```

---

### Output Example

```json
{
    "status": "success",
    "summary": {
        "confirmed": 2,
        "likely": 3
    },
    "artifacts": [
        {"type": "passwords.txt", "path": "example/passwords.txt"},
        {"type": "wallet", "path": "example/crypto_wallet.dat"}
    ]
}
```
- **status**: success or error
- **summary.confirmed**: Number of CONFIRMED hits (≥2 high-confidence artifacts)
- **summary.likely**: Number of LIKELY hits (1 high-confidence artifact)
- **artifacts**: List of detected artifact types and their paths

---

## FAQ

**Q: What log file formats are supported?**  
A: ZIP, RAR, 7z, and tar.gz archives.

**Q: Can I extend detection signatures?**  
A: Yes! Edit/add artifact signatures in the codebase to support new indicators.

**Q: Does it extract files to disk?**  
A: No, archives are scanned in-memory for speed and safety.

**Q: Is this safe for production or automation?**  
A: Yes; it runs fully locally, produces machine-readable output, and does not transmit data externally.

**Q: What are the limitations?**  
A: Currently, only common stealer log formats and artifacts are supported. Detection is signature-based and may not catch all variants.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes with clear messages
4. Submit a pull request

Please ensure your code follows project style and includes tests where applicable.  
For more details, see [CONTRIBUTING.md](CONTRIBUTING.md) (if available) or open an issue with your suggestions.

---

## Related Resources

- [RedLine Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.redline)
- [Raccoon Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.raccoon)
- [Vidar Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.vidar)
- [Common SIEM Integrations](https://www.elastic.co/guide/en/siem/guide/current/index.html)

---

## License

This project is open-source under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

*Have questions or suggestions? Open an issue or start a discussion!*
```

