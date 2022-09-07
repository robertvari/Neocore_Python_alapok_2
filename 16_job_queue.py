import time, random

file_list = [
    "file1.mov",
    "file2.mov",
    "file3.mov",
    "file4.mov",
    "file5.mov",
    "file6.mov",
    "file7.mov",
]


def video_worker(file):
    print(f"Worker started: {file}")
    time.sleep(random.randint(10, 30))
    print(f"Worker finished: {file}")

for i in file_list:
    video_worker(i)