import dash
from dash import html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import os

# Load logs from the CSV file
file_path = './data/AD_logs.csv'
if os.path.exists(file_path):
    logs = pd.read_csv(file_path)
else:
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Convert 'TimeCreated' column to datetime type
logs['TimeCreated'] = pd.to_datetime(logs['TimeCreated'], errors='coerce')

# Filter critical events
critical_event_ids = [4720, 4732, 4723]
critical_event_labels = {
    4720: "User Account Created",
    4732: "Security Group Member Added",
    4723: "Password Change Attempt"
}
critical_events = logs[logs['EventID'].isin(critical_event_ids)]

# Map EventID to labels
critical_events['EventDescription'] = critical_events['EventID'].map(critical_event_labels)

# Check if critical_events is empty
if critical_events.empty:
    raise ValueError("No critical events found in the provided logs.")

# Count critical events by EventID
event_counts = critical_events['EventID'].value_counts().rename_axis('EventID').reset_index(name='Counts')
event_counts['EventDescription'] = event_counts['EventID'].map(critical_event_labels)

# Count critical events by User
user_event_counts = critical_events['User'].value_counts().rename_axis('User').reset_index(name='Counts')

# Group critical events by date
critical_events['Date'] = critical_events['TimeCreated'].dt.date
events_by_date = critical_events.groupby('Date').size().reset_index(name='Counts')

# Create visualizations using Plotly
event_id_fig = px.bar(
    event_counts,
    x='EventDescription',
    y='Counts',
    color='EventID',
    title='Number of Critical Events by Event Description',
    labels={'EventDescription': 'Event Description', 'Counts': 'Number of Events'},
    color_discrete_sequence=px.colors.qualitative.Vivid
)
event_id_fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(255,255,255,1)')

user_fig = px.bar(
    user_event_counts,
    x='User',
    y='Counts',
    color='User',
    title='Number of Critical Events by User',
    labels={'User': 'User', 'Counts': 'Number of Events'},
    color_discrete_sequence=px.colors.qualitative.Pastel
)
user_fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(255,255,255,1)')

date_fig = px.line(
    events_by_date,
    x='Date',
    y='Counts',
    title='Number of Critical Events Over Time',
    labels={'Date': 'Date', 'Counts': 'Number of Events'},
    line_shape='spline',
    markers=True
)
date_fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(255,255,255,1)')

# Create the Dash app
app = dash.Dash(__name__)
app.title = "Active Directory Threat Dashboard"

# Define the app layout
app.layout = html.Div([
    html.H1("Active Directory Threat Dashboard", style={'textAlign': 'center', 'color': '#636EFA'}),
    html.Div("Analyze and visualize critical events in Active Directory logs.", style={'textAlign': 'center', 'marginBottom': '20px', 'fontSize': '18px'}),

    html.H2("Number of Critical Events by Event Description", style={'color': '#EF553B'}),
    dcc.Graph(figure=event_id_fig),

    html.H2("Number of Critical Events by User", style={'color': '#00CC96'}),
    dcc.Graph(figure=user_fig),

    html.H2("Number of Critical Events Over Time", style={'color': '#AB63FA'}),
    dcc.Graph(figure=date_fig),

    html.H2("Detailed Logs by User", style={'color': '#636EFA'}),
    dcc.Dropdown(
        id='user-dropdown',
        options=[{'label': user, 'value': user} for user in critical_events['User'].unique()],
        placeholder="Select a User",
        style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
    ),
    dash_table.DataTable(
        id='user-logs-table',
        columns=[
            {'name': 'TimeCreated', 'id': 'TimeCreated'},
            {'name': 'EventDescription', 'id': 'EventDescription'},
            {'name': 'Description', 'id': 'Description'}
        ],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '10px'},
        style_header={'fontWeight': 'bold', 'backgroundColor': '#636EFA', 'color': 'white'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#f9f9f9'
            }
        ]
    ),

    html.Footer(
        "Data sourced from Active Directory logs. Built with Dash and Plotly.",
        style={'textAlign': 'center', 'marginTop': '40px', 'fontSize': '12px', 'color': '#888'}
    )
])

# Callback to update the logs table based on selected user
@app.callback(
    Output('user-logs-table', 'data'),
    [Input('user-dropdown', 'value')]
)
def update_user_logs(selected_user):
    if selected_user:
        user_logs = critical_events[critical_events['User'] == selected_user]
        return user_logs[['TimeCreated', 'EventDescription', 'Description']].to_dict('records')
    return []

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
