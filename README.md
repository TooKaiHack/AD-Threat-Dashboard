# Active Directory Threat Dashboard

![active-directory-monitoring-and-analysis-real](https://github.com/user-attachments/assets/79aa8059-bb1e-4196-a9e6-d523374d9737)

## Description

The **Active Directory Threat Dashboard** is a web-based application designed to analyze and visualize critical events from Active Directory logs. This project demonstrates how to identify and monitor sensitive actions within an Active Directory environment, such as user account creation, password changes, and group membership modifications. It is intended as an educational tool for labs and exercises in cybersecurity.

---

## Features

- **Event Analysis by Event ID**: Visualize the number of critical events by their unique IDs, including detailed descriptions.
- **User Activity Monitoring**: Identify users involved in critical actions.
- **Time-Based Trends**: Track the occurrence of critical events over time.
- **Detailed Logs by User**: Explore logs associated with specific users, including timestamps, event descriptions, and details.

---

## Technologies Used

- **Dash**: For building the interactive web dashboard.
- **Plotly**: For creating dynamic, visually appealing charts.
- **Pandas**: For data manipulation and analysis.
- **Flask**: Backend server for serving the application.
- **PowerShell**: To extract critical Active Directory logs.

---

## Prerequisites

1. Python 3.7 or later installed on your system.
2. Active Directory environment or sample log files for testing.

### Required Python Libraries

Install dependencies with:
```bash
pip install -r requirements.txt
```

### Sample Requirements File (`requirements.txt`):
```
dash==2.11.1
plotly==5.15.0
pandas==2.1.1
flask==2.3.4
```

---

## Project Structure

```
AD-Threat-Dashboard/
├── app.py                 # Main application script
├── analyze_logs.py        # Script for processing and analyzing log data
├── data/                  # Directory containing input data
│   └── AD_logs.csv        # Example Active Directory log file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
└── LICENSE                # License file
```

---

## Event ID Descriptions

| Event ID | Description                     |
|----------|---------------------------------|
| 4720     | User Account Created           |
| 4732     | Security Group Member Added    |
| 4723     | Password Change Attempt        |

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/ToOKaiHack/AD-Threat-Dashboard.git
cd AD-Threat-Dashboard
```

### Run the Application
```bash
python app.py
```

### Open the Dashboard
Visit the following URL in your web browser:
```
http://127.0.0.1:8050
```

---

## Application Overview

### **Key Features:**
- **Event Breakdown by Type**: Analyze critical events such as user account creation, password changes, and group modifications.
- **User-Based Analysis**: Identify users performing sensitive actions.
- **Time-Series Trends**: Monitor activity over specific time periods.

## How It Works

1. **Log Extraction**:
   - Use PowerShell scripts to extract Active Directory event logs.
   - Filter and export critical events (e.g., 4720, 4732, 4723) to a CSV file.

2. **Data Analysis**:
   - Load the log data into Python using Pandas.
   - Group and aggregate the data by Event ID, User, and Date for visualization.

3. **Dashboard Creation**:
   - Use Dash and Plotly to build interactive visualizations for:
     - Event counts by type.
     - User activity monitoring.
     - Temporal trends.

4. **Future Enhancements**:
   - Integrate real-time monitoring with Elasticsearch or Splunk.
   - Expand to hybrid environments with Azure AD support.

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests. Your ideas and improvements are highly appreciated.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **GitHub Repository**: [AD Threat Dashboard](https://github.com/ToOKaiHack/AD-Threat-Dashboard)
- **Author**: [ToOKaiHack](https://github.com/ToOKaiHack)

---

## 💡 Feedback

If you test this project, your feedback is invaluable! Let me know what works well and what could be improved to make this dashboard even more useful. 🚀

---
