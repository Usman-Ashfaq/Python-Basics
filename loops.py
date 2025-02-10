number=4
#use of while loop
while(number>0):
    number=number-1
    print("Usman")
print("Next")
#use of for loop
li=["Usman","Ashfaq"]
for i in li:
    print(i)
for i in range(0,4):
    print("Hello")
 
 #use of cases or switch
match number:
 case 1:
    print("Number conataains 4!")
 case 2:
    print("It is 2")
 case 3|4:
    print("It contains 4")    
 case _:
    print("Other number, 4 is not not present!")
#loop within loop
for i in range(1, 5):
    for j in range(i):
        print(i,end=' ')
    print()