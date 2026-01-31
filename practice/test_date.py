import datetime

date_str = "2026-01-22"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
day_of_week_full = date_obj.strftime("%A")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_order = []

start = days.index(day_of_week_full)

for i in range(7):
    index = (days.index(day_of_week_full) + i)
    day = days[index % 7][:3].upper()
    days_order.append(day)

print(days_order)


from rich.console import Console
from rich.table import Table

# 1. Mock Data (Replace this with your actual 'events' list and Wrapper)
events = [
    {
        "summary": "Team Meeting", 
        "description": "Weekly sync", 
        "start": {"date": "2023-10-27", "dateTime": "2023-10-27T10:00:00"}, 
        "end": {"date": "2023-10-27", "dateTime": "2023-10-27T11:00:00"}
    },
    {
        "summary": "Lunch with Client", 
        "description": "Discuss project roadmap", 
        "start": {"date": "2023-10-28", "dateTime": "2023-10-28T13:00:00"}, 
        "end": {"date": "2023-10-28", "dateTime": "2023-10-28T14:30:00"}
    }
]

# Initialize Console and Table
console = Console()
table = Table(title="Upcoming Events", show_header=True, header_style="bold magenta")

# 2. Add Columns (These are the headers)
table.add_column("Date", style="cyan", no_wrap=True)
table.add_column("Summary", style="green")
table.add_column("Description", style="white")
table.add_column("Duration", justify="right", style="yellow")

# 3. Loop through events and add Rows (This is the data)
for event in events:
    # Safe extraction using .get() to avoid crashes if keys are missing
    summary = event.get("summary", "No Title")
    description = event.get("description", "")
    
    # Handle Start/End times
    start = event.get("start", {})
    end = event.get("end", {})
    
    # Prefer dateTime (for precise events) over date (for all-day events)
    start_str = start.get("dateTime", start.get("date", "N/A"))
    end_str = end.get("dateTime", end.get("date", "N/A"))
    
    # Simple formatting to just show the date/time part you likely want
    # (You can customize this parsing further with datetime objects)
    display_date = start_str.split('T')[0] 
    
    # Add the row to the table
    table.add_row(
        display_date,
        summary,
        description,
        f"{start_str.split('T')[-1]} - {end_str.split('T')[-1]}" # Slicing to show just time
    )

# 4. Print
console.print(table)