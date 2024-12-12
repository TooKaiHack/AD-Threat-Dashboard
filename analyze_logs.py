import pandas as pd
import matplotlib.pyplot as plt

# Load logs from the CSV file
logs = pd.read_csv('./data/AD_logs.csv')

# Display the first 5 rows to verify data loading
print("Preview of the data:")
print(logs.head())

# Convert 'TimeCreated' column to datetime type
logs['TimeCreated'] = pd.to_datetime(logs['TimeCreated'])

# Sort logs by date and time
logs = logs.sort_values('TimeCreated')

# Filter critical events (IDs 4720, 4732, 4723)
critical_event_ids = [4720, 4732, 4723]
critical_events = logs[logs['EventID'].isin(critical_event_ids)]

# Count the number of critical events by event ID
event_counts = critical_events['EventID'].value_counts().rename_axis('EventID').reset_index(name='Counts')
print("\nNumber of critical events by event ID:")
print(event_counts)

# Count the number of critical events by user
user_event_counts = critical_events['User'].value_counts().rename_axis('User').reset_index(name='Counts')
print("\nNumber of critical events by user:")
print(user_event_counts)

# Visualize the number of critical events by event ID
plt.figure(figsize=(8, 6))
plt.bar(event_counts['EventID'].astype(str), event_counts['Counts'], color='skyblue')
plt.title('Number of Critical Events by Event ID')
plt.xlabel('Event ID')
plt.ylabel('Number of Occurrences')
plt.savefig('./data/event_counts.png')
plt.show()

# Visualize the number of critical events by user
plt.figure(figsize=(8, 6))
plt.bar(user_event_counts['User'], user_event_counts['Counts'], color='orange')
plt.title('Number of Critical Events by User')
plt.xlabel('User')
plt.ylabel('Number of Occurrences')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./data/user_event_counts.png')
plt.show()

# Temporal analysis of critical events
# Group events by date
critical_events['Date'] = critical_events['TimeCreated'].dt.date
events_by_date = critical_events.groupby('Date').size().reset_index(name='Counts')

# Visualize the number of critical events by date
plt.figure(figsize=(10, 6))
plt.plot(events_by_date['Date'], events_by_date['Counts'], marker='o', linestyle='-')
plt.title('Number of Critical Events by Date')
plt.xlabel('Date')
plt.ylabel('Number of Occurrences')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./data/events_by_date.png')
plt.show()

# Save analysis results to CSV files
event_counts.to_csv('./data/event_counts.csv', index=False)
user_event_counts.to_csv('./data/user_event_counts.csv', index=False)
events_by_date.to_csv('./data/events_by_date.csv', index=False)

print("\nAnalysis completed. Charts and results have been saved in the 'data' folder.")
