# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n: int, low: int, high: int):
    if n >= low and n <= high:
        return True
    return False


print(in_range(6,5,10))
print(in_range(5,1,10))
print(in_range(1,1,10))
print(in_range(10,1,10))
print(in_range(0,1,10))

