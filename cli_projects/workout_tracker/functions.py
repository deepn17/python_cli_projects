import json
import datetime
import os

FILENAME = "cardio_log.json"

def load_data():
    """Loads existing data from the JSON file. Returns an empty dict if file doesn't exist."""
    if not os.path.exists(FILENAME):
        return {}

    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except(json.JSONDecodeError, IOError):
        # Return empty dict if file is corrupted or empty
        return {}


def save_data(data):
    """Writes the dictionary to the JSON file with indentation."""
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"[Success] Data saved to {FILENAME} ")

def add_workout(data):
    """Prompts user for details and adds them to the data dictionary."""
    print("\n--- Add New Workout ---")

    # 1. Get the date
    date_input = input("Enter Date (YYYY-MM-DD) or press enter for today: ").strip()
    if not date_input:
        date_input = datetime.datetime.now().strftime("%Y-%m-%d")

    # 2. Get workout details
    activity = input("Activity Type (e.g., Run, Swim, Walk, Cycle): ").capitalize().strip()

    # 3. Getting inputs from the user for the activity
    while True:
        try:
            duration = int(input("Duration (minutes): "))
            break
        except ValueError:
            print("Please enter a valid number for minutes.")

    while True:
        try:
            distance = float(input("Distance (km): "))
            break
        except ValueError:
            print("Please enter a valid number for distance.")

    while True:
        try:
            speed = float(input("Speed (kmph): "))
            break
        except ValueError:
            print("Please enter a valid number for speed.")

    while True:
        try:
            calories = int(input("Calories burned: "))
            break
        except ValueError:
            print("Please enter a valid number for calories.")

    notes = input("Notes (optional): ").strip()
    if not notes:
        notes = ""

    # 4. Construct the workout dictionary
    timestamp = datetime.datetime.now().isoformat()
    workout_entry = {
        "activity": activity,
        "duration": duration,
        "distance": distance,
        "speed": speed,
        "calories burned": calories,
        "notes": notes,
        "timestamp": timestamp # Tracks exactly when you entered it
    }

    # 5. Update the main data dictionary (Nested Logic)
    if date_input in data:
        next_num = len(data[date_input]) + 1
        workout_id = f"workout_{next_num}"
        data[date_input][workout_id] = workout_entry

    else:
        # if the date does not exist, create a new list
        data[date_input] = {"workout_1": workout_entry}
    save_data(data)

def view_history(data):
    """Prints the workout history in a readable format."""
    print("\n--- Workout History ---")
    if not data:
        print("No logs found.")
        return

    # Loop through dates
    for date, workouts in data.items():
        print(f"\nDate: {date}")
        # Loop through the list of workouts for that date
        for workout_id, workout in workouts.items():
            print(f" {workout_id}. {workout['activity']} | {workout['duration']} mins | "
                  f"{workout['distance']} kms")
