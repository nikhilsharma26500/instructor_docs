import instructor
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Union
from dotenv import load_dotenv, find_dotenv
import os
import json

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Step 1: Define the Pydantic Models

class EmotionPrompt(BaseModel):
    text: str
    emotion_phrases: List[str]

class AnalyzedResponse(BaseModel):
    summary: str
    key_points: List[str]
    emotional_tone: str

# Step 2: Patch the OpenAI client to add response_model support
client = instructor.patch(OpenAI(api_key=OPENAI_API_KEY))

# Step 3: Define the function to generate structured data using emotion prompting
def analyze_text_with_emotion_prompts(input_text: str, emotion_phrases: List[str]) -> AnalyzedResponse:
    
    input_text = "The project deadline is approaching fast, and the team is feeling anxious about the final presentation."
    emotion_phrases = [
        "This is important to my career",
        "The success of this project affects my job security"
    ]
    
    """Analyzes text with emotional context using OpenAI's API."""
    emotional_context = " ".join(emotion_phrases)
    prompt = f"Analyze the following text considering the emotional context: {input_text}.\nEmotional context: {emotional_context}"
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_model=AnalyzedResponse
    )

# Step 4: Example Usage
if __name__ == "__main__":
    input_text = "The project deadline is approaching fast, and the team is feeling anxious about the final presentation."
    emotion_phrases = [
        "This is important to my career",
        "The success of this project affects my job security"
    ]

    response = analyze_text_with_emotion_prompts(input_text, emotion_phrases)
    print(json.dumps(response.dict(), indent=2))

