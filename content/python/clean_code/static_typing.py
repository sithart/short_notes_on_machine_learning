# Create two variables to use as inputs to the function
fruit = 'Apple'
pieces = 'twelve'

# Create a function called describe_fruit that has two parameters,
# fruit_type that should be a string and fruit_number which should be an integer.
# The output of the function should be a string.
def describe_fruit(fruit_type: str, fruit_number: int) -> str:
    
    # Create output from the inputs
    description = "We have " + str(fruit_number) + " pieces of " + fruit_type 
    
    # Return the output
    return description

# Run function with inputs
describe_fruit(fruit, pieces)