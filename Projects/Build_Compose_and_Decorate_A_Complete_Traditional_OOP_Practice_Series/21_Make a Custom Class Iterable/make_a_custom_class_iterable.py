import time

class Countdown:
    def __init__(self, start):
        # Initialize the starting number
        self.start = start
        self.current = start  # This keeps track of the current number in the countdown

    def __iter__(self):
        # Return the iterator object itself
        # Also reset the current number so the countdown can be reused
        self.current = self.start
        return self

    def __next__(self):
        # Stop iteration if current number is less than 0
        if self.current < 0:
            raise StopIteration
        # Store the current number to return
        value = self.current
        # Decrease current number for the next call
        self.current -= 1
        return value



# Create a Countdown object starting from 5
cd = Countdown(5)

# Use a for-loop to iterate through the countdown
print("Counting down:")
for num in cd:
    print(num)
    time.sleep(1)