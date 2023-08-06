def add_punishment(concern):
    concern += 1  # concern = concern+1
    if concern == 3:
        print("You have received 3 concerns, you now have one warning on your record, you will now no longer receive "\
        "concerns and your next mistake will result in a warning.\nIf you receive two more warnings, you will receive "\
        "lunchtime detention.")
    elif concern == 5:
        print("You have received lunchtime detention. At lunchtime, please head to the staffroom.")
    return concern

def plural(val):
    return "s" if val != 1 else ""

def punishment_record(params):
    concern = params["concern"]
    if concern <= 0:
        return # print unsuccessful message?
    elif concern <= 2:
        print("You have", concern, "concern" + plural(concern))
    elif concern <= 4:
        warning = concern - 2
        print("You have", warning, "warning" + plural(warning))
    else:
        detention = concern - 4
        print("You have had", detention, "detention" + plural(detention))
