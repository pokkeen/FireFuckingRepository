#Yippee
ResponseList = {
   
    "Nice": ["Thank you"],
    "Mean": ["You suck"]

}

input = input()
if input == "y":
    print(ResponseList["Nice"][0])
else:
    print(ResponseList["Mean"][0])