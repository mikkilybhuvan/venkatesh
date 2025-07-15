from fastapi import FastAPI

app = FastAPI()

@app.get("/order")
def get_order():
    return {
        "order_id": 1,
        "item": "Book",
        "price": 500
    }
