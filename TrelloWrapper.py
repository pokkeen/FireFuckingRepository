import requests
import json

BoardID = '64f8ad85266330f160f747d7'
CardID = None
ListID = None

TrelloAPIurlDict = {
    'ListsFromBoard' : ['GET', f'https://api.trello.com/1/boards/{BoardID}/lists'],
    'CardsFromList' : ['GET',f'https://api.trello.com/1/lists/{ListID}/cards'],
    'EditCard' : ['PUT',f'https://api.trello.com/1/cards/{CardID}'],
    'CreateCard' : ['POST', f'https://api.trello.com/1/cards'],
    'DeleteCard' : ['DELETE', f'https://api.trello.com/1/cards/{CardID}'],
    'LabelsFromBoard' : ['GET', f'https://api.trello.com/1/boards/{BoardID}/labels'],
    'CardsFromBoard' : ['GET', f'https://api.trello.com/1/boards/{BoardID}/cards']  
}
query = {
  'key': 'de9199f8a79a551dfdbd82da5bb84aeb',
  'token': 'ATTA38d848682569db14b6bb4c05aa318b5f16ab9853736bc8cdb24a4630faf55f43428EB0F2'
}

CardParts = ['name', 'desc', 'idLabels', 'idList']

def ListRequest(ListName):
    response = requests.request(TrelloAPIurlDict['ListsFromBoard'][0], url=TrelloAPIurlDict['ListsFromBoard'][1], params=query)
    print(response)
    for Lists in response.json():
        if ListName == Lists['name']:
            ListID = Lists['id']
    return ListID

def GetLabels(LabelName=None):
    if LabelName == None:
        return LabelName
    response = requests.request(TrelloAPIurlDict['LabelsFromBoard'][0], url=TrelloAPIurlDict['LabelsFromBoard'][1], params=query)
    for labels in response.json():
        if LabelName == labels['name']:
            LabelName = labels['id']
    return LabelName, response



def CardsFromBoard(CardName):
    response = requests.request(TrelloAPIurlDict['CardsFromBoard'][0], url=TrelloAPIurlDict['CardsFromBoard'][1], params=query)
    for Cards in response.json():
        if CardName == Cards['name']:
            CardID = Cards['id']
    return CardID, response



def DeleteCard(CardName):
    CardID = CardsFromBoard(CardName)
    TrelloAPIurlDict['DeleteCard'][1] = f'https://api.trello.com/1/cards/{CardID}'
    response = requests.request(TrelloAPIurlDict['DeleteCard'][0], url=TrelloAPIurlDict['DeleteCard'][1], params=query)
    return response



def CreateCard(ListName, CardName, CardLabel = None):
    ListID = ListRequest(ListName)
    query['idList'] = ListID
    query['name'] = CardName
    query['idLabels'] = CardLabel
    response = requests.request(TrelloAPIurlDict['CreateCard'][0], url=TrelloAPIurlDict['CreateCard'][1], params=query)
    return response



def CardEdit(CardName, NewCardPart=CardParts, CardPartMod=None):
    CardID = CardsFromBoard(CardName)
    TrelloAPIurlDict['EditCard'][1] = f'https://api.trello.com/1/cards/{CardID}'
    if NewCardPart not in CardParts:
        return print('Not a valid modifier')
    if NewCardPart == 'idLabels':
        CardPartMod = GetLabels(CardPartMod)
        print(CardPartMod)
    if NewCardPart == 'idList':
        CardPartMod = ListRequest(CardPartMod)
    query[NewCardPart] = CardPartMod
    response = requests.request(TrelloAPIurlDict['EditCard'][0], url=TrelloAPIurlDict['EditCard'][1], params=query)
    return response



def CardRequestFromList(ListName, CardName=None):
    global CardID
    CardList = []
    ListID = ListRequest(ListName)
    TrelloAPIurlDict['CardsFromList'][1] = f'https://api.trello.com/1/lists/{ListID}/cards'
    response = requests.request(TrelloAPIurlDict['CardsFromList'][0], url=TrelloAPIurlDict['CardsFromList'][1], params=query)
    for Cards in response.json():
        CardList.append(Cards['name'])
        if CardName == Cards['name']:
            CardID = Cards['id']
    return CardID, CardList
