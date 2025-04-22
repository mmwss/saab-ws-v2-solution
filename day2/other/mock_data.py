import random
from datetime import datetime, timedelta

EXAMPLE_1 = """
Generate a dataset of user profiles for a social media platform.
Each user profile should have the following attributes:

    User ID (unique identifier).
    Name (first and last name).
    Username (alphanumeric, unique).
    Email address (unique).
    Bio (a short biography, up to 150 characters).
    Join Date (a random date in the past two years).
    Followers count (a random number between 0 and 5000).
    Following count (a random number between 0 and 3000).

Use AI to write a script that will generate this dataset for you.
"""

def generate_user_profiles(n=100):
    users = []
    for i in range(n):
        # Use AI code generation here
        pass  # Remove this pass statement after completing the code

    return users

EXAMPLE_2 = """
Generate mock data for e-commerce transactions.
Each transaction should contain:

    Transaction ID (unique identifier).
    User ID (links to a user).
    Product name (e.g., "Smartphone", "Laptop", etc.).
    Quantity (a number between 1 and 10).
    Price per unit (a decimal number between 10.00 and 2000.00).
    Total price (calculated as quantity * price per unit).
    Transaction Date (a random date in the past year).
    Shipping address (e.g., "123 Main St, New York, NY").

Use AI to generate the data itself and validate the correctness and diversity of the generated data.
"""

def generate_transactions(n=100):
    # Use AI code generation here
    pass  # Remove this pass statement after completing the code

EXAMPLE_3 = """
Generate mock data for sensor readings from Internet of Things (IoT) devices.
Each sensor reading should include:

    Device ID (unique identifier for the device).
    Timestamp (date and time of the reading).
    Temperature (a float between -10.0 and 40.0 degrees Celsius).
    Humidity (a percentage between 0 and 100%).
    Battery level (a percentage between 0 and 100%).
    Status ("online" or "offline").

Use AI to generate the data and ensure that the values fall within the specified ranges.
"""

def generate_sensor_readings(n=100):
    # Use AI code generation here
    pass  # Remove this pass statement after completing the code


if __name__ == "__main__":
    print("Mock Data")

    print("Profiles")
    for profile in generate_user_profiles(2):
        print(profile)

    print("Transactions")
    for transaction in generate_transactions(2):
        print(transaction)

    print("Sensor Readings")
    for reading in generate_sensor_readings(2):
        print(reading)
