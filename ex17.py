from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Coping from {from_file} to {to_file}.")

in_file = open(from_file).read()
# indata = in_file.read()

print(f"The input is {len(in_file)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Reading, hit RETURN to continue, CTRL-C to abort.")
input()
#The write mode woud create and write
out_file = (open(to_file,'w')).write(in_file)

print("Alright, all done.")

