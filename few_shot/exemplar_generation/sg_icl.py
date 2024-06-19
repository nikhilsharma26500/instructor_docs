import instructor
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json
from pydantic import BaseModel, Field
from typing import List, Optional

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

class SelfGeneration(BaseModel):
    text: str
    self_generation_prompt: str
    positive_response: str
    negative_response: str
    
input_text = "this movie is very slow and long"

self_generation_prompt = (
    f"Generate a review: { input_text }. Generate a positive review for the movie."
    f"Generate a review: { input_text }. Generate a negative review for the movie."
)

sg: SelfGeneration = client.chat.completions.create(
        model="gpt-4o",
        response_model=SelfGeneration,
        messages=[
            {
                "role": "user",
                "content": f"{self_generation_prompt}",
            }
        ],
    )

class InferenceResponse(BaseModel):
    text: str
    positive_response: str
    negative_response: str
    sentiment: str
    
inference_input = "this movie is very boring and incoherent"
    
inference_prompt = (
    "Your goal is to generate a response to the following reviews."
    "Sentiment should be Positive or Negative."
    f"Review: {sg.dict()['positive_response']}"
    "Sentiment positive"
    f"Review: {sg.dict()['negative_response']}"
    "Sentiment negative"
    f"Review: {inference_input}"
    "Sentiment: "
)

inf: InferenceResponse = client.chat.completions.create(
        model="gpt-4o",
        response_model=InferenceResponse,
        messages=[
            {
                "role": "user",
                "content": f"{inference_prompt}",
            }
        ],
    )

print(json.dumps(inf.dict(), indent=2))