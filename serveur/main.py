from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Classe pour le modèle de données de la requête
class Message(BaseModel):
    content: str

@app.post("/message")
async def receive_message(message: Message):
    if not message.content:
        raise HTTPException(status_code=400, detail="No content provided")
    # Traitement du message reçu ici
    print(f"Message reçu: {message.content}")
    return {"status": "success", "message": "Message reçu avec succès"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
