# Active Directory Threat Dashboard

## Overview

The **Active Directory Threat Dashboard** is an interactive tool designed to help analyze and visualize critical events logged in Active Directory environments. It allows users to gain insights into potential security threats, monitor activity, and identify anomalies.

---

## Features

- Visualize critical events by type (Event ID).
- Identify user activity patterns.
- Monitor trends in events over time.
- Analyze logs for potential security incidents or misconfigurations.

---

## Installation

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed on your machine. [Download Python](https://www.python.org/)
2. **Pip**: Ensure you have `pip`, Python's package manager, installed.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ToOKaiHack/AD-Threat-Dashboard.git
   cd AD-Threat-Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `data/` directory contains your log file (e.g., `AD_logs_complete_fictif.csv`).

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:8050
   ```

---

## File Structure

```
AD-Threat-Dashboard/
├── app.py                 # Main script for running the dashboard
├── analyze_logs.py        # Script for analyzing logs
├── data/                  # Directory for storing log files and outputs
│   ├── AD_logs.csv  # Example log file
│   ├── event_counts.csv            # Processed event data
│   ├── user_event_counts.csv       # Processed user data
│   ├── events_by_date.csv          # Temporal analysis
│   ├── event_counts.png            # Event count chart
│   ├── user_event_counts.png       # User event chart
│   ├── events_by_date.png          # Temporal trends chart
├── README.md              # Documentation of the project
├── requirements.txt       # Dependencies for the project
```

---

## Usage

### Dashboard Sections

1. **Number of Critical Events by Event ID**:
   - Displays the frequency of critical events by type (e.g., account creation, group additions).

2. **Number of Critical Events by User**:
   - Shows which users generated the most critical events.

3. **Number of Critical Events Over Time**:
   - Plots the frequency of events by date to identify spikes or unusual activity.

### Example Logs

- Event IDs analyzed:
  - **4720**: User account creation.
  - **4732**: User added to a group.
  - **4723**: Failed password change attempt.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
 ```bash
   git commit -m "Description of changes"
```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or suggestions, feel free to contact me:

- GitHub: [ToOKaiHack](https://github.com/TooKaiHack)
