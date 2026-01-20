from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/email")
async def email(prompt: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"email": response.choices[0].message.content}

@app.post("/resume")
async def resume(prompt: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Résume ce texte : " + prompt}]
    )
    return {"resume": response.choices[0].message.content}

@app.post("/tasks")
async def tasks(prompt: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Organise ces tâches : " + prompt}]
    )
    return {"tasks": response.choices[0].message.content}
