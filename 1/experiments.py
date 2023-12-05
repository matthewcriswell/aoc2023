def extract_numbers(input_string):
    # List of all number representations
    numbers = ['0', 'zero', '1', 'one', '2', 'two', '3', 'three', '4', 'four', 
               '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']

    input_string = input_string.lower()  # Convert to lowercase
    result = []
    i = 0

    while i < len(input_string):
        for number in numbers:
            if input_string.rfind(number, i, i + len(number)) != -1:
                result.append(number)
        i += 1

    return result

# Example usage
string = "eighthree83asdf9knonetwo3"
print(extract_numbers(string))

