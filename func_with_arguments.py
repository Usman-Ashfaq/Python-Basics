def func(*args):
    for i in args:
        print(i)


func(1, 2, 3, 4, 5)

def average(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("Sum of the numbers is:", sum)
    print("Average: ", sum/len(args))
average(2, 2, 3, 4, 5)

def fun(**kwargs):
    for k, val in kwargs.items():
        print(f" hi {val}")
        #print(f"{k}: {val}")


fun(name="Alice", age=30, city="New York")
