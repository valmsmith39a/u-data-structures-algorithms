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
# Part A
# fixed line: check for 0
# mobile: check for 7, 8, 9
# telemarketers: check for 140
# one per line
# lexicographic order (abc) with no duplicates

FIXED = ('0')
MOBILE = ('7', '8', '9')
TELE = ('140')

all_text_numbers = [text[0] for text in texts] + [text[1] for text in texts]
all_call_numbers = [call[0] for call in calls] + [call[1] for call in calls]
all_numbers = list(set(all_text_numbers + all_call_numbers))
codes = []

for num in all_numbers:
  if num.startswith('('):
    fixed_area_code = num[num.find('(')+1: num.find(')')]
    codes.append(fixed_area_code)

  elif num.startswith(MOBILE):
    mobile_code = num[: num.find(' ')]
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

'''
Part B

Objective: Find percentage of calls from Bangalore are also to Bangalore

Steps:
* Find all calls from Bangalore
* Of the calls from Bangalore, 
find the calls that are also to Bangalore
* Compute percentage
'''

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

print('\n')
print('PART B')
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent_calls_from_to_bangalore))



    



