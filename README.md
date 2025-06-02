# Stealer‑Log Detector 🚨

[![CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Joieux/stealer-log-detector/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/Joieux/stealer-log-detector)](https://github.com/Joieux/stealer-log-detector/commits/main)

A fast, lightweight CLI tool to scan directories for credential‑stealer log archives (ZIP, RAR, 7z, tar/gz) produced by common infostealer malware such as RedLine, Raccoon, Vidar, and others.  
Stealer‑Log Detector works recursively, identifies high-value artifacts (like `Passwords.txt`, browser `Cookies/`, crypto wallets, etc.), and outputs JSON reports suitable for SIEM ingestion.  
No external services, no telemetry – just efficient, signature-based detection for infosec professionals, threat analysts, and incident responders.

---
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
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

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joieux/stealer-log-detector.git
   cd stealer-log-detector
   
2. (Optional but recommended) Set up a Python virtual environment:
   ```bash
   
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate   

3. Install the dependencies:
  ```bash
python -m pip install -r requirements.txt

---
## Usage
To scan a directory:
  ```bash
python stealer_log_detector.py --scan /path/to/directory

# Example Outut:
```JSON
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
---
# For more options and help, run:
  ```bash
python stealer_log_detector.py --help

---
### Contributing
# Contributions are welcome! To contribute:

  1. Fork the repository.
  2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name

3. Commit your changes with clear messages.
4. Submit a pull request.

# Please ensure your code follows the project's coding style and includes tests where applicable.

---
License
----
This project is licensed under the MIT License. See the LICENSE file for details.
