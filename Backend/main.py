from fastapi import FastAPI
import asyncpg

app = FastAPI()

@app.post("/messages")
async def create_message(text: str):
    # Connect to the Postgres database
    conn = await asyncpg.connect(
        user="your_username",
        password="your_password",
        database="your_database",
        host="your_host",
        port=your_port
    )

    # Insert the message into the database
    await conn.execute("INSERT INTO messages (text) VALUES ($1)", text)

    # Close the database connection
    await conn.close()

    # Return a JSON response with the inserted message data
    return {"text": text}
