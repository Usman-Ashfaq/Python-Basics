# In Python, decorators are a powerful and flexible way to modify or extend 
# the behavior of functions or methods, without changing their actual code

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator             
def fun():
    print("Hello Usman")

fun()
