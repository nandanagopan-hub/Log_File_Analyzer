# Log File Analyzer Automation (Python + Pytest)

This project demonstrates an **automation framework** that:
- Reads application/server log files from command line
- Extracts and reports `ERR`, `WARN` lines
- Exports results to  **HTML**
- Sends reports via **email**
- Accepts **log file path from CLI** using pytest custom options


## 🔧 Tech Stack
- **Python 3**
- **Pytest** (for test execution & CLI)
- **Regex (re)** for log parsing
- **OpenPyXL** (Excel report generation)
- **smtplib** (Email notifications)