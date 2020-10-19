print('='*15,'#1','='*15)
#1 

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for c in Junior:
    credits = credits + Junior[c]

print('='*15,'#2','='*15)
#2

str1 = "peter piper picked a peck of pickled peppers"

freq = {}

for c in str1:
    if c not in freq: 
        freq[c] = 0
    freq[c] = freq[c] +1
for y in freq:
    print(freq[y], y)

print('='*15,'#3','='*15)
#3 

s1 = "hello"
counts = {}
for c in s1:
    if c not in counts:
        counts[c] = 0
    counts[c] = counts[c] +1
for y in counts:
    print(counts[y],y)


print('='*15,'#4','='*15)
#4
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
str1_splited = str1.split()
for c in str1_splited:
    if c not in freq_words:
        freq_words[c] = 0
    freq_words[c] = freq_words[c] +1 
for y in freq_words:
    print ('There are', freq_words[y], 'of' ,y)


print('='*15,'#5','='*15)
#5
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {} 
sent_splited = sent.split()
for c in sent_splited:
    if c not in wrd_d:
        wrd_d[c] = 0
    wrd_d[c] = wrd_d[c] +1
for y in wrd_d:
    print(wrd_d[y],y)


print('='*15,'#6','='*15)
#6
sally = "sally sells sea shells by the sea shore"
characters = {}
total = 0
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c] + 1 
keys = list(characters.keys())
best_char = keys [0]
for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print (best_char,characters)


print('='*15,'#7','='*15)
#7
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for c in sally:
    if c not in characters:
        characters[c] = 0 
    characters[c] = characters[c] +1
keys = list(characters.keys())
worst_char = keys[0]
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char =key
print(worst_char)


print('='*15,'#8','='*15)
#8

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}
string1_lower = string1.lower()
for c in string1_lower:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] = letter_counts[c] +1
for y in letter_counts:
    print("There are", letter_counts[y], "of", y)


print('='*15,'#9','='*15)
#9
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
p_low = p.lower()
for c in p_low:
    if c not in low_d:
        low_d[c] = 0
    low_d[c] = low_d[c] + 1
for y in low_d:
    print('There are', low_d[y], "of", y)


