from pydantic import BaseModel

class OrderDTO(BaseModel):
    account: str
    password: str
    contact: str
    remark: str