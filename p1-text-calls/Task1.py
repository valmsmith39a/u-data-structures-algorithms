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

TASK 1 Runtime Analysis

(1) for loop: O(m)

(2) Python's in operator: O(n) (worst case), used 2 times => 2 * O(n)
https://wiki.python.org/moin/TimeComplexity

(3) Python's len function takes O(1) time
https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

(4) This algorithm takes O(m) * 2 * O(n) time, which simplifies to O(mn) time.

In the best case, all the numbers are the same and we do only 1 insertion 
into diff_numbers array, although we still have to iterate through all 
the numbers collected in calls and texts.

In the worst case, all the numbers are different and we insert all 
the numbers into the diff_numbers array.

"""

