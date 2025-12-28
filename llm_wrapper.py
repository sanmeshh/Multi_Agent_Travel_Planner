import os
from dotenv import load_dotenv
from google.genai import Client
from schemas.preferences import UserPreference

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create the Gemini Client
client = Client()

class LLM:
    def __init__(self, model="gemini-2.5-flash"):
        self.model = model

    def invoke(self, prompt: str) -> str:
        # generate_content calls Gemini text generation
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
        "response_mime_type": "application/json",
        "response_json_schema": UserPreference.model_json_schema(),
    }
        )
        # the SDK returns `.text` for the generated output
        return response.text

# singleton instance
llm = LLM()



