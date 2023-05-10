from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

conn = psycopg2.connect(
    host="localhost",
    database="messages",
    user="postgres",
    password="1706",
)

cur = conn.cursor()

@app.post('/messages')
async def create_message(message: Message):
    # Generate a new ID by getting the maximum ID value from the database and adding 1
    cur.execute("SELECT MAX(id) FROM mess")
    max_id = cur.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    # Insert the new message into the database
    cur.execute("INSERT INTO mess (id, text) VALUES (%s, %s)", (new_id, message.text))
    conn.commit()

    # Return the new message with the generated ID
    return {"id": new_id, "text": message.text}