# Class A
class A:
    def show(self):
        print("Class A Method")


# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Class B Method")


# Class C also inherits from A and overrides show()
class C(A):
    def show(self):
        print("Class C Method")


# Class D inherits from both B and C (Diamond Inheritance)
class D(B, C):
    pass

# Create an object of D
obj = D()

# Call the show() method
obj.show()


# Print the Method Resolution Order (MRO)
print(D.mro())