""" Main file for the UI and is responsible for running the main application """


# import eel
# eel.init('web')

# @eel.expose
# def maindata(dummy_parm):
#     print(dummy_parm)
#     return dummy_parm

# eel.start('index.html' , size=(20,20))

import eel

eel.init('Front_End')

# Dummy Function it will be changed later
@eel.expose
def dumm_function():
    return "Hello World"


eel.start('index.html' , size=(200,200))
# This is the skeleton code for starting the application