import requests

AuthDict = {
            'key': '[Private]',
            'token' : '[Private]'
}
Headers = {
  "Accept": "application/json"
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
            if CardName in Card['name'].split(' | '):
                return Card
        print('Card does not exist')
        return None

# DO NOT DELETE IMPORTANT FUNCTION IF DELETED REST OF CLASS BREAKS
    def GetBoardList(self, ListName):
        Response = requests.request('GET',url=f'https://api.trello.com/1/boards/{self.ID}/lists',headers=Headers,params=AuthDict)
        print(Response)
        for List in Response.json():
            if ListName in List['name'].split(' | '):
                return List
        print('List does not exist')
        return None

# DO NOT DELETE IMPORTANT FUNCTION IF DELETED REST OF CLASS BREAKS
    def GetBoardLabel(self, LabelName):
        Response = requests.request('GET',url=f'https://api.trello.com/1/boards/{self.ID}/labels',params=AuthDict)
        print(Response)
        for Label in Response.json():
            if Label['name'] == LabelName:
                return Label
        print('Label does not exist')
        return None
    
    def CreateCard(self, Name=None, Desc=None, List=None, Label=None):
        AuthDict['idList'] = self.GetBoardList(List)['id']
        AuthDict['name'] = Name
        AuthDict['desc'] = Desc
        AuthDict['idLabels'] = self.GetBoardLabel(Label)['id']
        Response = requests.request("POST",url=f'https://api.trello.com/1/cards',headers=Headers,params=AuthDict)
        print(Response)
    
    def GetListCards(self, List=None):
        ID = self.GetBoardList(List)['id']
        Response = requests.request('GET',url=f'https://api.trello.com/1/lists/{ID}/cards',headers=Headers,params=AuthDict)
        return Response.json()
          
    def EditCardName(self,Name=None,Card=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['name'] = Name
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',headers=Headers,params=AuthDict)
        print(Response)

    def EditCardDesc(self,Desc=None,Card=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['desc'] = Desc
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',headers=Headers,params=AuthDict)
        print(Response)

    def AddLabel(self, Card=None, Label=None):
        ID = self.GetBoardCard(Card)
        AuthDict['idLabels'] = self.GetBoardLabel(Label)['id']
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',headers=Headers,params=AuthDict)
        print(Response)
    
    def RemoveLabel(self,Card=None, Label=None):
        ID1 = self.GetBoardCard(Card)['id']
        ID2 = self.GetBoardLabel(Label)['id']
        Response = requests.request("DELETE",url=f'https://api.trello.com/1/cards/{ID1}/idLabels/{ID2}',params=AuthDict)
        print(Response)
    
    def Move(self,Card=None, List=None):
        ID = self.GetBoardCard(Card)['id']
        AuthDict['idList'] = self.GetBoardList(List)['id']
        Response = requests.request("PUT",url=f'https://api.trello.com/1/cards/{ID}',headers=Headers,params=AuthDict)
        print(Response)

    def CreateList(self, Name=None):
        AuthDict['name'] = Name
        AuthDict['idBoard'] = self.ID
        Response = requests.request('POST', url='https://api.trello.com/1/lists', params=AuthDict)
        print(Response)
