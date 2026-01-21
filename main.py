from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

# Récupère la clé OpenAI depuis les variables d'environnement Render
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Autoriser toutes les origines pour le CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/email")
async def email(prompt: str = Form(...)):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    return {"answer": answer}

@app.post("/resume")
async def resume(prompt: str = Form(...)):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Résume ce texte : " + prompt}]
    )
    answer = response.choices[0].message.content
    return {"resume": answer}

@app.post("/tasks")
async def tasks(prompt: str = Form(...)):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Organise ces tâches : " + prompt}]
    )
    answer = response.choices[0].message.content
    return {"tasks": answer}
