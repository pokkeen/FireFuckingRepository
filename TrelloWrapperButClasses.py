import requests

AuthDict = {
            'key': 'de9199f8a79a551dfdbd82da5bb84aeb',
            'token' : 'ATTA38d848682569db14b6bb4c05aa318b5f16ab9853736bc8cdb24a4630faf55f43428EB0F2'
}

class TrelloBoard:
    def __init__(self, ObjectName, ObjectID):
        self.ID = ObjectID
        self.Name = ObjectName

# DO NOT DELETE IMPORTANT FUNCTION IF DELETED REST OF CLASS BREAKS 
    def GetBoardCard(self, CardName):
        Response = requests.request('GET',url=f'https://api.trello.com/1/boards/{self.ID}/cards',params=AuthDict)
        print(Response)
        for Card in Response.json():
            if Card['name'].split(' | ')[0] == CardName or Card['name'] == CardName:
                return Card
        print('Card does not exist')

# DO NOT DELETE IMPORTANT FUNCTION IF DELETED REST OF CLASS BREAKS
    def GetBoardList(self, ListName):
        Response = requests.request('GET',url=f'https://api.trello.com/1/boards/{self.ID}/lists',params=AuthDict)
        print(Response)
        for List in Response.json():
            if List['name'] == ListName:
                return List
        print('List does not exist')

# DO NOT DELETE IMPORTANT FUNCTION IF DELETED REST OF CLASS BREAKS
    def GetBoardLabel(self, LabelName):
        Response = requests.request('GET',url=f'https://api.trello.com/1/boards/{self.ID}/labels',params=AuthDict)
        print(Response)
        for Label in Response.json():
            if Label['name'] == LabelName:
                return Label
        print('Label does not exist')
    
    def CreateCard(self, Name=None, Desc=None, List=None):
        AuthDict['idList'] = self.GetBoardList(List)['id']
        AuthDict['name'] = Name
        AuthDict['desc'] = Desc
        Response = requests.request("POST",url=f'https://api.trello.com/1/cards',params=AuthDict)
        print(Response)
    
    def GetListCards(self, List=None):
        ID = self.GetBoardList(List)['id']
        CardList = []
        Response = requests.request('GET',url=f'https://api.trello.com/1/lists/{ID}/cards',params=AuthDict)
        for cards in Response.json():
            CardList.append(cards)
        print(Response)
        return CardList
    
    def EditCardName(self,Name=None,Card=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['name'] = Name
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',params=AuthDict)
        print(Response)

    def EditCardDesc(self,Desc=None,Card=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['desc'] = Desc
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',params=AuthDict)
        print(Response)

    def AddLabel(self, Card=None, Label=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['idLabels'] = self.GetBoardLabel(Label)['id']
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',params=AuthDict)
        print(Response)
    
    def RemoveLabel(self,Card=None, Label=None):
        ID1 = self.GetBoardCard(Card)
        ID2 = self.GetBoardLabel(Label)
        Response = requests.request("DELETE",url=f'https://api.trello.com/1/cards/{ID1}/idLabels/{ID2}',params=AuthDict)
        print(Response)
    
    def Move(self,Card=None, List=None):
        ID = self.GetBoardCard(Card)
        AuthDict['idList'] = self.GetBoardList(List)
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',params=AuthDict)
        print(Response)
        print(Response.json())
