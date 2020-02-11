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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

diff_numbers = []
numbers = texts + calls

for number in numbers:
  if number[0] not in diff_numbers:
    diff_numbers.append(number[0])

  if number[1] not in diff_numbers:
    diff_numbers.append(number[1])

numbers_numbers_len = len(diff_numbers)

print('There are {} different telephone numbers in the records'.format(numbers_numbers_len))

"""

Runtime Analysis

This algorithm takes O(n) time (linear time).

In the best case, all the numbers are the same and we do only 1 insertion 
into diff_numbers array, although we still have to iterate through all 
the numbers collected in calls and texts.

In the worst case, all the numbers are different and we insert all 
the numbers into the diff_numbers array.

"""

