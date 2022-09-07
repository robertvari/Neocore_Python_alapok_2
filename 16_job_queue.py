import time, random, threading, queue

# classic python list
file_list = [
    "file1.mov",
    "file2.mov",
    "file3.mov",
    "file4.mov",
    "file5.mov",
    "file6.mov",
    "file7.mov",
]

# create a job queue
job_queue = queue.Queue()
# list comprehension
[job_queue.put(i) for i in file_list]


def video_worker():
    while not job_queue.empty():
        file = job_queue.get()
        print(f"{threading.current_thread().name} Worker started: {file}")
        time.sleep(random.randint(2, 10))
        print(f"{threading.current_thread().name} Worker finished: {file}")
        
        job_queue.task_done()


for _ in range(4):
    t = threading.Thread(target=video_worker)
    t.start()