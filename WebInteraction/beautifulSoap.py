import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
print('Type: ' + str(type(noStarchSoup)))

# Examine a local example file
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print('Type: ' + str(type(exampleSoup)))

elems = exampleSoup.select('#author')
print('Type of elems: ' + str(type(elems)))
print('Length: ' + str(len(elems)))
print('Element 0 type: ' + str(type(elems[0])))
print('Contents: ' + elems[0].getText())
print('Full Text: ' + str(elems[0]))
print('Attributes: ' + str(elems[0].attrs))

pElems = exampleSoup.select('p')
print('pElem element 0: ' + str(pElems[0]))
print('Element 0 get text: ' + str(pElems[0].getText()))
print('pElem element 1: ' + str(pElems[1]))
print('Element 1 get text: ' + str(pElems[1].getText()))
print('pElem element 2: ' + str(pElems[2]))
print('Element 2 get text: ' + str(pElems[2].getText()))

# Getting data from an element's attributes
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
print('String: ' + str(spanElem))
print('ID: ' + str(spanElem.get('id')))
print('Attribute check: ' + str(spanElem.get('some_nonexistent_addr') == None))
print('Attributes: ' + str(spanElem.attrs))
