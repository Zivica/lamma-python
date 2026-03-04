import os
from dotenv import load_dotenv
from google import genai
# from google.genai.types import UsageMetadata
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


def main():
    if api_key is None:
        raise Exception("API key not set")
    response = client.models.generate_content(model="gemini-2.5-flash",
                                              contents=args.user_prompt)

    if response.usage_metadata is None:
        raise Exception("No usage metadata")
    # print(response.contents)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.prompt_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
