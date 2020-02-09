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

for num in all_numbers[:50]:
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

print('The numbers called by people in Bangalore have codes:\n{}'.format(codes))
