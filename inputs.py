import time

def typewriter(params):
    message = params["message"]
    for letter in message:
        print(letter, end="",
              flush=True)  # flush helps us to print one letter by one letter and be displayed immediately
    print()
    time.sleep(1)

def handle_input(message):  # user input = what is typed the user, return sends the input to wherever it is called
    typewriter({ "message": message })
    user_input = input(
        ">>> ").strip().lower()  # strip removes leading+trailing blank chars, lower converts string to lowercase
    time.sleep(1)
    return user_input