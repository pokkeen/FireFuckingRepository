import TrelloWrapper
import requests

def ShowToDoList():
    print(TrelloWrapper.CardRequestFromList('To do'))
    return

ShowToDoList()

class TrelloObject:
    def __init__(self):
        self.ObjectID = None
        self.ObjectName = None

    def testshit(self):
        self.ObjectID = 1

Obj = TrelloObject()

print(Obj.ObjectID)