# Import necessary packages for using correct version of Python
from sys import version_info
py3 = version_info[0] > 2 # creates boolean value for test that Python major version > 2
VERSION = 1.0

import re

# Case-Insensitive Matching
robocop = re.compile(r'robocop', re.I)
print('Case Insensitive Search: ' + str(robocop.search('RoboCop is part man, part machine, all cop.').group()))
print('Case insensitive search: ' + str(robocop.search('ROBOCOP protects the innocent.').group()))
print('Case insensitive search: ' + str(robocop.search('Al, why does your programming book talk about robocop so much?').group()))

# Substituting Strings with sub() Method
namesRegex = re.compile(r'Agent \w+')
print('Substitution: ' + str(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print('Substitution: ' + str(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')))

# Managing Complex Regexes
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegexMultiLine = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code
	(\s|-|\.)?			# separator
	\d{3}				# first 3 digits
	(\s|-|\.)			# separator
	\d{4}				# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?	# extension
	)''', re.VERBOSE)	# Note: Use of triple-quote syntax (''') to create a multiline string so that one can spread regualar expression
				# 	over many lines, making it more legible
someRegexValue = re.compile('foo'. re.IGNORECASE | re.DOTALL)	# Use pipe '|' to do bitwise or for multiple b/c compile() only takes one additioal argument
someRegexValue2 = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)	# Three options being passed at the same time
