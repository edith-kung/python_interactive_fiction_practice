import time

concern = 0


def typewriter(message):
    for letter in message:
        print(letter, end="",
              flush=True)  # flush helps us to print one letter by one letter and be displayed immediately
        time.sleep(0.025)
    print()
    time.sleep(1)


def activity_if_ontime():
    print("You swiped in on time")
    time.sleep(1)


def activity_iflate():
    print("one minute passes, you receive a concern on your record")
    punishment()
    time.sleep(1)


def punishment():
    global concern
    concern += 1  # concern = concern+1
    if concern == 3:
        print("You have received 3 concerns, you now have one warning on your record, you will now no longer receive \
        concerns and your next mistake will result in a warning.\nIf you receive two more warnings, you will receive \
        lunchtime detention.")
    elif concern == 5:
        print("You have received lunchtime detention. At lunchtime, please head to the staffroom.")


def handle_input(message):  # user input = what is typed the user, return sends the input to wherever it is called
    typewriter(message)
    user_input = input(
        ">>> ").strip().lower()  # strip removes leading+trailing blank chars, lower converts string to lowercase
    time.sleep(1)
    return user_input


def opening_message(valid_activities, instructions):
    activity = handle_input(
        "School begins at 8:10am, it is now 8:09am. What would you like to do?")  # activity = variable store user info
    while activity not in valid_activities:
        if activity in instructions:
            instructions[activity]()
        else:
            print("this is invalid")
        activity = handle_input(
            "School begins at 8:10am, it is now 8:09am. What would you like to do?")
    # from this point onwards activity should be valid
    valid_activities[activity]()  # activity is the input, which needs to match the dict, and becomes the key to point
    # back. Is function bc activity is defined by function


def punishment_record():
    if concern <= 2:
        print("You have", concern, "concern" + ("s" if concern != 1 else ""))
    elif concern <= 4:
        warning = concern - 2
        print("You have", warning, "warning" + ("s" if warning != 1 else ""))
    else:
        detention = concern - 4
        print("You have had", detention, "detention" + ("s" if detention != 1 else ""))


def main():
    typewriter("EXT. King George V School, established 1879. You are a new student, looking at the main entrance")
    valid_activities = {
        "do nothing": activity_iflate,
        "go inside": activity_if_ontime
    }
    instructions = {
        "check punishments": punishment_record
    }  # this dictionary contains all the instructions that do not advance plot or time
    opening_message(valid_activities, instructions)


main()
