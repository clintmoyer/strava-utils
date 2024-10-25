import urllib.request
import urllib.parse
import json
import os

# Retrieve the Strava API access token from the environment variable
ACCESS_TOKEN = os.getenv('STRAVA_ACCESS_TOKEN')

if not ACCESS_TOKEN:
    raise Exception("STRAVA_ACCESS_TOKEN environment variable not set")

# Constants for Strava API
STRAVA_API_URL = 'https://www.strava.com/api/v3/athlete/activities'
MAX_PER_PAGE = 200  # Maximum allowed by the Strava API

class Activity:
    def __init__(self, activity_data):
        self.id = activity_data.get('id')
        self.external_id = activity_data.get('external_id')
        self.upload_id = activity_data.get('upload_id')
        self.athlete = activity_data.get('athlete')
        self.name = activity_data.get('name')
        self.distance = activity_data.get('distance')
        self.moving_time = activity_data.get('moving_time')
        self.elapsed_time = activity_data.get('elapsed_time')
        self.total_elevation_gain = activity_data.get('total_elevation_gain')
        self.elev_high = activity_data.get('elev_high')
        self.elev_low = activity_data.get('elev_low')
        self.type = activity_data.get('type')
        self.sport_type = activity_data.get('sport_type')
        self.start_date = activity_data.get('start_date')
        self.start_date_local = activity_data.get('start_date_local')
        self.timezone = activity_data.get('timezone')
        self.start_latlng = activity_data.get('start_latlng')
        self.end_latlng = activity_data.get('end_latlng')
        self.achievement_count = activity_data.get('achievement_count')
        self.kudos_count = activity_data.get('kudos_count')
        self.comment_count = activity_data.get('comment_count')
        self.athlete_count = activity_data.get('athlete_count')
        self.photo_count = activity_data.get('photo_count')
        self.total_photo_count = activity_data.get('total_photo_count')
        self.map = activity_data.get('map')
        self.trainer = activity_data.get('trainer')
        self.commute = activity_data.get('commute')
        self.manual = activity_data.get('manual')
        self.private = activity_data.get('private')
        self.flagged = activity_data.get('flagged')
        self.workout_type = activity_data.get('workout_type')
        self.upload_id_str = activity_data.get('upload_id_str')
        self.average_speed = activity_data.get('average_speed')
        self.max_speed = activity_data.get('max_speed')
        self.has_kudoed = activity_data.get('has_kudoed')
        self.hide_from_home = activity_data.get('hide_from_home')
        self.gear_id = activity_data.get('gear_id')
        self.kilojoules = activity_data.get('kilojoules')
        self.average_watts = activity_data.get('average_watts')
        self.device_watts = activity_data.get('device_watts')
        self.max_watts = activity_data.get('max_watts')
        self.weighted_average_watts = activity_data.get('weighted_average_watts')


def get_activities(page):
    """Fetch activities from Strava API for the given page."""
    params = urllib.parse.urlencode({'per_page': MAX_PER_PAGE, 'page': page})
    url = f"{STRAVA_API_URL}?{params}"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch activities: {response.status} {response.reason}")
        data = response.read()

    return json.loads(data)


def fetch_all_activities():
    """Fetch all activities from Strava API with pagination."""
    activities = []
    page = 1
    while True:
        print(f"Fetching page {page}...")
        page_activities = get_activities(page)
        if not page_activities:
            break  # Exit loop when there are no more activities
        activities.extend(page_activities)
        page += 1
    return activities


def save_activities_to_json(activities, filename='activities.json'):
    """Save the list of activities to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(activities, file, indent=4)
    print(f"Saved {len(activities)} activities to {filename}")


def main():
    # Fetch all activities
    all_activities = fetch_all_activities()

    # Save to JSON file
    save_activities_to_json(all_activities)


if __name__ == "__main__":
    main()

