# Given nums = [1, 2, 3, 4, 5], build a dict mapping each number to its cube → {1: 1, 2: 8, 3: 27, ...}.

nums = [1, 2, 3, 4, 5]

cubeNums = {num: num*num*num for num in nums}
print(cubeNums) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# Given words = ["cat", "elephant", "dog"], build a dict mapping each word to its length → {"cat": 3, "elephant": 8, "dog": 3}.

words = ["cat", "elephant", "dog"]

wordsLength = {word:len(word) for word in words}
print(wordsLength) # {'cat': 3, 'elephant': 8, 'dog': 3}

# Given names = ["xicor", "vegeta", "korin"], build a dict mapping each name to its capitalized form → {"xicor": "Xicor", ...}.

names = ["xicor", "vegeta", "korin"]

capitalizedNames = {name: name.capitalize() for name in names}

print(capitalizedNames) # {'xicor': 'Xicor', 'vegeta': 'Vegeta', 'korin': 'Korin'}

# Given products = ["pen", "book", "bag"] and prices = [10, 50, 120], build a dict mapping each product to its price.

products = ["pen", "book", "bag"]
prices = [10, 50, 120]

# pricesOfProducts = {key:value for key,value in list(zip(products,prices))}

# better version

pricesOfProducts = dict(zip(products,prices))
print(pricesOfProducts) # {'pen': 10, 'book': 50, 'bag': 120}

# Given keys = ["name", "age", "city"] and values = ["Xicor", 22, "Tokyo"], zip them into a single dict.

keys = ["name", "age", "city"]
values = ["Xicor", 22, "Tokyo"]

# personInfo = {key:value for key,value in list(zip(keys,values))}

# better version
personInfo = dict(zip(keys,values))
print(personInfo) # {'name': 'Xicor', 'age': 22, 'city': 'Tokyo'}

# Given scores = {"amy": 88, "ben": 32, "cara": 71, "dan": 45}, build a new dict of only those who scored 50 or above.
scores = {"amy": 88, "ben": 32, "cara": 71, "dan": 45}

onlyFiftyOrAbove = {key:value for key,value in scores.items() if value >= 50}
print(onlyFiftyOrAbove) # {'amy': 88, 'cara': 71}

# Given prices = {"pen": 10, "book": 50, "bag": 120, "pin": 5}, build a dict of only the items priced under 100.

prices = {"pen": 10, "book": 50, "bag": 120, "pin": 5}

pricesUnderHundered = {key:value for key,value in prices.items() if value < 100}
print(pricesUnderHundered) # {'pen': 10, 'book': 50, 'pin': 5}

# Given prices = {"pen": 10, "book": 50}, build a new dict with every price increased by 10% (value * 1.1), keys unchanged.

prices = {"pen": 10, "book": 50}

pricesIncreased = {key:value * 1.1 for key,value in prices.items()}
print(pricesIncreased) # {'pen': 11.0, 'book': 55.00000000000001} why we are getting 55.0000000001 please explain

# Given scores = {"amy": 88, "ben": 32}, build a dict mapping each name to "pass" or "fail" (pass if score ≥ 40). (This is the if/else-in-the-expression form — the value position, before the for.)

scores = {"amy": 88, "ben": 32}

passOrFail = {key: "pass" if value >= 40 else "fail" for key,value in scores.items()}
print(passOrFail) # {'amy': 'pass', 'ben': 'fail'}

# Given codes = {"IN": "India", "JP": "Japan", "US": "USA"}, build the reverse dict → {"India": "IN", "Japan": "JP", "US": "USA"}

codes = {"IN": "India", "JP": "Japan", "US": "USA"}
reverseCodes = {value:key for key,value in codes.items()}
print(reverseCodes) # {'India': 'IN', 'Japan': 'JP', 'USA': 'US'}

# Given fruits = ["apple", "banana", "cherry"], build a dict mapping each fruit to its position → {"apple": 0, "banana": 1, "cherry": 2}. (Hint: enumerate(fruits) gives you (index, item) pairs — mind which one becomes the key.)

fruits = ["apple", "banana", "cherry"]

fruitsAtPosition = {item:index for index,item in enumerate(fruits)} 
print(fruitsAtPosition) # {'apple': 0, 'banana': 1, 'cherry': 2}

# Given sentence = "the quick brown fox", build a dict mapping each word to its length, but only for words longer than 3 letters → {"quick": 5, "brown": 5}. (split + filter + build.)

sentence = "the quick brown fox"

wordsLength = {word:len(word) for word  in sentence.split() if(len(word) > 3)}
print(wordsLength) # {'quick': 5, 'brown': 5}

# From nums = range(1, 11), build a dict mapping each number to "even" or "odd" — but only for numbers greater than 5 → {6: "even", 7: "odd", 8: "even", 9: "odd", 10: "even"}. (filter + if/else value + all in one.)

nums = range(1, 11)

evenOrOddGreaterThanFive = {num: "even" if num % 2 == 0 else "odd" for num in nums if num > 5}
print(evenOrOddGreaterThanFive) # {6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}