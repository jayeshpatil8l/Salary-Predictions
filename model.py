import pickle
from pydantic import BaseModel

class Data(BaseModel):
    designation : str
    age : int 
    exp : int 
    ratings : int
    leaves : int = 0

def predict(data : Data):
    with open("RFModel.pkl", "rb") as f:
        model = pickle.load(f)

    des_map = {"Analyst": 1, "Senior Analyst": 2, "Associate": 3, "Senior Manager": 4, "Manager": 5, "Director": 6}

    designation = des_map.get(data.designation)
    age = data.age
    exp = data.exp
    ratings = data.ratings
    leaves = data.leaves

    yhat = model.predict([[designation, age, exp, ratings, leaves]])[0]
    
    return "{:,.2f}".format(yhat)


