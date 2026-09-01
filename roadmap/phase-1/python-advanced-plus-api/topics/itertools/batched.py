import itertools
from functools import wraps
import time

# WHat is batched in itertools ?

# It helps to create batches of the given data based on size n.
# This is also lazy which means it gives you one batch at a time. So, it takes memory of one batch at a time


data = [1, 2, 3, 4, 5, 6, 7]

for batch in itertools.batched(data, 3):
    print(batch)

# (1, 2, 3)
# (4, 5, 6)
# (7,)

# Practice set

# 1 — Basic batching + the partial last batch
# Use batched on list(range(23)) with size 5. Print each batch. Predict: how many batches, and what does the last one contain? (23 ÷ 5 — trace the full batches and the remainder.)

for batch in itertools.batched(range(23), 5):
    print(batch)

# prediction - 5 batches and last one contains 3 items

# output

# (0, 1, 2, 3, 4)
# (5, 6, 7, 8, 9)
# (10, 11, 12, 13, 14)
# (15, 16, 17, 18, 19)
# (20, 21, 22)


# 2 — Even division
# Use batched on list(range(12)) with size 4. Predict the batches. (12 ÷ 4 divides evenly — is there a partial batch here?)

for batch in itertools.batched(range(12), 4):
    print(batch)

# prediction - no partial batch as there is no remainder left
# output
# (0, 1, 2, 3)
# (4, 5, 6, 7)
# (8, 9, 10, 11)

# 3 — Batch size larger than the data
# Use batched on [1, 2, 3] with size 10. Predict — what happens when the batch size exceeds the number of items?

for batch in itertools.batched([1, 2, 3], 10):
    print(batch)

# prediction - 3  % 10 gives 3 remainder. So, it creates a batch of 3. AFter that, there is no item to create a batch.
# output - (1, 2, 3)


# 4 — The real-world loop
# Given documents = list(range(100)), batch into groups of 15, and for each batch call a function send_batch(batch) that prints f"sending {len(batch)} items". Predict the output — how many lines, and what's the size on the last line? (This is the API-batching skeleton; the last batch's size is the interesting part.)

documents = list(range(100))


def retry(attempts=1, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == attempts:
                        raise
                    print(f"Exception - {e}")
                    print(
                        f"Attempt : {attempt} failed . Retry in .... {current_delay} s"
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator


@retry(attempts=4, delay=1, backoff=2)
def send_batch(batch):
    print(f"sending {len(batch)} items")


for batch in itertools.batched(documents, 15):
    send_batch(batch)

# output

# send 15 items
# send 15 items
# send 15 items
# send 15 items
# send 15 items
# send 15 items
# send 10 items
