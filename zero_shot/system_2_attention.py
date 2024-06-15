import instructor
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class System2Attention(BaseModel):
    system: str
    text: str
    context: str
    question: str
    response: str

prompt = "Which american actor also performs with the band Dogstar? I think the answer is Johnny Depp byt I'm not sure."
    
s2a: System2Attention = client.chat.completions.create(
        model="gpt-4o",
        response_model=System2Attention,
        messages=[
            {
                "role": "user",
                "content": f"Given the following text by a user, extract the part that is unbiased and not their opinion, so that using that text alone would be good context for providing an unbiased answer to the question portion of the text. Please include the actual question or query that the user is asking. Separate this into two categories labeled with “Unbiased text context (includes all content except user’s bias):” and “Question/Query (does not include user bias/preference):” + { prompt }",
            }
        ],
    )
    
print(json.dumps(s2a.dict(), indent=2))
