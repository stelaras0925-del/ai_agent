import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if api_key == None:
        raise RuntimeError("Api key not found")
    

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]
    content = client.models.generate_content(model='gemini-2.5-flash', contents=messages)
    usage = content.usage_metadata
    print(f"User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(f"Response: \n{content.text}")

if __name__ == "__main__":
    main()
