"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers_dict = {}

for call in calls:
  if call[0] in numbers_dict:
    numbers_dict[call[0]] = int(numbers_dict[call[0]]) + int(call[3])
  else:
    numbers_dict[call[0]] = int(call[3])
  
  if call[1] in numbers_dict:
    numbers_dict[call[1]] = int(numbers_dict[call[1]]) + int(call[3])
  else:
    numbers_dict[call[1]] = int(call[3])

# numbers_dict.items() => list of tuples ex. [('78130 00821', 26368), ('98453 94494', 26368)]
# x is each tuple
max_caller, max_duration = max(numbers_dict.items(), key = lambda x: x[1])

print('{} spent the longest time, {} seconds on the phone during September 2016'.format(max_caller, max_duration))

"""

TASK 2 Runtime Analysis

This algorithm takes O(n) time (linear time).

We first iterate through all the calls in the for loop and 
create a dictionary to store all unique call numbers with
each number's time accumulated over all the calls.
This will take O(n) time in best and worst cases.

We then find the max duration by using Python's max function which
takes O(n) time. 
https://stackoverflow.com/questions/5454030/how-efficient-is-pythons-max-function

The total runtime is 2 * O(n) which, after dropping constants, simplifies to O(n).

"""
