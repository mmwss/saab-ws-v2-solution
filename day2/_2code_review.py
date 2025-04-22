"""
Generate meaningful documentation for each function, method, and
class based on the code structure, logic, and flow.

Along with the documentation, ensure that the code is
refactored for better readability and maintainability.

Rename variables and functions to be more descriptive,
and add type hints where appropriate.

Convert camelCase to snake_case for consistency with
Python conventions.
"""

class DataProcessor:
    """
    Processes a dataset according to specific rules and thresholds.

    Attributes:
        threshold (float): The threshold value used for calculations.
        current_value (float): The current accumulated value.
        value_track (list): A list to track intermediate values.
    """

    def __init__(self, threshold: float):
        self.threshold = threshold
        self.current_value = 0
        self.value_track = []

    def process_data_part(self, dataset: dict):
        """
        Processes a part of the dataset, calculating values and updating tracking.

        Args:
            dataset (dict): A dictionary containing data to be processed.
        """
        for data_point in dataset.get('data', []):
            value = self._calculate_value(data_point['amount'], data_point['rate'])
            self.value_track.append(value)
        if len(dataset['data']) > 5:
            self._perform_extra_step()

    def _calculate_value(self, amount: float, rate: float) -> float:
        """
        Calculates a value based on amount and rate, applying a discount if amount exceeds a threshold.

        Args:
            amount (float): The amount value.
            rate (float): The rate value.

        Returns:
            float: The calculated value.
        """
        if amount > 50:
            return amount * rate * 0.85
        return amount * rate

    def _perform_extra_step(self):
        """
        Performs an additional calculation step if the sum of tracked values exceeds the threshold.
        """
        if sum(self.value_track) > self.threshold:
            self.current_value = sum(self.value_track) * 0.90

    def finalize(self) -> float:
        """
        Finalizes the processing, returning the current value if it's greater than 0,
        otherwise returning the sum of tracked values.

        Returns:
            float: The final processed value.
        """
        return self.current_value if self.current_value > 0 else sum(self.value_track)

def process_batch(batch: list, threshold: float) -> float:
    """
    Processes a batch of data using the DataProcessor class.

    Args:
        batch (list): A list of data dictionaries.
        threshold (float): The threshold value for processing.

    Returns:
        float: The final processed value.
    """
    processor = DataProcessor(threshold)
    for data_part in batch:
        processor.process_data_part(data_part)
    return processor.finalize()

def find_largest_data(data_batches: list) -> dict:
    """
    Finds the data batch with the largest total value.

    Args:
        data_batches (list): A list of data batches.

    Returns:
        dict: The data batch with the largest total value.
    """
    max_data = None
    largest_total = 0
    for batch in data_batches:
        total = 0
        for data_point in batch.get('data', []):
            total += data_point['amount'] * data_point['rate']
        if total > largest_total:
            largest_total = total
            max_data = batch
    return max_data

def find_highest_amount(data_list: list) -> float:
    """
    Finds the highest 'amount' value in a list of dictionaries.

    Args:
        data_list (list): A list of dictionaries containing 'amount' keys.

    Returns:
        float: The highest 'amount' value.
    """
    highest = 0
    for item in data_list:
        if item['amount'] > highest:
            highest = item['amount']
    return highest

def calculate_sum_with_multiplier(data: dict, multiplier: float) -> float:
    """
    Calculates the sum of values in a dictionary, applying a multiplier and a discount if the sum exceeds 1000.

    Args:
        data (dict): A dictionary containing 'info' key with a list of dictionaries having 'value' keys.
        multiplier (float): The multiplier to apply to the values.

    Returns:
        float: The calculated sum.
    """
    total = 0
    for item in data.get('info', []):
        total += item['value'] * multiplier
    if total > 1000:
        total *= 0.95
    return total

if __name__ == "__main__":
    print("Automated Documentation")

    # Sample data for testing
    sample_data = [
        {"data": [{"amount": 60, "rate": 20}, {"amount": 30, "rate": 15}]},
        {"data": [{"amount": 10, "rate": 5}, {"amount": 200, "rate": 1.5}]},
    ]

    batch_data = [
        {"data": [{"amount": 80, "rate": 12}, {"amount": 15, "rate": 10}]},
        {"data": [{"amount": 20, "rate": 25}, {"amount": 50, "rate": 7}]},
    ]

    result = process_batch(sample_data, 500)

    largest_data = find_largest_data(batch_data)

    item_list = [{"amount": 10}, {"amount": 40}, {"amount": 5}, {"amount": 100}]
    highest_amount = find_highest_amount(item_list)

    data_with_values = {"info": [{"value": 500}, {"value": 700}, {"value": 200}]}
    total_with_multiplier = calculate_sum_with_multiplier(data_with_values, 2)
