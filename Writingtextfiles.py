file_obj = open("squares.txt", "w") #Usar w de writing
for number in range (13):
    square = number * number
    file_obj.write(str(square))
    file_obj.write('\n')
    
file_obj.close()
