import instructor
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class SelfAsk(BaseModel):
    text: str
    prompt: str
    self_ask_prompt: str
    response: str
    

input_text = "How does gravity work?"

sa: SelfAsk = client.chat.completions.create(
        model="gpt-4o",
        response_model=SelfAsk,
        messages=[
            {
                "role": "user",
                "content": f"Given the following text, generate a question that would be relevant to the text and provide an answer to that question. { input_text }",
            }
        ],
    )

print(json.dumps(sa.dict(), indent=2))