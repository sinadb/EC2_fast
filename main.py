# This is a sample Python script.
import time

import uvicorn
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()



@app.get("/")
def root():
    return {"message": "Welcome to Mangum"}




# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
