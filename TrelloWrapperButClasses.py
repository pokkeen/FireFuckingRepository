import requests

AuthDict = {
            'key': 'de9199f8a79a551dfdbd82da5bb84aeb',
            'token' : 'ATTA38d848682569db14b6bb4c05aa318b5f16ab9853736bc8cdb24a4630faf55f43428EB0F2'
}

CardsDict = {}
ListsDict = {}
LabelsDict = {}



class TrelloObject:
    def __init__(self, ObjectID, ObjectName):
        self.ObjectID = ObjectID
        self.ObjectName = ObjectName

#When Creating a board, you should probably initialize the entire board so what does this mean?
#When the board is initialized, it gets creates all the cards and list on a specific board
#This is so I can initialize multiple boards in different parts of a code so its easier to manage certain parts
class TrelloBoard(TrelloObject):
    def __init__(self, Name, ID):
        super().__init__(ID, Name)
    
    def InitalizeBoard(self):
        ListsFromBoard = requests.request('GET', url=f'https://api.trello.com/1/boards/{self.ObjectID}/lists', params=AuthDict)
        for Lists in ListsFromBoard.json():
            ListsDict[Lists['name']] = TrelloList(Lists['name'],Lists['id'])
        CardsFromBoard = requests.request('GET', url=f'https://api.trello.com/1/boards/{self.ObjectID}/cards', params=AuthDict)
        for Cards in CardsFromBoard.json():
            CardsDict[Cards['name']] = TrelloCard(Cards['name'],Cards['id'])
        LabelsFromBoard = requests.request('GET', url=f'https://api.trello.com/1/boards/{self.ObjectID}/labels', params=AuthDict)
        for Labels in LabelsFromBoard.json():
            LabelsDict[Labels['name']] = TrelloLabel(Labels['name'],Labels['id'])

     
class TrelloList(TrelloObject):
    def __init__(self, Name, ID):
        super().__init__(ID, Name) 
    
class TrelloCard(TrelloObject):
    def __init__(self, Name, ID):
        super().__init__(ID, Name)

    def GetCard(self):
        Response = requests.request(
            "GET", 
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response.json())

    def EditName(self,Name):
        AuthDict['name'] = Name
        Response = requests.request(
            "PUT",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response)
    
    def EditDesc(self,Desc):
        AuthDict['desc'] = Desc
        Response = requests.request(
            "PUT",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response)
    
    def AddLabel(self,Label):
        AuthDict['idLabels'] = Label.ObjectID
        Response = requests.request(
            "PUT",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response)
    
    def RemoveLabel(self,Label):
        Response = requests.request(
            "DELETE",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}/idLabels/{Label.ObjectID}',
            params=AuthDict
        )
        print(Response)

    def Move(self,ListID):
        AuthDict['idList'] = ListID
        Response = requests.request(
            "PUT",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response)
        print(Response.json())

class TrelloLabel(TrelloObject):
    def __init__(self, Name, ID):
        super().__init__(ID, Name)

