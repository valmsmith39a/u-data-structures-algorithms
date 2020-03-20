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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""
Own Notes

Part A:
# Find the telephone codes called by fixed line numbers in Banglore
# Get all calls with outbound numbers from fixed lines from Bangalore
# From calls from Bangalore, get the codes from the inbound numbers
# fixed line: check for 0
# mobile: check for 7, 8, 9
# telemarketers: check for 140
# one per line
# lexicographic order (abc) with no duplicates

Steps:
# iterate through each call
# in each outbound number, look for Bangalore
# get the inbound number for the call from Bangalore
# get the code from the inbound number
"""

FIXED_BANGALORE = '080'
TELE_CODE = '140'

FIXED = ('0')
MOBILE = ('7', '8', '9')
TELE = ('140')

numbers_called_by_fixed_bangalore = []
codes = []

# Get all called-to numbers (inbound) with called-from numbers (outbound) from Bangalore
for call in calls:
  number_from = call[0]
  number_to = call[1]

  if number_from.startswith('('):
     fixed_area_code = number_from[number_from.find('(')+1: number_from.find(')')]
     
     if fixed_area_code == FIXED_BANGALORE:
       numbers_called_by_fixed_bangalore.append(number_to)

# Get the codes from the numbers called by fixed line numbers from Bangalore
for num in numbers_called_by_fixed_bangalore:
  if num.startswith('('):
    fixed_area_code = num[num.find('(')+1: num.find(')')]
    codes.append(fixed_area_code)

  elif num.startswith(MOBILE):
    mobile_code = num[: num.find(' ') - 1]
    codes.append(mobile_code)

  elif num.startswith(TELE):
    codes.append(TELE_CODE)

# remove duplicates
codes = list(set(codes))
codes.sort(key=int)

print('PART A')
print('\n')
print('The numbers called by people in Bangalore have codes:')
for code in codes:
  print(code)

"""

TASK 3A Runtime Analysis

Get the numbers called by fixed lines in Bangalore, the for loop takes O(a) time.

Get the codes from the numbers called by fixed lines in Bangalore, the for loop takes O(b) time.

Filter out duplicate numbers by using Python's set function which takes O(c) time
Construct a list by using Python's list function which takes O(d) time
https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

Runtime is:
O(a) + O(b) + O(c) + O(d)

Simplify by taking the largest number of elements (a), runtime is O(a).

"""

"""
Part B (own notes):

What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Fixed Lines also in Bangalore / Calls from fixed lines in bangalore

Objective: Find percentage of calls from Bangalore are also to Bangalore

Steps:
# Find all calls from Bangalore
# Of the calls from Bangalore, 
find the calls that are also to Bangalore
# Compute percentage
"""

BANGALORE = '(080)'
number_of_calls_from_bangalore = 0
number_of_calls_from_and_to_bangalore = 0

for call in calls:
  call_from = call[0]

  if BANGALORE in call_from:
    number_of_calls_from_bangalore += 1

    call_to = call[1]
    if BANGALORE in call_to:
      number_of_calls_from_and_to_bangalore += 1

percent_of_calls_from_bangalore_to_bangalore = round(number_of_calls_from_and_to_bangalore / number_of_calls_from_bangalore, 2) * 100 

print('\n')
print('PART B')
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent_of_calls_from_bangalore_to_bangalore))

"""

TASK 3B  Runtime Analysis

For loop takes O(n) time

"""
