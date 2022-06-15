import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print('Type Test: ' + str(type(res)))
print('Ok status_code?: ' + str(res.status_code == requests.codes.ok))
print('Length of contents: ' + str(len(res.text)))
# print('Contents: ' + str(res.text[:250]))

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))
