'''My first personal project by using condition , modules and variables'''
# Here is step -1
import pyttsx3
engine = pyttsx3.init()
engine.say("Sir, please enter your six digit travel number")
engine.runAndWait()

# Here is step -2

user = int(input("Enter your six digit travel number : "))
if(user>99999 and user<1000000):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("Hello Ruhanyat, Have a safe journey!")
    engine.runAndWait()
else: 
# Here is step -3
    
    import pyttsx3
    import time
    time.sleep(1)
    engine = pyttsx3.init()
    engine.say("Sir, please enter a valid travel number")
    engine.runAndWait()