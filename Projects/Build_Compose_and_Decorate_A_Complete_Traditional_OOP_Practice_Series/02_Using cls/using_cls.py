class Counter:
    count = 0   # class variable to track number of objects

    def __init__(self):
        Counter.count += 1   # increment count whenever a new object is created

    @classmethod
    def display_count(cls):
        print(f"Total Objects: {cls.count}")


# Create some objects
c1 = Counter()
c2 = Counter()
c3 = Counter()


# Call class method to show count
Counter.display_count()
