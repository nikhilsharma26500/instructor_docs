import instructor
import json
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class SimToM(BaseModel):
    input_text: str
    first_prompt: str
    second_prompt: str
    response: str
    

input_text = "What is the capital of France?"

prompt = (
    "This task involves handling complex questions that include multiple entities, such as people or objects. "
    "Given a specific question, your goal is to first identify and isolate the set of facts known by one particular entity. "
    "Then, using only this information, you should answer the question. "
    "This process is divided into two main steps: "
    "1. Establishing the facts known by one entity. "
    "2. Answering the question based solely on those facts. "
    "This approach aims to minimize the impact of irrelevant information on the response."
)

stm: SimToM = client.chat.completions.create(
        model="gpt-4o",
        response_model=SimToM,
        messages=[
            {
                "role": "user",
                "content": f"{prompt} Here is the user question: { input_text }",
            }
        ],
    )

print(json.dumps(stm.dict(), indent=2))