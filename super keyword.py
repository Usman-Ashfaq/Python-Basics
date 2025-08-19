#super calls the correct functions insteadof calling wwrong one

class A:
    def display(self):
        print("Display from class A")
class B(A):
    def display(self):
        print("Display from class B")
        super().display()  # Calls the display method from class A
class C(B):
    def display(self):
        print("Display from class C")
        super().display()  # Calls the display method from class B
c= C()
c.display()
#b = B()
#b.display()  # This will print "Display from class B" followed


