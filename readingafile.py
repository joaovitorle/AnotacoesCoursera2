fileref = open("olympics.txt", "r") #primeiro escolhe o arquivo e depois o "r" de read
contents = fileref.read() #função para ler de fato o arquivo
print(contents[:100]) #printar os primeiros 100 caracteres
fileref.close() 

print('-'*100)


fileref = open("olympics.txt", "r")
lines = fileref.readlines() #Cria uma lista e cada linha vira uma string
for line in lines[0:4]:
    print(line.strip()) #Printa as linhas e elimina os espaços

fileref.close()

print('-'*100)

fileref = open("olympics.txt", "r")
for line in fileref:
    print(line.strip())
fileref.close()

print('-'*100)

#To count the number of lines 
fileref = open("olympics.txt", "r")
lines = fileref.readlines()
print(len(lines))
fileref.close()

print('-'*100)

#To count the number of characters
fileref = open("olympics.txt", "r")
contents = fileref.read()
print(len(contents))
fileref.close()

print('-'*100)