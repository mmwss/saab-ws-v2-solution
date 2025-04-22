"""
Identify and fix the error in a function that
computes the average for a list of items,
handling potential non-numeric values.
"""

def calculate_average(items):
    numeric_items = [float(item) for item in items if isinstance(item, (int, float))]
    if not numeric_items:
        return 0  
    return sum(numeric_items) / len(numeric_items)

# Example usage
if __name__ == "__main__":
    print("Code Debugging[1] Average Calculator")

    average = calculate_average([])
    print(f"Empty list average: {average}")

    average = calculate_average([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {average}")

    average = calculate_average([10, '20', 'NaN'])
    print(f"Average of [10, '20', 'NaN']: {average}")
