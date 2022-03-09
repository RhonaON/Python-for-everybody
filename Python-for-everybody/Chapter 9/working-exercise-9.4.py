fname = input('Enter file: ')
# below line is a check so that a default file opens regardless of what is entered in input
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

# cant use dict as a variable name
di = dict()
for line in handle:
    line = line.rstrip()
 #   print(line)
    words = line.split()
 #   print(words)
    for word in words:
     #   print(word)
     # below line of code means get returns a defualt value of -99 when the word is not found in the dictionary
     # .get allows us to get a value out if it is there and default if it isn't
      #  print('**', word, di.get(word, -99))
      # if key is not there the count is zero
        oldcount = di.get(word, 0)
        newcount = oldcount + 1
        di[word] = newcount
       # print(word, 'new', oldcount)
     #   if word in di :
      #      di[word] = di[word] + 1
       #     print('**Existing**')
        #else:
         # di[word] = 1
          #print('**New**') 
      #  print(word, di[word])

      # the below line is an idiom: retrieve/create/update
        di[word] = di.get(word,0) + 1
      #  print(word, 'new', newcount)

# now we can print the dictionary and verify it is correct      
# print(di)

#now we want to find the most common word (like a maximum loop)

largest = -1
for key,value in di.items() :
    if value > largest :
        largest = value
        theword = key #capture or remember the word which is the largest

print(theword, largest)
