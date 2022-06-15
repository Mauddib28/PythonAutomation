# Import necessary packages for using correct version of Python
from sys import version_info
py3 = version_info[0] > 2 # creates boolean value for test that Python major version > 2
VERSION = 1.0

import re

xmasRegex = re.compile(r'\d+\s\w+')
print('Findall() example: ' + str(xmasRegex.findall('12 drummers, 11 pipers, 10 lord, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 patridge')))

# Making own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print('Findall() example: ' + str(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print('Findall() example: ' + str(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')))

# Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello')
print('Search check: ' + str(beginsWithHello.search('Hello world!')))
print('Search check: ' + str(beginsWithHello.search('He said hello.') == None))

endsWithNumber = re.compile(r'\d$')
print('Search check: ' + str(endsWithNumber.search('Your number is 42')))
print('Search check: ' + str(endsWithNumber.search('Your number is forty two.') == None))

wholeStringIsNum = re.compile(r'^\d+$')
print('Search check: ' + str(wholeStringIsNum.search('1234567890')))
print('Search check: ' + str(wholeStringIsNum.search('12345xyz67890') == None))
print('Search check: ' + str(wholeStringIsNum.search('12  34567890') == None))

# Wildcard character (the dot '.')
atRegex = re.compile(r'.at')
print('Findall() example: '+ str(atRegex.findall('The cat in the hat sat on the flat mat.')))

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print('Group Test: ' + mo.group(1))
print('Group Test: ' + mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
print('Group Test: ' + mo1.group())

greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print('Group Test: ' + mo2.group())

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')	# Note: the dot-star will match everything EXCEPT a newline
print('Group Test: ' + str(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUpload the law.').group()))

newlineRegex = re.compile('.*', re.DOTALL)	# Note: Inclusion of 're.DOTALL' allows for the '.' character to match all characters
print('Group Test: ' + str(newlineRegex.search('Serve the public trust.\bProtect the innocent.\nUphold the law.').group()))
# Note Bene: One can pass the 're.I' flag/variable to make the regex case-insensitive
