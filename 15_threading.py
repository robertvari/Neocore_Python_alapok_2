import time, random, threading


def worker1(name, email):
    print(f"Worker 1 started: name {name} emai {email}")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished!")

def worker2():
    print("Worker 2 started....")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished!")

def worker3():
    print("Worker 3 started....")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished!")

# dedicate threads for our functions
t1 = threading.Thread(target=worker1, args=["Robert", "robert@gmail.com"])
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)

# start threads
t1.start()
t2.start()
t3.start()