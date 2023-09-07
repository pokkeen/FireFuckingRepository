import requests
import json

CardID = None
ListID = None
TrelloAPIurlDict = {
    'ListFromBoard' :['GET', 'https://api.trello.com/1/boards/64f8ad85266330f160f747d7/lists'],
    'CardsFromList' :['GET',f'https://api.trello.com/1/lists/{ListID}/cards'],
    'EditCard' : ['PUT',f'https://api.trello.com/1/cards/{CardID}']
}

query = {
  'key': 'de9199f8a79a551dfdbd82da5bb84aeb',
  'token': 'ATTA38d848682569db14b6bb4c05aa318b5f16ab9853736bc8cdb24a4630faf55f43428EB0F2'
}

CardParts = ['name', 'desc']

def ListRequest(ListName):
    global ListID
    response = requests.request(TrelloAPIurlDict['ListFromBoard'][0], url=TrelloAPIurlDict['ListFromBoard'][1], params=query)
    for Lists in response.json():
        print(Lists['name'])
        if ListName == Lists['name']:
            
            ListID = Lists['id']
            return ListID
    

def CardRequest(ListName, CardName=None):
    global ListID
    global CardID
    if ListID == None:
        ListID = ListRequest(ListName)
    TrelloAPIurlDict['CardsFromList'][1] = f'https://api.trello.com/1/lists/{ListID}/cards'
    response = requests.request(TrelloAPIurlDict['CardsFromList'][0], url=TrelloAPIurlDict['CardsFromList'][1], params=query)
    for Cards in response.json():
        print(Cards['name'])
        if CardName == Cards['name']:
            CardID = Cards['id']
            return CardID
    
def CardEdit(ListName, CardName, NewCardPart, CardPartMod):
    global CardID
    if CardID == None:
        CardID = CardRequest(ListName, CardName)
    TrelloAPIurlDict['EditCard'][1] = f'https://api.trello.com/1/cards/{CardID}'
    if NewCardPart not in CardParts:
        return print('Not a valid modifier')
    query[NewCardPart] = CardPartMod
    response = requests.request(TrelloAPIurlDict['EditCard'][0], url=TrelloAPIurlDict['EditCard'][1], params=query)
    print(response)
    return

CardEdit('Test','Card2','name','Card2 But cooler')

