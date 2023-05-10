from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class Message(BaseModel):
    id: int
    text: str

conn = psycopg2.connect(
    host="localhost",
    database="messages",
    user="postgres",
    password="1706",
)

cur = conn.cursor()

@app.post("/messages")
async def create_message(message: Message):
    cur.execute("INSERT INTO mess (id, text) VALUES (%s, %s)", (message.id, message.text))
    conn.commit()
    return {"message": "Message created"}
