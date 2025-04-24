import  random

def computer_gues(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"IS {guess} too High (H), too Low (L), or Correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay!, Computer guessed your number, {guess}, correctly!")

computer_gues(100)