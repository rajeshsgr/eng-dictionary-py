import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def searchWord(w) :
    w=w.lower()
    if w in data: 
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0 :
        user_input= input("Did you mean %s ? Enter Y if yes or N if no :" % get_close_matches(w, data.keys())[0])
        if(user_input== "Y") :
            return data[get_close_matches(w, data.keys())[0]]
        elif (user_input== "N"):
            return " Word doesnt exist"
        else :
            return " Sorry we dont understand your entry"
            
    else:
        return " Word doesnt exist"



data = json.load(open("data.json"))

word = input("Enter word : ")

result= searchWord(word)

if type(result)==list:
    for output in result :
        print(output)
else :
    print(result)
