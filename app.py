import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load logs from the CSV file
logs = pd.read_csv('./data/AD_logs.csv')

# Convert 'TimeCreated' column to datetime type
logs['TimeCreated'] = pd.to_datetime(logs['TimeCreated'])

# Filter critical events
critical_event_ids = [4720, 4732, 4723]
critical_events = logs[logs['EventID'].isin(critical_event_ids)]

# Count critical events by EventID
event_counts = critical_events['EventID'].value_counts().rename_axis('EventID').reset_index(name='Counts')

# Count critical events by User
user_event_counts = critical_events['User'].value_counts().rename_axis('User').reset_index(name='Counts')

# Group critical events by date
critical_events['Date'] = critical_events['TimeCreated'].dt.date
events_by_date = critical_events.groupby('Date').size().reset_index(name='Counts')

# Create visualizations using Plotly
event_id_fig = px.bar(
    event_counts,
    x='EventID',
    y='Counts',
    color='EventID',
    title='Number of Critical Events by Event ID',
    labels={'EventID': 'Event ID', 'Counts': 'Number of Events'}
)

user_fig = px.bar(
    user_event_counts,
    x='User',
    y='Counts',
    color='User',
    title='Number of Critical Events by User',
    labels={'User': 'User', 'Counts': 'Number of Events'}
)

date_fig = px.line(
    events_by_date,
    x='Date',
    y='Counts',
    title='Number of Critical Events Over Time',
    labels={'Date': 'Date', 'Counts': 'Number of Events'}
)

# Create the Dash app
app = dash.Dash(__name__)
app.title = "Active Directory Threat Dashboard"

# Define the app layout
app.layout = html.Div([
    html.H1("Active Directory Threat Dashboard", style={'textAlign': 'center'}),
    html.Div("Analyze and visualize critical events in Active Directory logs.", style={'textAlign': 'center'}),

    html.H2("Number of Critical Events by Event ID"),
    dcc.Graph(figure=event_id_fig),

    html.H2("Number of Critical Events by User"),
    dcc.Graph(figure=user_fig),

    html.H2("Number of Critical Events Over Time"),
    dcc.Graph(figure=date_fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
