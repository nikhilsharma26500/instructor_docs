import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class RephraseAndRespond(BaseModel):
    text: str
    rephrased_text: str
    response: str
    

input_text = "How to make a biryani?"


rar: RephraseAndRespond = client.chat.completions.create(
        model="gpt-4o",
        response_model=RephraseAndRespond,
        messages=[
            {
                "role": "user",
                "content": f"Rephrase the following text: { input_text } and expand the question before generating the final answer and provide a response.",
            }
        ],
    )

print(json.dumps(rar.dict(), indent=2))