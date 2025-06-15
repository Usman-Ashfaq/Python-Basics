import os

# Clear terminal (works for Windows and Unix)
os.system('cls' if os.name == 'nt' else 'clear')

def table(n):
    for i in range(1,n+1):
        print(n, "x", i, " = ", n*i)

n=10
table(n)