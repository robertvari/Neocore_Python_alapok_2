def calculate_result(a: int, b: int) -> int:
    # nested functions. Only callable in this scope.
    def add_number(x, y):
        return x + y

    def multiply_number(x, y):
        return x * y

    def divide_number(x, y):
        return x / y

    
    result = add_number(a, b)
    result = multiply_number(result, b)
    result = divide_number(result, b)

    return result


print( calculate_result(100, 425) )