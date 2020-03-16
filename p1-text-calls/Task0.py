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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_text_in_num = texts[0][0]
first_text_ans_num = texts[0][1]
first_text_time = texts[0][2]

last_call_in_num = calls[len(calls) - 1][0]
last_call_ans_num = calls[len(calls) - 1][1]
last_call_time = calls[len(calls) - 1][2]
last_call_duration = calls[len(calls) - 1][3]

print('First record of texts, {} texts {} at time {}'.format(first_text_in_num, first_text_ans_num, first_text_time))
print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(last_call_in_num, last_call_ans_num, last_call_time, last_call_duration))

"""

TASK 0 Runtime Analysis

This set of operations will take O(1) time (constant time).

The runtime is the same for small or large n because we are always
getting data from the first and last elements.

"""
