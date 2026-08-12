# Generator A Generator is a function which we write, where yield produces a value and pause the function, resuming it on each next(),
# computing items lazily instead of all building up.

# Write first_n(n) that yields 0, 1, 2, ..., n-1, loop over first_n(5), and print each — predicting the output first.

def first_n(n):
    while(n > 0):
        yield n
        n -= 1
        
worker = first_n(5)

print(next(worker)) # 5
print(next(worker)) # 4
print(next(worker)) # 3
print(next(worker)) # 2
print(next(worker)) # 1
print(next(worker)) #  StopIteration

