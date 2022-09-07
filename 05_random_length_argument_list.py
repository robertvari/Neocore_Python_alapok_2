def hello(*args):
    for i in args:
        print(i)

# hello(
#     1, 
#     12, 
#     "Robert", 
#     ["csaba", "kriszta"]
# )

def hello2(**kwargs):
    print(kwargs)

# hello2(
#     name="Robert",
#     address="Budapest",
#     email="robert@gmail.com"
# )

def hello3(*args, **kwargs):
    print(args)
    print(kwargs)

hello3(
    1, 
    2, 
    3, 
    ["csaba", "csilla"], 
    name="Robert", 
    address="Budapest", 
    email="robert@gmail.com"
)