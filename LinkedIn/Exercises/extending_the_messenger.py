# Create a class "SaveMessages" that extends the Messenger class that does the following things:

# Add any messages it receives to a list, along with the time the message was received
# Use the provided "getCurrentTime" function so that the received message time is a string
# Contains a method called "printMessages" that prints all collected messages when it's called.
# You might also consider clearing the message list when "printMessages" is called.

from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass

class SaveMessages(Messenger):
    def __init__(self,listeners=[]):
        super().__init__(listeners)
        self.messages_with_time = []

    def receive(self, message):
        self.messages_with_time.append((message,getCurrentTime()))
    
    def printMessages(self):
        for message in self.messages_with_time:
            print(message[0],message[1])
        self.messages_with_time = []
    

# Test 
listener = SaveMessages()

messenger = Messenger([listener])

messenger.send("Hello")
messenger.send("How are you?")
messenger.send("I'm good, thanks!")

listener.printMessages()