# Active Directory Threat Dashboard

## Description

The **Active Directory Threat Dashboard** is a web-based application designed to analyze and visualize critical events from Active Directory logs. It provides insights into event patterns, user activity, and potential security threats using interactive charts and tables.

## Features

- **Event Analysis by Event ID**: Visualize the number of critical events by their unique IDs, such as account creation, password changes, and group modifications.
- **User Activity Monitoring**: Identify users with the most critical activities.
- **Time-Based Trends**: Track the occurrence of critical events over time.
- **Detailed Logs by User**: View detailed logs for a specific user, including timestamps, event descriptions, and event details.

## Event ID Descriptions

The dashboard currently supports the following critical events:

| Event ID | Description                     |
|----------|---------------------------------|
| 4720     | User Account Created           |
| 4732     | Security Group Member Added    |
| 4723     | Password Change Attempt        |

## Technologies Used

- **Dash**: Web framework for building interactive dashboards.
- **Plotly**: For creating dynamic and interactive charts.
- **Pandas**: Data manipulation and analysis.
- **Flask**: Backend server for serving the application.

## Installation

### Prerequisites

1. Python 3.7 or later.
2. Required Python libraries:
   - `dash`
   - `plotly`
   - `pandas`
   - `flask`

Install dependencies with:
```bash
pip install -r requirements.txt
```

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ToOKaiHack/AD-Threat-Dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AD-Threat-Dashboard
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:8050
   ```

## Project Structure

```
AD-Threat-Dashboard/
├── app.py                 # Main application script
├── data/                  # Directory containing input data
│   └── AD_logs.csv        # Example log file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Usage

1. Upload your Active Directory logs to the `data/AD_logs.csv` file.
2. Launch the application and explore the insights through:
   - Event ID charts.
   - User activity visualizations.
   - Time-series analysis.
   - Detailed logs for individual users.

## Contributions

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **ToOKaiHack**  
  Passionate about cybersecurity and data analysis. Connect with me on [GitHub](https://github.com/ToOKaiHack).
