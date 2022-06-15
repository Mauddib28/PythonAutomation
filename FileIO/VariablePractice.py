import shelve

# Open file and save variables with the shelve module
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close

# Open file and read variables with the shelve module
shelfFile = shelve.open('mydata')
print('Type: ' + str(type(shelfFile)))
print('Variable \'cats\': ' + str(shelfFile['cats']))
shelfFile.close()

# Open file and read variables to display keys and values
shelfFile = shelve.open('mydata')
print('Keys: ' + str(list(shelfFile.keys())))
print('Values: ' + str(list(shelfFile.values())))
shelfFile.close()
