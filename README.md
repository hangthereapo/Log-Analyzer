# 🛡️ PySentinel: Simple Cyber Security Log Parser

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Role](https://img.shields.io/badge/Role-Incident%20Response-red)](https://github.com/)

An automated Python-based utility designed for **Incident Responders** to rapidly scan server logs for specific **Indicators of Compromise (IoC)**, unauthorized access attempts, or critical system failures.

---

## 🚀 Key Features

* **🔍 Automated Scanning:** Includes pre-configured filters for `System Errors` and `Failed Login` attempts.
* **🎯 Custom Analysis:** Search for unique patterns or specific strings to track non-standard incidents.
* **📡 Case-Insensitive Engine:** Uses specialized matching logic to ensure no alerts are missed due to formatting variations.
* **📍 Precise Alerting:** Provides exact line numbers for rapid forensic investigation.

---

## 🛠️ Usage Instructions

1.  **Preparation:** Ensure you have a `server.log` file in the project's root directory.
2.  **Execution:** Run the script via terminal:
    ```bash
    python3 log_parser.py
    ```
3.  **Analysis:** Follow the interactive menu to select your scan type and review detected incidents.

---

## 📈 Roadmap & Learning Goals
Developed as part of my journey into **Cybersecurity Operations**. Future updates will include:
- [ ] **Regex Support:** For automated IP and timestamp extraction.
- [ ] **Log Rotation Handling:** Support for `.gz` and large-scale log files.
- [ ] **IBM SkillsBuild Integration:** Enhancing the logic with techniques from **IBM CyberStart 2.0**.

---
*Created by **Abdelrahman Alshoqirat** - Aspiring Cybersecurity Specialist*
