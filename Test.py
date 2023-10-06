import TrelloWrapper


TrelloBoard = TrelloWrapper.TrelloBoard

TestBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

for tasks in TestBoard.GetListCards('To do'):
    tasks['labels'][0]['name']