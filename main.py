from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import db
from pojo.OrderDTO import OrderDTO
from pojo.Result import Result

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

rootHtml = open("static/index.html" ,  encoding='utf-8').read()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/" , response_class=HTMLResponse)
def read_root():
    rootHtml = open("static/index.html" ,  encoding='utf-8').read()
    return rootHtml

@app.post("/api/submit/order")
def submitOrder(orderDTO : OrderDTO):

    account = orderDTO.account
    password = orderDTO.password
    contact = orderDTO.contact
    note = orderDTO.remark

    conn , cursor = db.getDb()
    # 将订单数据插入数据库
    cursor.execute('INSERT INTO orders (account, password, contact , note) VALUES (?, ?,?, ?)',
                    (account, password,contact, note))
    conn.commit()


    # result = Result()
    # result.code = 1
    # result.msg = 'success'
    # result.data = None
    # return result
    return {"msg" : "success" , "code" : 1 , "data" : None}
    

@app.get("/api/query/order")
def submitOrder(contact : int):

    conn , cursor = db.getDb()

    cursor.execute('SELECT * FROM orders WHERE contact = ?', (contact,))
    orders_data = cursor.fetchall()
    
    # 将查询结果转换为字典列表
    orders = []
    for order in orders_data:
        order_dict = {
            'id': order[0],
            'order_time': order[1],
            'order_status': order[2],
            'account': order[3],
            'password': order[4],
            'note': order[6],
            'order_amount': order[7]
        }
        orders.append(order_dict)

    return {"msg" : "success" , "code" : 1,"data" : orders}
