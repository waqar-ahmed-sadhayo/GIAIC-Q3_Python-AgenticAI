
def get_user_data():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")

    return first_name, last_name, email_address

def main():
    user_data = get_user_data()
    print(f"Received the following data: {user_data}")

if __name__ == "__main__":
    main()