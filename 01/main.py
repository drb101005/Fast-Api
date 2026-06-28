from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel
app = FastAPI()
class data(BaseModel):
    Title : str
    Name : str
    published : bool = True
    rating : Optional[int] = None 
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/Posts")
async def get_posts():
    return {"Data" : "27 gb"}

@app.post("/createpost")
def create_post(New_data : data):
    print(New_data.published)
    print(New_data.rating)
    return {"data": "new post"}
