import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("OPENAI_API_KEY")

print("Using OpenAI API key:", os.getenv("OPENAI_API_KEY"))