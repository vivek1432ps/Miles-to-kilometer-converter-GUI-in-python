row = int(input("Enter the height of the piramida:"))

for i in range(row):


    print(("*" * (i * 2 + 1)).center(row * 2 - 1))