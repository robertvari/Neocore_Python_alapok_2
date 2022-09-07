def add_numbers(a: int, b: int):
    return a + b

def multiply_numbers(a: int, b: int):
    return a * b

def divide_numbers(a: int, b: int):
    return a / b

add_result = add_numbers(10, 4)
multiply_result = multiply_numbers(add_result, 10)
divide_result = divide_numbers(multiply_result, 200)

print(divide_result)

def return_multiple_results():
    return 10, 300, 32, 543

print(return_multiple_results())