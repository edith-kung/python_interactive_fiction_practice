import time
from punishments import *
from inputs import *

concern = 4

def activity_if_ontime():
    print("You swiped in on time")
    time.sleep(1)

def activity_iflate():
    global concern
    print("one minute passes, you receive a concern on your record")
    concern = add_punishment(concern)
    time.sleep(1)

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
