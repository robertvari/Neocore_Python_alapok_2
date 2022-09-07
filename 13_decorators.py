import time, random
from my_utils.decorators import my_timer

@my_timer
def worker1():
    print("Worker 1 started....")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished!")

@my_timer
def worker2():
    print("Worker 2 started....")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished!")

@my_timer
def worker3():
    print("Worker 3 started....")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished!")


worker1()
worker2()
worker3()