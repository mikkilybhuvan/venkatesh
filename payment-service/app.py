from fastapi import FastAPI

app = FastAPI()

@app.get("/payment")
def get_payment():
    return {
        "payment_id": 1,
        "status": "Success",
        "amount": 500
    }
