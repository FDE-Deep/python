# Requests

# requests is not a built in library. We need to install it.

# It has two operations get and post.

# Get

import requests
from functools import wraps

timeout = 10
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)  # 200
data = response.json()
print(data)


def retry(attempts=1, exceptions=(), delay=1, offset=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == attempts:
                        raise
                    current_delay *= offset

        return wrapper

    return decorator


@retry(attempts=1, exceptions=(requests.Timeout, requests.HTTPError), delay=1, offset=2)
def getData(url):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


print(getData("https://jsonplaceholder.typicode.com/todos/1"))


@retry(attempts=1, exceptions=(requests.Timeout, requests.HTTPError), delay=1, offset=2)
def postData(url, requestBody):
    response = requests.post(url, json=requestBody, timeout=timeout)
    return response.json()


data = {"title": "title", "body": "bar", "userId": 100}
print(postData("https://jsonplaceholder.typicode.com/posts", data))


# Practice set

# 1 — A basic GET
# Use requests.get to call a free public API (e.g. https://api.github.com/users/torvalds or https://jsonplaceholder.typicode.com/todos/1). Print the status_code, then .json() the response and print some fields. Include a timeout.


response = requests.get("https://api.github.com/users/torvalds", timeout=timeout)
print(response.status_code)
data = response.json()
print(data)
print(data["login"])  # torvalds
print(data["id"])  # 1024025


# 2 — Check status codes
# Call a URL that returns 404 (e.g. https://jsonplaceholder.typicode.com/todos/99999999 or a made-up path). Check the status_code and print a friendly message if it's not 200. Then try raise_for_status() in a try/except and catch the HTTPError.

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/99999999", timeout=timeout
)
if response.status_code != 200:
    print("Try Again")
else:
    data = response.json()

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/99999999", timeout=timeout
    )
    response.raise_for_status()
except requests.HTTPError as e:
    print(e)


# 3 — A POST
# Use requests.post to send JSON to https://jsonplaceholder.typicode.com/posts (a fake API that echoes back what you send). Send {"title": "test", "body": "hello", "userId": 1}, print the status code and the response. (This API fakes creation and returns your data with an id — good for practicing POST.)


body = {"title": "test", "body": "hello", "userId": 1}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=body, timeout=timeout
)
print(response.status_code)
data = response.json()
print(data)


# 4 — .env and secrets (the important one)
# Create a .env file with a fake key like API_KEY=my_secret_123. Create a .gitignore with .env in it. Write code that uses load_dotenv() + os.getenv("API_KEY") to read the key and print it. Then create a .env.example with API_KEY=your_key_here. (This is the whole secrets-management pattern — practice it now so it's automatic.)

import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")
print(key)


# 5 — Combine: a real API call with timeout + retry
# Take your @retry decorator. Write a function that calls a public API with a timeout, uses raise_for_status(), and is wrapped with @retry. This is the production shape — API call + timeout + retry + proper error handling, everything from the week together.


print(getData("https://jsonplaceholder.typicode.com/todos/1"))
