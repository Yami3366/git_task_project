# utils.py

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

def find_max(numbers):
    """
    Find the maximum number in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum number in the list.
    """
    return max(numbers)

def find_min(numbers):
    """
    Find the minimum number in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The minimum number in the list.
    """
    return min(numbers)
