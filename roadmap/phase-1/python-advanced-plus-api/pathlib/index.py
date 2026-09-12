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


# There are scenarios where we actually need to process multiple files from a folder
# We can access those files using glob or rglob method.


# In order to access file, we need to mention the pattern in  glob method

# Example : path = Path("data").glob(*.csv) This will fetch all the csvs present at top level. Glob only checks the top level. If we want to check the subfolders also, use rglob

# If we want to match a particular pattern, use ?. ? only matches single character. For example: Path("data").glob(file?[123].txt) This will return files which are having file starts with file and matches any of these 1 or 2 or 3.


# Practice set

# 1 — Set up and glob
# First create a few test files: use mkdir to make a test_files/ folder, then write 3 files into it — a.txt, b.txt, and data.csv (use write_text with any content). Then use glob("*.txt") to find just the .txt files and print each. Predict which files it finds (and which it doesn't).

# __file__ gives the path where script is present and resolve gives the absolute path and
# parent returns the folder where script present.

directory = Path(__file__).resolve().parent

test_folder = directory / "data"

test_folder.mkdir(parents=True, exist_ok=True)

a = Path(test_folder / "a.txt")
a.write_text("Hello from A")

b = Path(test_folder / "b.txt")
b.write_text("Hello from B")

with open(test_folder / "data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["first_name", "last_name"])
    writer.writerows([["A", "B"], ["C", "D"]])

with open(test_folder / "data1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["first_name", "last_name"])
    writer.writerows([["E", "F"], ["G", "H"]])


for file in test_folder.glob("*.txt"):
    print(file.read_text())


for csvFile in test_folder.glob("*.csv"):
    with open(csvFile, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


# 2 — Different patterns
# Using your test_files/ folder, glob for: (a) all files (*), (b) all .csv files, (c) all files (*.*). Print the results of each. Predict what each pattern matches.


allFiles = test_folder.glob("*")
print(list(allFiles))

csvFiles = test_folder.glob("*.csv")
print(list(csvFiles))

files = test_folder.glob("*.*")
print(list(files))

# * and *.* give the same results. But "* will return the files which dont have . Here it returns the same output as "*.* because all file contains .

# 3 — Count and sort
# Glob all .txt files, sort them, and print them in sorted order. Then count how many .txt files there are. (Practices sorted() on glob output and counting.)

sorted_files = sorted(test_folder.glob("*.txt"))
print(len(sorted_files))


# 4 — The real-world pattern (folder of files)
# Create 2 CSV files in a folder, each with a header and a couple of rows. Then write a loop that globs all *.csv files, opens each (with encoding="utf-8"), reads them with DictReader, and prints each row. (This is the client-integration skeleton — find all CSVs in a folder, process each.)

csvFiles = test_folder.glob("*.csv")
for file in csvFiles:
    with open(file, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

# output

# {'first_name': 'A', 'last_name': 'B'}
# {'first_name': 'C', 'last_name': 'D'}
# {'first_name': 'E', 'last_name': 'F'}
# {'first_name': 'G', 'last_name': 'H'}
