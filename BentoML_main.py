from fastapi import FastAPI , Depends
from pydantic import BaseModel
from bentoml import load

class Inputdata(BaseModel):
    Company : int
    Job : int
    Degree : int



app = FastAPI(title="BentoML with FastAPI")

@app.get("/Predict/")
async def main(Inputdata : Inputdata = Depends()):

    '''if Inputdata.Company == "Reliance":
        C = 0
    elif Inputdata.Company == "Torrent":
        C = 2
    else: #Inputdata.Company == "Sun Pharma":
        C = 1
    if Inputdata.Job == "Sale":
        J = 2
    elif Inputdata.Job == "Business":
        J = 0
    else: #Inputdata.Job == "Computer":
        J = 1
    if Inputdata.Degree == "BE":
        D = 0
    else: #Inputdata.Degree == "ME":
        D = 1 '''

    save_path = "/home/keval2415/bentoml/repository/Classifier/20220116084935_FD6184"
    model = load(save_path)
    ans = str(model.predict([[Inputdata.Company,Inputdata.Job ,Inputdata.Degree]]))

    return {"Prediction" : ans}


