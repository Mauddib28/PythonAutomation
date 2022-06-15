# Import necessary packages for using correct version of Python
from sys import version_info
py3 = version_info[0] > 2 # creates boolean value for test that Python major version > 2
VERSION = 1.0

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # Note: the 'r' before the frist quote marks the string as a raw string
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# More Pattern Matching with Regex
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search('My number is 415-555-4242.')
print('Group 1: ' + mo.group(1))
print('Group 2: ' + mo.group(2))
print('Group 0: ' + mo.group(0))
print('No Group: ' + mo.group())
print('All Groups: ' + str(mo.groups()))

phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex3.search('My phone number is (451) 555-4242.')
print('Group 1: ' + mo.group(1))
print('Group 2: ' + mo.group(2))
