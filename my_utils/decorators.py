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