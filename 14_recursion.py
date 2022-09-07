def call_myself(n):
    print(f"n = {n}")

    # exit block
    if n < 1:
        return  # early return

    # recursion step
    call_myself(n-1)

call_myself(10)