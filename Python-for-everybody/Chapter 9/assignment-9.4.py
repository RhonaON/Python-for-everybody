# open and handle filee
name = input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

# create list of emails
lst = list()
for line in handle:
    if not line.startswith('From:'): 
        continue
    line = line.split()
    lst.append(line[1])  

# creat empty dictionary
# look through the emails in the list 
# count the amount of times an email appears(this becomes a key - word = email) in the list and add this to the value
count = dict()
for word in lst:
    count[word] = count.get(word, 0) +1
# logic which calculates the 
bigcount = None
bigword =  None
# key, value in dictionary expressed as .items
for word, counts in count.items():
    if bigcount is None or counts > bigcount:
      # collect / hold counts in these variables
        bigcount = counts
        bigword = word

print(bigword, bigcount)     



