import re

file = open("logs.txt", "r")

lines = file.readlines()

for line in lines:
    if re.search("ERROR", line):
        print("ERROR:", line)

    elif re.search("WARNING", line):
        print("WARNING:", line)

    elif re.search("INFO", line):
        print("INFO:", line)

file.close()