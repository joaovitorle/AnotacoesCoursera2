#1
print('='*15,'#1','='*15)

eng2pt = {} # We just created an empty dictionary 

eng2pt['one'] = 'um' #'one' is the key and 'um' is the value. The key is like the main word, in a real dictionarie, and the value is the description of the dictionary.
eng2pt['two'] = 'dois'
eng2pt['three'] = 'três'

print(eng2pt)


#2
print('='*15,'#2','='*15)
eng2pt = {'three': 'três', 'two': 'dois', 'one': 'um'} # We just created an empty dictionary 

value = eng2pt['two']
print(value)

print(eng2pt['one'])


#3 number in the dictionary
print('='*15,'#3','='*15)
olympics = {'gold': 7, 'silver': 10, 'bronze': 20}
print(olympics)


#4 Dictionary operations
print('='*15,'#4','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del inventory ['pears'] #Delete from the inventory the key called pears 

print(inventory)


#5 How to change the value number
print('='*15,'#5','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory ['pears'] = 0 #Change the value number 

print(inventory)

#6 Somar um value 
print('='*15,'#6','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory ['bananas'] = inventory ['bananas'] + 200
numItens = len(inventory)

print (inventory)
print (numItens)
print (inventory['bananas'])


#7 Dictionary Methods
print('='*15,'#7','='*15) 
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for key in inventory.keys():
    print(key,'has the value', inventory[key])

for key in inventory:
    print ('Got key', key)

    
#8 Turn into a list 
print('='*15,'#8','='*15)
keys = list(inventory.keys())
print(keys)


#9
print('='*15,'#9','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print (list(inventory.values()))
print (list(inventory.items()))

for key in inventory:
    print('Got', key, "that maps to", inventory[key])


#10
print('='*15,'#10','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory) #in retorna True or false se tiver aquela palavra dentro do inventorio
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print('We have no bananas')


#11 Using get
print('='*15,'#11','='*15)
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get('apples')) #get the value of the key directly
print(inventory.get('cherries'))
print(inventory.get('cherries',0)) #equal to the code above, ao inves de o resultado ser "None" is "0"



#12 Aliasing and copying 
print('='*15,'#12','='*15)
opposites = {'up' : 'down', 'right': 'wrong', 'true' : 'false'}
alias = opposites

print (alias is opposites)

alias ['right'] = 'left'
print(opposites['right'])



#12 Accumulating in dictionary
print('='*15,'#12','='*15)

f = open('olympics.txt', 'r')
txt = f.read() #now the txt is one long string containing all the characters 
x = {} #starts with an empty dictionary
x['t'] = 0 #initializer the t counter 
x['s'] = 0 #initialize the s counter
for c in txt: 
    if c == 't':
        x['t'] = x['t'] +1 #increment the t counter 
    elif c == 's':
        x['s'] = x['s'] +1 #increment the s counter
print('t: ' + str(x['t']) + ' occurences ')
print('s:' + str(x['s']) + ' occurences')


#13 Accumulating in dictionary 
print('='*15,'#13','='*15)
f = open('olympics.txt', 'r')
txt = f.read() #now the txt is one long string containing all the characters 
x = {}
for c in txt:
    if c not in x: #we have not seen this characters before, so initialize a counter for it
        x[c] = 0 
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1
print('t: ' + str(x['t']) + ' occurences ') #Now i can find all the occurences, just print it out
print('s:' + str(x['s']) + ' occurences')
print('t: ' + str(x['a']) + ' occurences ')
print('s:' + str(x['b']) + ' occurences')


#14
print('='*14,'#14','='*15)
txt = 'MICHIGAN'
x = {}
for c in txt:
    if c not in x: #we have not seen this characters before, so initialize a counter for it
        x[c] = 0 
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1 #Se o caracter já foi visto incrementa +1
print('I: ' + str(x['I']) + ' occurences ') #Now i can find all the occurences, just print it out



#15
print('='*15,'#15','='*15)
sentence = 'The dog chased the rabbit into the forest but the rabbit was too quick.'
words = sentence.split()
word_counts = {}
for word in words: 
    if word not in word_counts:
        word_counts[word] = 0    
    word_counts[word] = word_counts[word] +1 
print(word_counts) 



#16 Completa extração e busca de multiplos dados.
print('='*15,'#16','='*15)

f = open ('olympics.txt', 'r')
txt = f.read() #now txt is one long string containing all te characters 
letter_counts = {} #start with an empty dictionary
for c in txt: 
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] = letter_counts[c] +1 
for y in letter_counts: 
    print('There are', letter_counts[y], "'", y, "'s")



#17 
print('='*15,'#17','='*15)
f = open ('olympics.txt', 'r')
txt = f.read() #now txt is one long string containing all te characters 
x = {} #start with an empty dictionary
for c in txt: 
    if c not in x:
        x[c] = 0
    x[c] = x[c] +1
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'm':3, 'n':1, 'o':1} 
scrabble_score = 0
for y in letter_values: 
    scrabble_score = scrabble_score + letter_values[y] * x[y]

print(scrabble_score)


#18 
print('='*15,'#18','='*15)
travel = {'North America': 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa": 1, "Antarctica":0, "Australia": 1} #The number of countries within each country someone has traveled to
total = 0
for continent in travel:
    total = total + travel[continent] #Soma de todos os valores contidos no dicionário
print(total)

 

#19 Find a particular key 
print('='*15,'#19','='*15)
nome = "João é legal"
d = {}

for c in nome:
    if c not in d:
        d[c] = 0
    d[c] = d[c] +1 
keys = list(d.keys())
min_value = keys [0]
for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print (min_value,d)


















