import math

def digit_trunc(number):
    """Returns the last digit of a number."""
    return int(str(number)[-1])

def is_num_interesting(number, interesting_numbers = []):
    """
    Parameters:
     - number: int, 
     - interesting_numbers: list, 

    Returns:
     - True if number is interesting
     - False if number isn't interesting
    
    range(i, j) produces i, i+1, i+2, ..., j-1. 
    start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. 
    These are exactly the valid indices for a list of 4 elements. 
    step is given, it specifies the increment (or decrement).
    """
    try:
        # normalising parameters:
        int(number)
        
        if type(interesting_numbers) == type(12345) or type(interesting_numbers) == type("12345"): # if int or str
            int(interesting_numbers)
            interesting_numbers = set([interesting_numbers])
        else:
            set(interesting_numbers)
        
        number_str = str(number)

        # Any digit followed by all zeros
        if number_str[1:] == ("0") * (len(number_str) - 1):
            return True
        
        # Every digit is the same number: 1111
        if number_str == number_str[0] * len(number_str):
            return True
        
        # The digits are sequential, incementing: 1234
        is_asc = True
        prev_i = 0 # placeholder value
        for i in number_str:
            if i != number_str[0]:
                if digit_trunc(int(prev_i) + 1) != int(i):
                    is_asc = False
                    break
            prev_i = i
        if is_asc == True:
            return True
        
        # The digits are sequential, decrementing: 4321
        is_dec = True
        prev_i = 0 # placeholder value
        number_str_inverted = number_str[::-1]
        for i in number_str_inverted:
            if i != number_str_inverted[0]:
                if digit_trunc(int(prev_i) + 1) != int(i):
                    is_dec = False
                    break
            prev_i = i
        if is_dec == True:
            return True

        # The digits are a palindrome: 73837
        is_palin = True
        for i in range(math.trunc(len(number_str) / 2) + 1): # only needs to check halfway through the list (rounded up)
            if number_str[i] != number_str[-(i + 1)]:
                is_palin = False
                break
        if is_palin == True:
            return True

        # The digits match one of the values in the interesting_numbers array
        if number in interesting_numbers:
            return True
        
    except:
        ValueError

    return False


# asserts:

assert(digit_trunc(10) == 0)
assert(digit_trunc(24356) == 6)

assert(is_num_interesting(9000000000000000) == True)
assert(is_num_interesting(200) == True)

assert(is_num_interesting("quick") == False)
assert(is_num_interesting("boop oop soup") == False)

assert(is_num_interesting(11111) == True)
assert(is_num_interesting(5555) == True)

assert(is_num_interesting(12312, {12312, 234987234, 131023.123}) == True)
assert(is_num_interesting("testing", {"testing"}) == False) # only accepts ints
assert(is_num_interesting(314159, 314159) == True) # only accepts lists/arrays


assert(is_num_interesting(45678901234567) == True)
assert(is_num_interesting(89012) == True)

assert(is_num_interesting(7654) == True)
assert(is_num_interesting(21098) == True)

assert(is_num_interesting(14641) == True)
assert(is_num_interesting(1001) == True)
