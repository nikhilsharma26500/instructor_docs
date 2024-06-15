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
    summary: str
    key_points: List[str]
    emotional_tone: str

input_text = "The project deadline is approaching fast, and the team is feeling anxious about the final presentation."

emotion_phrases = [
        "This is important to my career",
        "The success of this project affects my job security"
]

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

emotional_context = " ".join(emotion_phrases)

ar: AnalyzedResponse = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {
                "role": "user",
                "content": f"Analyze the following text considering the emotional context: {input_text}.\nEmotional context: {emotional_context}"
            }
        ],
    response_model=AnalyzedResponse
)

print(json.dumps(ar.dict(), indent=2))
