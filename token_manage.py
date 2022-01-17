from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Token(BaseModel):
    ID : int
    Number_of_baggage_items: int 

dic = {i: None for i in range(1,101)}

@app.get("/")
def Home():
    return {"Hello" : "Welcome to token management system"}

@app.get("/List_all_active_token")
def List_all_active_token():
    cnt = 0
    lst = []
    for i in dic.keys():
        if dic[i] == None:
            cnt = cnt + 1
            lst.append(i)

    return {"Number of Token" : cnt ,
            "List of token" : lst
        }

@app.get("/get info for a given token ID{ID}")
def Get_info_given_token_ID(ID : int ):
    return {"Token ID" : ID , "Data" : dic[ID]}

@app.put("/Delete a token/{ID}")
def delete_token(ID : int):
    dic[ID] = None
    lst2 = []
    cnt2 = 0
    for j in dic.keys():
        if dic[j] == None:
            lst2.append(j)
            cnt2 = cnt2 + 1 

    return {"Token" : "Token is deleted" , "Available token" : cnt2 , "List of token" : lst2}

@app.post("/Update baggage count and store value {inputdata}")
def Update_baggage(inputdata : int):
    for i in dic.keys():
        if dic[i] == None:
            dic[i] = inputdata
            return {"Token ID" : i , "Number_of_baggage_items" : inputdata}
            break
        else:
            return {"Token":"Not available"}


    

    

