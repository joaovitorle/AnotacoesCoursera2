with open ('squares.txt', 'r') as md: #Here we are using with and the variable"md" 
    for line in md:
        print(line.strip())

#Using with we dont need to close the file
