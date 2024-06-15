import instructor
from openai import OpenAI
from pydantic import BaseModel
import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class RolePrompt(BaseModel):
    question: str
    answer: str

role = "Michael Jordan"

input_text = "The project deadline is approaching fast, and the team is feeling anxious about the final presentation."

rp: RolePrompt = client.chat.completions.create(
        model="gpt-4o",
        response_model=RolePrompt,
        messages=[
            {
                "role": "user",
                "content": f"Analyze the following text from the perspective of a {role}: {input_text}"
            }
        ],
    )

print(json.dumps(rp.dict(), indent=2))