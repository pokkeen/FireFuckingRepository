import TrelloWrapperButClasses
from TrelloWrapperButClasses import ListsDict
from TrelloWrapperButClasses import CardsDict
from TrelloWrapperButClasses import LabelsDict

TrelloBoard = TrelloWrapperButClasses.TrelloBoard

TestBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

TestBoard.InitalizeBoard()
CardsDict['Card1'].RemoveLabel(LabelsDict['Claimed'])