def counting(num, increment):
    i = 0
    numbers = []

    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def Newcounting(num,incrementor):
    for i in range(0,num,incrementor):
        if i < num:
            print(i)



countingNew(10, 3)