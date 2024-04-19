"""
Write the function that parses the mileage number input, and returns:
    True if the number is "interesting" (see below)
    False if the number is not interesting

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

-- Any digit followed by all zeros: 100, 90000
-- Every digit is the same number: 1111
- The digits are sequential, incementing†: 1234
- The digits are sequential, decrementing‡: 4321
- The digits are a palindrome: 1221 or 73837
- The digits match one of the values in the awesome_phrases array

† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

- The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
"""

def is_interesting(number, interesting_numbers = []):
    if number in interesting_numbers:
        return True
    j = 0
    try:
        # Any digit followed by all zeros
        number_str = str(number)
        if number_str[1:] == ("0")*(len(number_str)-1):
            return True
        # Every digit is the same number: 1111
        if number_str == number_str[0]*len(number_str):
            return True
        
        # The digits are sequential, incementing: 1234
        

        # The digits are sequential, decrementing: 4321
        # The digits are a palindrome: 1221 or 73837
        # The digits match one of the values in the awesome_phrases array
    except:
        ValueError
    return False


assert(is_interesting(1000000) == True)
assert(is_interesting(9000000000000000) == True)
assert(is_interesting(200) == True)
assert(is_interesting("fit") == False)
assert(is_interesting(11111) == True)
assert(is_interesting(5555) == True)
assert(is_interesting(12312, [12312, 234987234, 131023.123]) == True)

number = str(123456)
a = 0
for i in number:
    a += 1
