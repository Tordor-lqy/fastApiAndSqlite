from pydantic import BaseModel

class Result(BaseModel):
    msg: str
    code: int
    data: None