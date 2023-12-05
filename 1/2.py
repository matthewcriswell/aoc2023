with open("input.txt", "r") as infile:
    lines = [line.strip() for line in infile]
    
def extract_numbers(input_string):
    numbers = ['0', 'zero', '1', 'one', '2', 'two', '3', 'three', '4', 'four', 
               '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']

    result = []
    i = 0

    while i < len(input_string):
        for number in numbers:
            if input_string.rfind(number, i, i + len(number)) != -1:
                result.append(number)
        i += 1

    return result

def convert_strings(input_list):
    lookup_hash = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    output_list = []
    for item in input_list:
        if item.isnumeric():
            output_list.append(item)
        else:
            output_list.append(str(lookup_hash[item]))
    return output_list

result = 0
for line in lines:
    raw_numbers = extract_numbers(line)
    print(f'raw_numbers: {raw_numbers}')
    numbers = convert_strings(raw_numbers)
    print(f'numbers: {numbers}')
    print(f'number0: {numbers[0]} number1: {numbers[-1]}')
    result += int(numbers[0] + numbers[-1])
    print(f'result: {result}')

print(result)
