# Given nums = [1, 2, 3, 4, 5], create a generator expression that yields each number doubled. Print the generator object itself first (don't convert it), then pull the first two values with next(). Predict all three outputs.

nums = [1, 2, 3, 4, 5]

numsWorker = (num * 2 for num in nums)
print(numsWorker) # <generator object <genexpr> at 0x00000278328D92F0>
print(next(numsWorker)) # 2
print(next(numsWorker)) # 4
print(next(numsWorker)) # 6

# Given nums = [1, 2, 3, 4, 5], create a generator of squares, then convert it to a list. Predict the output — and predict what a second list() call on the same generator gives.

nums = [1, 2, 3, 4, 5]
numsWorker = (num * num for num in nums)

print(list(numsWorker)) # [1, 4, 9, 16, 25]
print(list(numsWorker)) # []

# From nums = range(1, 11), make a generator of only the odd numbers. Loop over it with a for and print each.

nums = range(1,11)

numsWorker = (num for num in nums if num % 2 == 1)

for num in numsWorker:
    print(num,end = " ") # 1 3 5 7 9 here once the for loop prints all the numbers , the worker will be exhausted right ?
    
# Given words = ["cat", "elephant", "dog", "giraffe"], make a generator that yields each word's length, but only for words longer than 3 letters.

words = ["cat", "elephant", "dog", "giraffe"]

wordsWorker = (len(word) for word in words if len(word) > 3)
print()
print(next(wordsWorker)) # 8
print(next(wordsWorker)) # 7
# print(next(wordsWorker)) # StopIteration

# Given nums = [-3, 5, -1, 8, 0], make a generator yielding "neg", "zero", or "pos" for each (the chained if/else from your set-comprehension work).

nums = [-3, 5, -1, 8, 0]

numsWorker = ("neg" if num < 0 else "zero" if num == 0 else "pos" for num in nums)

print(next(numsWorker)) # neg
print(next(numsWorker)) # pos
print(next(numsWorker)) # neg
print(next(numsWorker)) # pos
print(next(numsWorker)) # zero

# Given nums = [1, 2, 3, 4, 5], use sum() with a generator expression to add up all the squares — in one line, no intermediate list. (Recall you can drop the extra parentheses: sum(... for ...).)

nums = [1, 2, 3, 4, 5]

sumOfNums = sum (num * num for num in nums)
print(sumOfNums) # 55 the worker is an iterator right ? so does sum create a list out of it first and then loop through and sum it ?

# Given nums = [4, 1, 7, 3, 9, 2], use max() with a generator expression to find the largest value after adding 10 to each.

nums = [4, 1, 7, 3, 9, 2]

maxNum = max(num + 10 for num in nums)
print(maxNum) # 19

# Given words = ["hi", "hello", "hey", "howdy"], use sum() with a generator to count how many words start with "h". (Hint: sum(1 for w in words if ...) — a common counting trick. Think about why True behaves like 1 here.)

words = ["hi", "hello", "hey", "howdy"]

sumofWordsStartsWithh = sum(1 for word in words if word[0] == 'h')
print(sumofWordsStartsWithh) # I didnt get where true behaves as 1. according to me,it is behaving an integer only

# Predict the output of each print line, and explain the second:

gen = (n * 2 for n in [1, 2, 3])
print(list(gen)) # [2,4,6]
print(list(gen)) # []

# Predict what this prints, and think carefully about when the numbers appear relative to the "made a generator" message:

def loud(x):
    print(f"  computing {x}")
    return x * x

gen = (loud(n) for n in [1, 2, 3])
print("made a generator") # made a generator
first = next(gen) # 1
print(f"got {first}") # got 2