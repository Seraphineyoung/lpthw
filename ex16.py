from sys import argv

# #WRITING TO THE FILE
script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!.")


print("Now I am going to ask you three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()


#READING THE FILE ALREADY WRITTEN

# script, filename = argv

# open_file =  open(filename, "r")

# read_file = open_file.read()

# print(f"Reading file\n{read_file}")



# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	open for exclusive creation, failing if the file already exists
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
