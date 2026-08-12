# Given nums = [1, 2, 2, 3, 3, 3, 4], build a set of each number squared. (Notice how the duplicates collapse.)

nums = [1,2,2,3,3,3,4] # note: set comprehension is required here because we are transforming the data.

uniqueNumsSquared = {num*num for num in nums}
print(uniqueNumsSquared) # {16, 1, 4, 9}

# Given words = ["Hello", "WORLD", "hello", "World"], build a set of the words all lowercased → how many distinct words are really there?

words = ["Hello", "WORLD", "hello", "World"]

lowerCaseWords = {word.lower() for word in words}
print(lowerCaseWords) # {'hello', 'world'}

# Given nums = range(1, 21), build a set of only the numbers divisible by 3.

nums = range(1, 21)

numsDivisibleByThree = {num for num in nums if num % 3 == 0}
print(numsDivisibleByThree) # {3, 6, 9, 12, 15, 18}

# Given sentence = "the cat sat on the mat", build a set of the distinct word lengths that appear.

sentence = "the cat sat on the mat"

distinctWordLengths = {len(word) for word in sentence.split()}
print(distinctWordLengths) # {2, 3}

# Given nums = [-5, 3, -2, 8, -1, 0, 4], build a set labeling each as "negative", "zero", or "positive" — how many distinct labels come out? (if/elif-style logic in the expression — you'll need nested if/else: "neg" if n < 0 else "zero" if n == 0 else "pos".)

nums = [-5, 3, -2, 8, -1, 0, 4]

uniqueLabels = {"negative" if num < 0 else "zero" if num == 0 else "positive"  for num in nums}
print(uniqueLabels) # {'zero', 'negative', 'positive'}