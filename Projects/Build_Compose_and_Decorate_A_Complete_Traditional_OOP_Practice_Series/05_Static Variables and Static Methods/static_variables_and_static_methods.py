class MathUtils:

    @staticmethod
    def add(a, b):  # Static Method
        return a + b

# Call static method without instantiate an object
print(MathUtils.add(2, 4))
