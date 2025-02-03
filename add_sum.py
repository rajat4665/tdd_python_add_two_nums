import re

def add(numbers: str) -> int:
    """
    function to add list of string and return an integer
    """
    # edge case handled when empty string came as input
    if not numbers:
        return 0
    
    # Split using both ',' and '\n' as delimiters
    list_of_nums = re.split(r'[,\n]', numbers)
    result = 0
    for num in list_of_nums:
        result += int(num)
    
    return result


if __name__ == '__main__':
    print(add('1,2,3,4,5'))  # output: 15
    print(add("1\n2,3"))  # output: 6