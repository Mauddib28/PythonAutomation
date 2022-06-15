# Import necessary packages for using correct version of Python
from sys import version_info
py3 = version_info[0] > 2 # creates boolean value for test that Python major version > 2
VERSION = 1.0

import re

# Matching Multiple Groups Using Pipes
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print('Group Test: ' + mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print('Group Test: ' + mo2.group())

# Optional Matching with Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print('Group Test: ' + mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print('Group Test: ' + mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print('Group Test: ' + mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print('Group Test: ' + mo2.group())

# Matching Zero or More with Star
batRegex2 = re.compile(r'Bat(wo)*man')
mo1 = batRegex2.search('The Adventures of Batman')
print('Group Test: ' + mo1.group())

mo2 = batRegex2.search('The Adventures of Batwoman')
print('Group Test: ' + mo2.group())

mo3 = batRegex2.search('The Adventures of Batwowowowoman')
print('Group Test: ' + mo3.group())

# Matching One or More with Plus
batRegex3 = re.compile(r'Bat(wo)+man')
mo1 = batRegex3.search('The Adventures of Batwoman')
print('Group  Test: ' + mo1.group())

mo2 = batRegex3.search('The Adventures of Batwowowowoman')
print('Group Test: ' + mo2.group())

mo3 = batRegex3.search('The Adventures of Batman')
print('Match Test: ' + str(mo3 == None))

# Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print('Group Test: ' + mo1.group())

mo2 = haRegex.search('Ha')
print('Group Test: ' + str(mo2 == None))

# Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print('Group Test: ' + mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print('Group Test: ' +  mo2.group())

# Using the findall() Method
phoneNumRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex2.search('Cell: 415-555-9999 Work: 212-555-0000')
print('Group Test: ' + mo.group())

phoneNumRegex3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')	# Has no groups
print('Findall() Test: ' + str(phoneNumRegex3.findall('Cell: 415-555-9999 Work: 212-555-0000')))

phoneNumRegex4 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')	# Has groups
print('Finall() Test with groups: ' + str(phoneNumRegex4.findall('Cell: 415-555-9999 Work: 212-555-0000')))
