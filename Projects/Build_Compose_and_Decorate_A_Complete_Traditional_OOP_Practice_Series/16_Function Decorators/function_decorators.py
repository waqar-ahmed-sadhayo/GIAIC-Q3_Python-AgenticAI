# Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator using @ syntax
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
