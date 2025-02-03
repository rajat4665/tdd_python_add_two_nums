import re

def add(numbers: str) -> int:
    """
    function to add list of string and return an integer
    """
    # edge case handled when empty string came as input
    if not numbers:
        return 0

    # default delimiter , and \n
    delimiter = ',|\n'

    # custom delimiter case
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])  # Extract delimiter after '//'
        numbers = parts[1]

    list_of_nums = re.split(delimiter, numbers)
    result = 0
    for num in list_of_nums:
        num = int(num)
        if num > 0 and num < 1001:
            result += int(num)
        elif num < 0:
            raise ValueError(f'Negative numbers are not allowed: {num}')
    
    return result

# run the main program with some expected cases
if __name__ == '__main__':
    print(add('1,2,3,4,5'))  # output: 15
    print(add("1\n2,3"))  # output: 6
    print(add("//;\n1;2;3;9"))
    try:
        print(add("1,-2,3"))
    except ValueError as e:
        print(e)
    print(add("1001,2,3"))  # output: 5
