import requests
import time

# Intial greeting and race location selection
print("Welcome to the F1 Data Fetcher!")
time.sleep(1)
year = int(input("What year are you looking for(2023 or later)?: "))
if year < 2023:
    print("Please enter a year of 2023 or later.")
    exit()

print("Here are the race locations you can choose from:")
meetings_url = f"https://api.openf1.org/v1/meetings?year={year}"
response = requests.get(meetings_url)
race_locations = [meeting["location"] for meeting in response.json()]
print(race_locations)

race = input("What race are you looking for?: ").strip()
matching_location = next((loc for loc in race_locations if loc.lower() == race.lower()), None)
if not matching_location:
    print("Please enter a valid race location from the list.")
    exit()
    # URL for the OpenF1 API to fetch session data
sessions_url = "https://api.openf1.org/v1/sessions"
params = {
    "location": matching_location,
    "session_name": "Race",
    "year": year
}

response = requests.get(sessions_url, params=params)
sessions = response.json()

sessions_key = sessions[0]["session_key"]
print(f"Session Key: {sessions_key}")

# Fetching driver data based on user input
drivers_url = f"https://api.openf1.org/v1/drivers?session_key={sessions_key}"
drivers = requests.get(drivers_url).json()

# Displaying driver information
print("\nDrivers in this race:")
for d in sorted(drivers, key=lambda x: x["driver_number"]): #Lambda is a function that sorts the drivers by their driver number
    print(f" #{d['driver_number']}: {d['full_name']} ({d['team_name']})")

# 4. Prompt for driver number
driver_num_input = input("\nEnter driver number: ").strip()
if not driver_num_input.isdigit():
    print("Please enter a valid numeric driver number.")
    exit()

driver_number = int(driver_num_input)

# Fetching driver data from the OpenF1 API for specific race
driver_url = f"https://api.openf1.org/v1/drivers?driver_number={driver_number}&session_key={sessions_key}"
request = requests.get(driver_url).json()

while 
lap_url = f"https://api.openf1.org/v1/laps?driver_number={driver_number}&session_key={sessions_key}"
print(f"\nDriver: {request[0]['full_name']}")
sorted_by_lap = sorted(request, key=lambda x: x["lap_number"])
for lap in sorted_by_lap:
    print(f"Lap: {lap['lap_number']} Pos: {lap['lap_position'] } Time: {lap['lap_time']} Tyre: {lap['tyre_type']} Stint: {lap['stint_number']}")
