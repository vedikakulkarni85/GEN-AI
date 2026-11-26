import os
from dotenv import load_dotenv
from google import genai
import time

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize client
client = genai.Client(api_key=api_key)

# Generate response with retry
for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents="What is Artificial Intelligence? Explain in simple words."
        )

        print("\nLLM Response:")
        print(response.text)
        break

    except Exception as error:
        print(f"Attempt {attempt + 1} failed: {error}")

        if attempt < 2:
            time.sleep(10)
        else:
            print("API request failed after 3 attempts.")

