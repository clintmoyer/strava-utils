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

def filter_hiking_walking_activities_last_5_years(activities):
    """Filter activities to include only hiking and walking for the last 5 years."""
    current_year = datetime.now().year
    start_year = current_year - 5  # Start from 5 years ago

    filtered_activities = []
    for activity in activities:
        # Parse the start date and extract the year
        activity_date = datetime.fromisoformat(activity.start_date.replace('Z', '+00:00'))
        if activity.sport_type in ["Hike", "Walk"] and activity_date.year >= start_year:
            filtered_activities.append(activity)

    return filtered_activities

def calculate_yearly_mileage(activities):
    """Calculate the total mileage per year for all hiking and walking activities."""
    yearly_mileage = defaultdict(float)  # Default to 0.0 for each year

    for activity in activities:
        # Convert distance from meters to miles (1 meter = 0.000621371 miles)
        distance_miles = activity.distance * 0.000621371

        # Parse the start date and extract the year
        start_date = datetime.fromisoformat(activity.start_date.replace('Z', '+00:00'))
        year = start_date.year

        # Accumulate the mileage for the corresponding year
        yearly_mileage[year] += distance_miles

    return yearly_mileage

def plot_yearly_mileage(yearly_mileage, last_n_years=5):
    """Plot the total yearly mileage as a bar chart."""
    # Determine the current year and the range of years to include
    current_year = datetime.now().year
    years = list(range(current_year - last_n_years, current_year))

    # Extract the mileage values for each year, ensuring no missing years
    mileage_values = [yearly_mileage.get(year, 0) for year in years]

    # Plot the data as a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(years, mileage_values, color='b')

    # Set chart title and labels
    plt.title('Annual Miles (5 years)')
    plt.ylabel('Miles')
    plt.xlabel('')  # Remove x-axis label

    # Remove horizontal grid lines
    plt.grid(False, axis='y')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()

def main():
    # Load activities from JSON
    activities = load_activities()

    # Filter only hiking and walking activities from the last 5 years
    hiking_walking_activities = filter_hiking_walking_activities_last_5_years(activities)

    # Calculate total yearly mileage
    yearly_mileage = calculate_yearly_mileage(hiking_walking_activities)

    # Plot the total yearly mileage for the last 5 years
    plot_yearly_mileage(yearly_mileage)

if __name__ == "__main__":
    main()

