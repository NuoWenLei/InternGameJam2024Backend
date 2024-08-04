import os, random
from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI
from openai import OpenAI

from constants import characterPrompt, systemPrompt, mapping, reverseMapping, maximumMovements

load_dotenv()

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)

app = FastAPI()

@app.get("/generateCharacterActions")
def generateActions(description: str, customContext: str):

  prompt = f"""{systemPrompt} {customContext}
{characterPrompt}{description}

List of actions:
"""
  
  print(prompt)

  completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": prompt}
    ],
    model="gpt-4o-mini",
  )

  msg = completion.choices[0].message
  print(msg)
  mappedActions = mapping.values()
  filteredCharacters = [reverseMapping[c] for c in msg.content.upper() if c in mappedActions]
  return filteredCharacters[:maximumMovements]
    
    

