# Dev_@ladinh production
# currency conveter program; this project mainly entails automatically sending messages to a number provided in the url after a period of time you plan it to send the message

import pywhatkit

class Currency:
    def currency_conveter():
        try:
            sender_name = input("Enter your name\n:-> ")
            receiver_name = input("Enter the receiver's name\n:-> ")            
            pywhatkit.sendwhatmsg("+254769405130", "Good morning sir, it's JARVIS", 12,10)
            print(f"Helloh! {sender_name}, Your Message has been sent succesfully to {receiver_name}.")
            
        except:
            print(f"{sender_name}, An error encountered while sending the message to {receiver_name}")
    currency_conveter()
