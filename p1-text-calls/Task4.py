"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""

Own Notes

Background:
# Set of possible telemarketers
# Outgoing calls but no texts
# Don't receive texts and don't receive incoming calls

Objective: 
#Find potential telemarketers

General Steps:
# Which numbers make outgoing calls but no texts
# Which numbers never receive incoming calls

Pseudocode:
# Get all outgoing call numbers
# Get all incoming call numbers
# Get all text numbers
# Of the outgoing call numbers, which numbers are not in incoming calls
# Of the outgoing call nunbers, which numbers numbers are not in texts

"""
import re

outgoing_calls = [call[0] for call in calls]
incoming_calls = [call[1] for call in calls]
all_text_numbers = [text[0] for text in texts] + [text[1] for text in texts]

outgoing_not_incoming_numbers = [outgoing_call for outgoing_call in outgoing_calls if outgoing_call not in incoming_calls]
potential_tele_numbers = [ out_not_in_num for out_not_in_num in outgoing_not_incoming_numbers if out_not_in_num not in all_text_numbers]

# remove duplicates
potential_tele_numbers = list(set(potential_tele_numbers))
# remove parentheses and whitespaces
potential_tele_numbers = [re.sub(r"[\s()]", '', num) for num in potential_tele_numbers]
# sort in lexicographic order
potential_tele_numbers.sort(key=int)

print('These numbers could be telemarketers:')
for num in potential_tele_numbers:
  print(num)


"""

TASK 4 Runtime Analysis

outgoing calls list comprehension: O(a)
incoming calls list comprehension: O(a)
all text numbers: O(b) + O(b) = 2*O(b) => O(b)

outgoing not incoming: 
- for loop: O(c)
- Python's `in` operator: O(d)
- `in` operator run on each item in for loop, so runtime is: O(cd)

potential telemarketers:
- for loop: O(e)
- Python's `in` operator: O(f)
- `in` operator run on each item in for loop, so runtime is: O(ef)

O(a) + O(a) + O(b) + O(b) + O(cd) + O(ef) =>

2*O(a) + 2*O(b) + O(cd) + O(ef) => 

O(a) + O(b) + O(cd) + O(ef)

"""
  