import math
import random

def digit_trunc(number):
    """Returns the last digit of a number."""
    return int(str(number)[-1])

def is_num_interesting(number, interesting_numbers = {}):
    """
    (See README.md for a definition of an interesting number)
    Parameters:
     - number (int)
     - interesting_numbers (list, set, tuple, int)

    Returns:
     - True if number is interesting
     - False if number isn't interesting
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

def random_test(interval_start = 1, interval_end = 2**64):
    """
    random_test() passes a random integer within an interval into is_num_interesting(), returning if the number was interesting or not.\n

    Parameters:
     - interval_start (int), inclusive
     - interval_end (int), inclusive

    Returns:
     - True if the random number is interesting
     - False if the random number isn't interesting
    """
    
    if is_num_interesting(random.randint(interval_start, interval_end)):
        return True
    return False

def random_test_until_true(interval_start = 1, interval_end = 2**64, max_randints_generated = 2**8):
    """
    random_test_until_true() passes a random integer within an interval into is_num_interesting() repeatedly, returning the first interesting number found.\n
    
    Parameters:
     - interval_start (int), inclusive
     - interval_end (int), inclusive
     - max_randints_generated (int), reccomended to be no higher than 2**8

    Returns:
     - [number, "randints generated = " + str(count)] if an interesting random number is found
     - ["no interesting number found", "randints generated = " + str(count)] False if an interesting random number isn't found
    """
    
    interesting_int_found = False
    count = 1
    while count <= max_randints_generated and interesting_int_found == False:
        number = random.randint(interval_start, interval_end)
        if is_num_interesting(number) == True:
            return [number, "randints generated = " + str(count)]
        count += 1
    return ["no interesting number found", "randints generated = " + str(count - 1)] # (count - 1) b/c the final count += 1 at the end of the while loop overestimates the count by 1


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
