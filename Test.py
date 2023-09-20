import TrelloWrapperButClasses
from TrelloWrapperButClasses import ListsDict
from TrelloWrapperButClasses import CardsDict
from TrelloWrapperButClasses import LabelsDict

import requests


TrelloBoard = TrelloWrapperButClasses.TrelloBoard

TestBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

TestBoard.InitalizeBoard()
print(CardsDict)
print(LabelsDict)
print(ListsDict)