# Get user input for a list of numbers
numbers_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
numbers = [float(num) for num in numbers_str.split()]

# Check if the list is not empty
if not numbers:
    print("The list is empty.")
else:
    # Find the maximum and minimum values
    max_value = max(numbers)
    min_value = min(numbers)

    # Display the results
    print(f"The maximum value is: {max_value}")
    print(f"The minimum value is: {min_value}")