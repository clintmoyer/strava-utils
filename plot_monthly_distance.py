import json
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# Same Activity class as before
class Activity:
    def __init__(self, activity_data):
        self.id = activity_data.get('id')
        self.external_id = activity_data.get('external_id')
        self.upload_id = activity_data.get('upload_id')
        self.athlete = activity_data.get('athlete')
        self.name = activity_data.get('name')
        self.distance = activity_data.get('distance')  # distance in meters
        self.moving_time = activity_data.get('moving_time')
        self.elapsed_time = activity_data.get('elapsed_time')
        self.total_elevation_gain = activity_data.get('total_elevation_gain')
        self.elev_high = activity_data.get('elev_high')
        self.elev_low = activity_data.get('elev_low')
        self.type = activity_data.get('type')
        self.sport_type = activity_data.get('sport_type')  # sport type
        self.start_date = activity_data.get('start_date')  # in ISO format

def load_activities(filename='activities.json'):
    """Load activities from the JSON file and return a list of Activity objects."""
    with open(filename, 'r') as file:
        data = json.load(file)
    activities = [Activity(activity_data) for activity_data in data]
    return activities

def filter_hiking_walking_activities(activities, target_year=None):
    """Filter activities to include only hiking and walking for the previous year based on sport_type."""
    if target_year is None:
        target_year = datetime.now().year - 1  # Use the full previous year

    filtered_activities = []
    for activity in activities:
        # Parse the start date and extract the year
        activity_date = datetime.fromisoformat(activity.start_date.replace('Z', '+00:00'))
        if activity.sport_type in ["Hike", "Walk"] and activity_date.year == target_year:
            filtered_activities.append(activity)

    return filtered_activities

def calculate_monthly_mileage(activities):
    """Calculate the total monthly mileage for all hiking and walking activities."""
    monthly_mileage = defaultdict(float)  # Default to 0.0 for each month

    for activity in activities:
        # Convert distance from meters to miles (1 meter = 0.000621371 miles)
        distance_miles = activity.distance * 0.000621371

        # Parse the start date and extract the year and month
        start_date = datetime.fromisoformat(activity.start_date.replace('Z', '+00:00'))
        year_month = start_date.strftime('%Y-%m')  # Format as YYYY-MM

        # Accumulate the mileage for the corresponding month
        monthly_mileage[year_month] += distance_miles

    return monthly_mileage

def plot_monthly_mileage(monthly_mileage, target_year):
    """Plot the total monthly mileage as a line chart."""
    # Sort the monthly data by date
    sorted_months = sorted(monthly_mileage.keys())

    # Extract the corresponding mileage values
    mileage_values = [monthly_mileage[month] for month in sorted_months]

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_months, mileage_values, marker='o', linestyle='-', color='b')

    # Format months as full month name (e.g., "January")
    month_labels = [datetime.strptime(month, '%Y-%m').strftime('%B') for month in sorted_months]

    # Update the x-axis labels to show full month names, no days
    plt.xticks(ticks=range(len(sorted_months)), labels=month_labels, rotation=45)

    # Update chart title with the specific year
    plt.title(f'Hiking Mileage {target_year}')

    # Update y-axis label to "Miles" and remove x-axis label
    plt.ylabel('Miles')
    plt.xlabel('')  # No x-axis label

    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

def main():
    # Load activities from JSON
    activities = load_activities()

    # Filter only hiking and walking activities from the previous year
    previous_year = datetime.now().year - 1
    hiking_walking_activities = filter_hiking_walking_activities(activities, target_year=previous_year)

    # Calculate total monthly mileage
    monthly_mileage = calculate_monthly_mileage(hiking_walking_activities)

    # Plot the total monthly mileage
    plot_monthly_mileage(monthly_mileage, target_year=previous_year)

if __name__ == "__main__":
    main()

