import re

# Define the filename or the file path
file_name = "regex_sum_1761513.txt "

# Function to extract numbers from a string using regex and compute the sum
def extract_and_compute_sum(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()

            # Use regex to find all numbers in the content
            numbers = re.findall(r"[0-9]+", content)

            # Convert the numbers from strings to integers and compute the sum
            sum_of_numbers = sum(map(int, numbers))

            return sum_of_numbers

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return 0

# Call the function and get the result
total_sum = extract_and_compute_sum(file_name)
print("Sum of numbers in the file:", total_sum)
