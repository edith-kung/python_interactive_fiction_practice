import time
concern = 2
def typewriter(message):
    for letter in message:
        print(letter, end = "", flush = True) # flush helps us to print one letter by one letter and be displayed immediately
    print()
    time.sleep(1)

def activity_if_ontime():
    print("You swiped in on time")
    time.sleep(1)

def activity_iflate():
    global concern
    print("one minute passes, you receive a concern on your record")
    concern += 1 # concern = concern+1 
    warning()
    time.sleep(1)
    
def warning():
    if concern == 3:
        print("You have received 3 concerns, \
              you have now received one warning.")

def handle_input(message): # user input = what is typed the user, return sends the input to wherever it is called
    typewriter(message)
    user_input = input(">>> ").strip().lower() # strip removes leading+trailing blank chars, lower converts string to lowercase
    time.sleep(1)
    return user_input

def opening_message(valid_activities):
    activity = handle_input(
        "School begins at 8:10am, it is now 8:09am. What would you like to do?")  # activity = variable store user info
    while (activity not in valid_activities):
        print("this is invalid")
        activity = handle_input(
            "School begins at 8:10am, it is now 8:09am. What would you like to do?")
    # from this point onwards activity should be valid
    valid_activities[activity]() # activity is the input, which needs to match the dict, and becomes the key to point back. Is function bc activity is defined by function

def main():
    typewriter("EXT. King George V School, established 1879. You are a new student, looking at the main entrance")
    valid_activities = {
        "do nothing": activity_iflate,
        "go inside": activity_if_ontime
    }
    opening_message(valid_activities)

main()
