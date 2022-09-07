from my_utils.file_utils import get_all_files

def call_myself(n):
    print(f"n = {n}")

    # exit block
    if n < 1:
        return  # early return

    # recursion step
    call_myself(n-1)
# call_myself(10)

file_list = []
# r = raw string
root_folder = r"C:\Work\_PythonSuli\Neocore"
get_all_files(root_folder, file_list)

for i in file_list:
    print(i)

print(f"File count: {len(file_list)}")