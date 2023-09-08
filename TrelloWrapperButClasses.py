import requests
import json

ListBoard = {}

class Trello:
    def __init__(self, TrelloKey, TrelloToken):
        self.TrelloKey = TrelloKey
        self.TrelloToken = TrelloToken
        self.AuthDict = {
            'key': TrelloKey,
            'token' : TrelloToken
        }

class TrelloBoard:
    def __init__(self, BoardID, AuthDict):
        response = requests.request("GET", url=f'https://api.trello.com/1/boards/{BoardID}', params=AuthDict)
        self.BoardID = BoardID
        self.BoardName = None

    def GetListsFromBoard(self, BoardID, AuthDict):
        response = requests.request("GET", url=f'https://api.trello.com/1/boards/{BoardID}/lists/{ListID}', params=AuthDict)
        global ListBoard
        for List in response.json():
            if List['name'] in ListBoard:
                print("List already in dict")
                pass
            ListBoard[List['name']] = List['id']
        return
    


    
    
trello = Trello('de9199f8a79a551dfdbd82da5bb84aeb', 'ATTA38d848682569db14b6bb4c05aa318b5f16ab9853736bc8cdb24a4630faf55f43428EB0F2')

trelloBoard = TrelloBoard('64f8ad85266330f160f747d7', trello.AuthDict)

class TrelloObject:
    def __init__(self, ObjectID, ObjectName):
        self.ObjectID = ObjectID
        self.ObjectName = ObjectName

    
class TrelloList(TrelloObject):
    def __init__(self, Name):
        super().__init__(None, Name)
        selfx   

class TrelloBoard(TrelloObject):
    def __init__(self, Name):
        super().__init__(None, Name)

class TrelloCard(TrelloObject):
    def __init__(self, Name):
        super().__init__(None, Name)

class TrelloLabel(TrelloObject):
    def __init__(self, Name):
        super().__init__(None, Name)



    

