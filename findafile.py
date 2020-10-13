fileref = open("../../Textos/Teste01.txt", "r") # Os "../.." representa que estavam voltando duas pastas, ou seja chega até a pasta "Projetos" e depois é só colocar o diretório e o nome do arquivo
contents = fileref.read()
print (contents)
fileref.close()

print('-'*100)