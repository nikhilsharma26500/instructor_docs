import instructor
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv 
import os
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class StylePrompt(BaseModel):
    style: str
    text: str

style = "Franz Kafka peom"
input_text = "What is the purpose of life?"

sp: StylePrompt = client.chat.completions.create(
        model="gpt-4o",
        response_model=StylePrompt,
        messages=[
            {
                "role": "user",
                "content": f"Rewrite the following text in the style of {style}: {input_text}"
            }
        ],
    )

print(json.dumps(sp.dict(), indent=2))