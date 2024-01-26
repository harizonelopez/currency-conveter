# Dev_@ladinh production
# currency conveter program; a project which automatically sends messages to a number provided by the url

import pywhatkit
def currency_conveter():
    try:
        pywhatkit.sendwhatmsg("+254769405130", "Good morning sir, it's JARVIS", 12,10)
        print("Helloh! Your Message has been sent succesfully.")
        
    except:
        print("An error encountered while sending the message")
currency_conveter()
