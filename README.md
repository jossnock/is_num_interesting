# sturdy-broccoli

## A function that takes an integer input and returns:
 - True if the number is "interesting" (see below)
 - False if the number is not interesting

## "Interesting" Numbers:
 - Any digit followed by all zeros: 100, 90000
 - Every digit is the same number: 1111
 - The digits are sequential, incementing†: 1234
 - The digits are sequential, decrementing‡: 4321
 - The digits are a palindrome: 1221 or 73837
 - The digits match one of the values in the interesting_numbers array

 † For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
 ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.