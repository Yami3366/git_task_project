# main.py

def helper_function(data):
    """
    A helper function to process data.

    Args:
        data (list): A list of data to be processed.

    Returns:
        list: The processed data.
    """
    processed_data = []

    for item in data:
        # Perform some processing on each item
        processed_item = item * 2
        processed_data.append(processed_item)

    return processed_data

def main():
    # Example usage of the helper function
    data = [1, 2, 3, 4, 5]
    processed_data = helper_function(data)
    print("Processed Data:", processed_data)

if __name__ == "__main__":
    main()
