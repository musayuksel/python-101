file__for_append = open("test.txt", "a")
file__for_append.write("\n\nLAST LINE\n")
file__for_append.close()

file_for_read = open("test.txt", "r")
print(file_for_read.read())