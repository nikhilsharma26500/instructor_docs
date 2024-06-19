import instructor
import os
import json
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class KNN(BaseModel):
    text: str
    prompt: str
    knn_prompt: str
    response: str
    
input_text = "How does gravity work?"

prompt = (
    "This task involves generating a response to a given text based on the context provided and save it in knn_prompt."
    "Given a specific text, your goal is to generate a response that is relevant to the text. "
    "This approach aims to test your ability to understand and interpret written information accurately."
)

knn: KNN = client.chat.completions.create(
        model="gpt-4o",
        response_model=KNN,
        messages=[
            {
                "role": "user",
                "content": f"{prompt} Here is the user question: { input_text }",
            }
        ],
    )

print(json.dumps(knn.dict(), indent=2))