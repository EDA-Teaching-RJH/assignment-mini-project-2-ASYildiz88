file = open("logs.txt", "r")

lines = file.readlines()

for line in lines:
    if "WARNING" in line:
        print(line)

file.close()