# sturdy-broccoli

 ## Functions Included:
 ### digit_trunc(number)
Returns the last digit of a number.

### is_num_interesting(number, interesting_numbers = {})
(See below for a definition of an interesting number)

Parameters:
    - number (int)
    - interesting_numbers (list, set, tuple, int)

Returns:
    - True if number is interesting
    - False if number isn't interesting

#### "Interesting" Numbers:
 - Any digit followed by all zeros: 100, 90000
 - Every digit is the same number: 1111
 - The digits are sequential, incementing†: 1234
 - The digits are sequential, decrementing‡: 4321
 - The digits are a palindrome: 1221 or 73837
 - The digits match one of the values in the interesting_numbers array

 † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
 ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

### random_test(interval_start = 1, interval_end = 2**64):
random_test() passes a random integer within an interval into is_num_interesting(), returning if the number was interesting or not.

Parameters:
    - interval_start (int), inclusive
    - interval_end (int), inclusive

Returns:
    - True if the random number is interesting
    - False if the random number isn't interesting

### random_test_until_true(interval_start = 1, interval_end = 2**64, max_randints_generated = 2**8):
random_test_until_true() passes a random integer within an interval into is_num_interesting() repeatedly, returning the first interesting number found.

Parameters:
    - interval_start (int), inclusive
    - interval_end (int), inclusive
    - max_randints_generated (int), reccomended to be no higher than 2**8

Returns:
    - [number, "randints generated = " + str(count)] if an interesting random number is found
    - ["no interesting number found", "randints generated = " + str(count)] False if an interesting random number isn't found