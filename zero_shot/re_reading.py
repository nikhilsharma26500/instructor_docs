import instructor
import json
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class Re_Reading(BaseModel):
    text: str
    prompt: str
    re_read_prompt: str
    response: str
    
input_text = "How does gravity work?"

prompt = (
    "This task involves re-reading a given text to understand the context and then answering a question based on that context. "
    "Given a specific text, your goal is to re-read it carefully to understand the context. "
    "Then, using only the information provided in the text, you should answer the question. "
    "This approach aims to test your ability to understand and interpret written information accurately."
)

rr: Re_Reading = client.chat.completions.create(
        model="gpt-4o",
        response_model=Re_Reading,
        messages=[
            {
                "role": "user",
                "content": f"{prompt} Here is the user question: { input_text }",
            }
        ],
    )

print(json.dumps(rr.dict(), indent=2))