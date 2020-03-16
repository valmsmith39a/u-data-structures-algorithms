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
    codes.append('140')

codes = list(set(codes))
codes.sort(key=int)

print('PART A')
print('\n')
print('The numbers called by people in Bangalore have codes:')
for code in codes:
  print(code)

"""

TASK 3A Runtime Analysis

Get all the text numbers, which takes 2 * O(a) time

Get all the call numbers, which takes 2 * O(b) time

Filter out duplicate numbers by using Python's set function which takes O(c) time
Construct a list by using Python's list function which takes O(d) time
https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

Python's startswith takes O(1) time

The for loop takes O(e) time

Python's string find function takes O(fg) time in the worst case.
We have 3 instances of find, which have runtimes of O(fg), O(fh), O(fi)
https://stackoverflow.com/questions/29728969/worst-case-time-complexity-of-str-find-in-python

Sorting the list of codes takes O(j log j) time.
https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method

Total runtime is:

2*O(a) + 2*O(b) + O(c) + O(d) + O(1) + O(e) + O(fg) + O(fh) + O(fi) + O(j log j) 

Simplified and rearranged runtime is: 
O(j log j) + O(fg) + O(fh) + O(fi) + O(a) + O(b) + O(c) + O(d) + O(e) + O(1)

"""

"""

Own Notes

Part B:

Objective: Find percentage of calls from Bangalore are also to Bangalore

Steps:
# Find all calls from Bangalore
# Of the calls from Bangalore, 
find the calls that are also to Bangalore
# Compute percentage

"""

BANGALORE = '080'
calls_from_bangalore = []
calls_from_to_bangalore = []

for call in calls:
  call_from = call[0]

  if call_from.startswith('('):
    code = call_from[call_from.find('(')+1:call_from.find(')')] 
    
    if code == BANGALORE:
      calls_from_bangalore.append(code)
      call_to = call[1]

      if call_to.startswith('('):
        code = call_to[call_to.find('(')+1:call_to.find(')')] 
        
        if code == BANGALORE:
          calls_from_to_bangalore.append(code)

  
num_calls_from_bangalore = len(calls_from_bangalore)
num_calls_from_to_bangalore = len(calls_from_to_bangalore)

percent_calls_from_to_bangalore = round(num_calls_from_to_bangalore / num_calls_from_bangalore, 2) * 100

# print('\n')
# print('PART B')
# print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent_calls_from_to_bangalore))


"""

TASK 3B  Runtime Analysis

Note: I tried using fewer variables here to simplify, but representation is not as accurate.

(1)
The for loop takes O(n) time

Python's startswith takes O(1) time

Python's find function takes O(mn) time

Python's len function takes O(1) time
https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

(2)
Worst case runtime is:

for loop: O(n)

startswith: 2 * O(1)

find: 4 * O(mn)

len: O(1)

4*O(mn) + O(n) + 3 * O(1)

which simplifies to:

O(mn) + O(n) + O(1)

and taking the longest runtime would give us:

O(mn)

"""
