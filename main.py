from fastapi import FastAPI
from pydantic import BaseModel
from numerology import DestinyCalculator

app = FastAPI()

class BirthdayIn(BaseModel):
    birthday: str

@app.post("/brief")
def get_brief(info: BirthdayIn):
    calc = DestinyCalculator(info.birthday)
    return calc.get_brief()

@app.post("/codes")
def get_codes(info: BirthdayIn):
    calc = DestinyCalculator(info.birthday)
    return {"codes": calc.get_codes()}

@app.post("/five")
def get_five(info: BirthdayIn):
    calc = DestinyCalculator(info.birthday)
    return calc.get_five_elements()
