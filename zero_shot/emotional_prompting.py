import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Union
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class AnalyzedResponse(BaseModel):
    question: str
    answer: str

input_text = "What is gravity?"

emotion_prompt = "This is an extremely important topic for my exam"

client = instructor.from_openai(OpenAI(api_key=OPENAI_API_KEY))

ar: AnalyzedResponse = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {
                "role": "user",
                "content": f"Explain me: {input_text}.\n {emotion_prompt}"
            }
        ],
    response_model=AnalyzedResponse
)

print(json.dumps(ar.dict(), indent=2))
