import json

def save_data(vehicles, customers):
    try:
        data = {
            "vehicles": vehicles,
            "customers": customers
        }

        with open("rental_data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    except (OSError, TypeError) as e:
        print(f"Error saving data: {e}")


def load_data():
    try:
        with open("rental_data.json", "r") as file:
            data = json.load(file)

        print("Data loaded successfully!")

        return data["vehicles"], data["customers"]

    except FileNotFoundError:
        print("No previous data found. Starting a new system!")
        return {}, {}

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"Error loading data: {e}")
        return {}, {}

    except OSError as e:
        print(f"File error: {e}")
        return {}, {}