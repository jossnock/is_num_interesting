"""
It's up to you, intrepid warrior, to glue the parts together. 
Write the function that parses the mileage number input, and returns:
    a 2 if the number is "interesting" (see below)
    a 1 if an interesting number occurs within the next two miles
    a 0 if the number is not interesting

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

- Any digit followed by all zeros: 100, 90000
- Every digit is the same number: 1111
- The digits are sequential, incementing†: 1234
- The digits are sequential, decrementing‡: 4321
- The digits are a palindrome: 1221 or 73837
- The digits match one of the values in the awesome_phrases array

† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
"""

def is_interesting(number):
    j = 0
    for i in range(3):
        number_str = str(number)
        if number_str[1:] == 0*(len(number_str)-1):
            return 2 - j

        if j == 0:
            j = 1
        number += 1
    return 0


print(is_interesting(1000000))
