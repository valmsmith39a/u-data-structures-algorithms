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

# Method 1 
diff_numbers = []
numbers = texts + calls

for number in numbers:
  if number[0] not in diff_numbers:
    diff_numbers.append(number[0])

  if number[1] not in diff_numbers:
    diff_numbers.append(number[1])

numbers_numbers_len = len(diff_numbers)

print('There are {} different telephone numbers in the records'.format(numbers_numbers_len))