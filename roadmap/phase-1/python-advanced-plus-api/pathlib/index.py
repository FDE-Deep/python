# What is pathlib?

# A pathlib is a modern way of handling OS operations like file read /write etc


# Practice set
import json
import csv
from pathlib import Path

# 1 — pathlib basics
# Create a Path to "data/reports/summary.txt" using the / operator. Then print its .name, .stem, .suffix, and .parent. Predict each.

p = Path("data/reports/summary.txt")

print(p.name)  # summary.txt
print(p.stem)  # summary
print(p.suffix)  # .txt
print(p.parent)  # data\reports

# 2 — Safely ensure a directory + write
# Use mkdir(parents=True, exist_ok=True) to create a test_output/ folder, then use write_text to write "hello" to a file inside it, then read_text it back and assert it matches. (This is the safe "make folder, write file" pattern — like your library's save.)

Path("test_output/").mkdir(parents=True, exist_ok=True)
p = Path("test_output/output.txt")
p.write_text("Hello World")
print(p.read_text() == "Hello World")
# QUestion: Path.mkdir is just to create directories and verify if it exist or not.
# And if we want to create a file for read write operation then we need to create a seperate path object for that ?
# I mean why cant we creat an object of mkdir and use that object to read/write

# 3 — JSON round-trip
# Take a Python dict, write it to a .json file with json.dump (indent=2), read it back with json.load, and assert the loaded data equals the original. Use a Path for the file. (You did this in your library — now with pathlib.)

dic = {"name": "Xicor", "anime": "Dragon Ball Af"}

jsonFile = Path("test_output/jsonFile.json")
jsonFile.parent.mkdir(parents=True, exist_ok=True)
with open(jsonFile, "w") as file:
    json.dump(dic, file, indent=2)

with open(jsonFile) as file:
    data = json.load(file)

print(data)  # {'name': 'Xicor', 'anime': 'Dragon Ball Af'}


# 4 — CSV read/write
# Write a CSV file with a header row and two data rows using csv.writer (remember newline=""). Then read it back with csv.DictReader and print each row as a dict. Predict the output.

csvFile = Path("test_output/csvFile.csv")
csvFile.parent.mkdir(parents=True, exist_ok=True)

with open(csvFile, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "anime"])
    writer.writerow(["Xicor", "Dragon Ball AF"])
    writer.writerows([["Majin Vegeta", "Dragon Ball Z"], ["Goku", "Dragon Ball Z"]])

with open(csvFile) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# output:
# {'name': 'Xicor', 'anime': 'Dragon Ball Af'}
# {'name': 'Xicor', 'anime': 'Dragon Ball AF'}
# {'name': 'Majin Vegeta', 'anime': 'Dragon Ball Z'}
# {'name': 'Goku', 'anime': 'Dragon Ball Z'}
