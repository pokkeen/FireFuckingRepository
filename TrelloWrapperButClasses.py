import requests
import json

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

    def EditCardName(self, Name):
        AuthDict['name'] = Name
        Response = requests.request(
            "PUT",
            url=f'https://api.trello.com/1/cards/{self.ObjectID}',
            params=AuthDict
        )
        print(Response)
    
    def EditCardDesc(CardID, Desc):
        AuthDict['desc'] = Desc
        Response = requests.request(
            "PUT",
            f'https://api.trello.com/1/cards/{CardID}',
            AuthDict
        )
    
    def EditCardLabels(CardID, Label):
        AuthDict['idLabels'] = Label
        Response = requests.request(
            "PUT",
            f'https://api.trello.com/1/cards/{CardID}',
            AuthDict
        )

    def MoveCard(CardID, ListID):
        AuthDict['idList'] = ListID
        Response = requests.request(
            "PUT",
            f'https://api.trello.com/1/cards/{CardID}',
            AuthDict
        )

class TrelloLabel(TrelloObject):
    def __init__(self, Name, ID):
        super().__init__(ID, Name)

class testClass():
    def __init__(self):
        self.Fuck = None
        return
    
    def NewClass(self):
        Filler = testClass()
        return Filler

cals = testClass()
NewThing = cals.NewClass()
NewThing.Fuck = "Frick"
print(NewThing.Fuck)

TestBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

TestBoard.InitalizeBoard()
print(CardsDict)
print(ListsDict)
print(LabelsDict)

CardsDict['Card1'].EditCardName('Fuck YOU suck my fucking nuts you little n-x')