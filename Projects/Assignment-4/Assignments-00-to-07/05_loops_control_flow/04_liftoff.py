# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
#
# Here's a sample run of the program:
#
# 10 9 8 7 6 5 4 3 2 1 Liftoff!
import time
def main():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
    print("Liftoff!")

if __name__ == "__main__":
    main()



