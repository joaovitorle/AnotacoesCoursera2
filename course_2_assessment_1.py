#1 Read the number of characters 

fileref = open("travel_plans.txt","r")
num = 0
for i in fileref:
    num = num + len(i)
fileref.close()


#2 Read the number of words

num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)

#3 Read the number of lines
num_lines = 0
fileref = "school_prompt.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_lines += 1

#4 Read the first 30 characters 

fileref = open("school_prompt.txt","r")
beginning_chars = fileref.read(30)
print (beginning_chars)

fileref.close()

#5 Find a specific character number in which line

three = [] 
with open('school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)

#6 Find a specific character number in which line

emotions = [] #Criar lista
with open('emotion_words.txt', 'r') as f:
    emotions = [line.split()[0] for line in f] #Cria uma lista na line e então buscar o caractere 0
    print(emotions) 
