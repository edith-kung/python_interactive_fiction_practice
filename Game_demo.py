import time
from punishments import *
from inputs import *

global_variables = {
    "concern": 0
}
instructions = {
    "check punishments": {
        "functions": [
            {
                "function": punishment_record,
                "global params": ["concern"]
            }
        ]
    }
}  # this dictionary contains all the instructions that do not advance plot or time

def receive_concern():
    global_variables["concern"] = add_punishment(global_variables["concern"])

def activity_if_ontime():
    print("You swiped in on time")
    time.sleep(1)

def activity_if_late():
    print("one minute passes, you receive a concern on your record")
    time.sleep(1)

def get_global_params(params):
    return dict([(i, global_variables[i]) for i in params])

def get_params(func):
    if "params" in func:
        return func["params"]
    params = {}
    if "dict params" in func:
        params = params | func["dict params"]
    if "global params" in func:
        params = params | get_global_params(func["global params"])
    return params

def run_functions(dictionary):
    if "functions" in dictionary:
        for func in dictionary["functions"]:
            params = get_params(func)
            if (params):
                func["function"](params)
                continue
            func["function"]()
    if "branch" in dictionary:
        return opening_message(dictionary["branch"])

def opening_message(event):
    activity = handle_input(event["prompt"])  # activity = variable store user info
    if activity in event["valid_activities"]:
        return run_functions(event["valid_activities"][activity])  # activity is the input, which needs to match the dict, and becomes the key to point
    elif activity in instructions:
        run_functions(instructions[activity])
    else:
        print("this is invalid")
    opening_message(event)

def main():
    typewriter({ "message": "EXT. King George V School, established 1879. You are a new student, looking at the main entrance"})
    doing_nothing_activities = {
        "prompt": "Don't just stand there, do something!",
        "valid_activities": {
            "do nothing": {
                "functions": [
                    {
                        "function": activity_if_late
                    }
                ]
            },
            "run away": {
                "functions": [
                    {
                        "function": activity_if_late
                    }
                ]
            }
        }
    }
    go_inside_activities = {
        "prompt": "You are standing next to the gate. What would you like to do?",
        "valid_activities": {
            "swipe in": {
                "functions": [
                    {
                        "function": activity_if_ontime
                    }
                ]
            },
            "go to class": {
                "functions": [
                    {
                        "function": activity_if_late
                    }
                ]
            }
        }
    }
    first_event = {
        "prompt": "School begins at 8:10am, it is now 8:09am. What would you like to do?",
        "valid_activities": {
            "do nothing": {
                "branch": doing_nothing_activities, # next branch
                "functions": [ # to run when this option is chosen before going onto next branch
                    {
                        "function": typewriter,
                        "dict params":
                            {
                                "message": "one minute passes, you receive a concern on your record"
                            }
                    },
                    {
                        "function": receive_concern
                    }
                ]
            }, 
            "go inside": {
                "branch": go_inside_activities
            }
        }
    }
    opening_message(first_event)


main()