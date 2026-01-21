from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

# Récupère la clé OpenAI depuis les variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# CORS pour autoriser toutes les origines
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle de données pour recevoir le prompt en JSON
class PromptRequest(BaseModel):
    prompt: str

@app.post("/email")
async def email(request: PromptRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"answer": response.choices[0].message.content}
    except openai.error.RateLimitError:
        return {"error": "Quota OpenAI dépassé, veuillez vérifier votre plan."}

@app.post("/resume")
async def resume(request: PromptRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Résume ce texte : " + request.prompt}]
        )
        return {"resume": response.choices[0].message.content}
    except openai.error.RateLimitError:
        return {"error": "Quota OpenAI dépassé, veuillez vérifier votre plan."}

@app.post("/tasks")
async def tasks(request: PromptRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Organise ces tâches : " + request.prompt}]
        )
        return {"tasks": response.choices[0].message.content}
    except openai.error.RateLimitError:
        return {"error": "Quota OpenAI dépassé, veuillez vérifier votre plan."}
