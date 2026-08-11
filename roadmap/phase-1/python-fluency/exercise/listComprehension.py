# Given nums = [1, 2, 3, 4, 5], build a list of each number squared.
nums = [1, 2, 3, 4, 5]
squaredNums = [num*num for num in nums ]

print(squaredNums) # [1, 4, 9, 16, 25]

# Given words = ["hello", "world", "python"], build a list of the length of each word.

words = ["hello", "world", "python"]

lengthOfWords = [len(word) for word in words]

print(lengthOfWords) # [5, 5, 6]

# Given celsius = [0, 20, 37, 100], convert each to Fahrenheit (f = c * 9/5 + 32).

celsius = [0, 20, 37, 100]

fahrenheit = [c * 9/5 + 32 for c in celsius]

print(fahrenheit) # [32.0, 68.0, 98.6, 212.0]

# From nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], keep only the even numbers.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [num for num in nums if num % 2 == 0]

print(even) # [2, 4, 6, 8, 10]

# From words = ["cat", "elephant", "dog", "giraffe", "ox"], keep only words longer than 3 letters.

words = ["cat", "elephant", "dog", "giraffe", "ox"]

longerThanThree = [word for word in words if len(word) > 3]

print(longerThanThree) # ['elephant', 'giraffe']

# From nums = range(1, 21), keep numbers divisible by both 2 and 3.

nums = range(1, 21)

numsDivisibleByTwoAndThree = [num for num in nums if num % 2 == 0 and num % 3 == 0]
print(numsDivisibleByTwoAndThree) # [6, 12, 18]

# Given nums = [-5, 3, -2, 8, -1, 0], produce a list where negatives become 0 and non-negatives stay as-is.

nums = [-5, 3, -2, 8, -1, 0]

integers = [0 if num < 0 else num for num in nums]
print(integers) # [0, 3, 0, 8, 0, 0]

# Given nums = [1, 2, 3, 4, 5, 6], produce a list of "even" or "odd" labels for each.

nums = [1, 2, 3, 4, 5, 6]

listOfEvenOdd = ["even" if num % 2 == 0 else "odd" for num in nums]
print(listOfEvenOdd) # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Given names = ["xicor", "vegeta", "korin"], produce them capitalized ("Xicor", …).

names = ["xicor", "vegeta", "korin"]

capitalizeNames = [name.capitalize() for name in names]
print(capitalizeNames) # ['Xicor', 'Vegeta', 'Korin']

# Given sentence = "the quick brown fox", build a list of the first letter of each word. (Hint: sentence.split().)

sentence = "the quick brown fox"
firstLetterOfEachWord = [s[0] for s in sentence.split(" ")]
print(firstLetterOfEachWord) # ['t', 'q', 'b', 'f']

# Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], flatten it into a single list [1, 2, 3, 4, 5, 6, 7, 8, 9].

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

singleList = [y for x in matrix for y in x] # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(singleList)

# Given the nested school structure from earlier (students and teachers, each a dict with a "data" list of {"name": ...}), build a flat list of every person's name.

students = {
    "data": [{
        "name":"Xicor"
    }, {
        "name": "Vegeta"
    }]
}

teachers = {
    "data": [
        {
            "name":"Master Roshi"
        }, {
            "name": "Korin"
        }
    ]
}

# nested dictionary

school = {
    "students":students,
    "teachers":teachers
}

names = [d["name"] for _,value in school.items() for d in value["data"] ]
print(names) # ['Xicor', 'Vegeta', 'Master Roshi', 'Korin']


# From matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], build a flat list of only the even numbers, each multiplied by 10 → [20, 40, 60, 80]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatList = [y * 10 for x in matrix for y in x if y % 2 == 0]
print(flatList) # [20, 40, 60, 80]

# Given pairs = [("amy", 88), ("ben", 32), ("cara", 71)], build a list of just the names of people who scored 40 or above.

pairs = [("amy", 88), ("ben", 32), ("cara", 71)]

names = [name for (name,score) in pairs if score >= 40]
print(names) # ['amy', 'ben', 'cara']