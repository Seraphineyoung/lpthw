#This line imports argument variable from sys
from sys import argv

#This line unpacks the argv from the user input
script, filename = argv

#open filename and stores it in txt
txt = open(filename)

#prints the filename name
print(f"Here's is you file {filename}:")

#reads the file name
print(txt.read())
txt.close()

print("Type the filename again:")
#Ask the user for a filename from input function

file_again = input("> ")
#Opens it and stores in txt_again

txt_again = open(file_again)
#reads the content of txt_again
print(txt_again.read())

ttx_again.close()