from textwrap import wrap
import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        print("my_timer started...")

        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Process time: {time.time() - start_time}")

        return result
    return wrapper

def hello_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello! How are you?")
        result = func(*args, **kwargs)
        return result
    return wrapper