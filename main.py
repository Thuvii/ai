import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
    load_dotenv()
    args = []
    verbose = "--verbose" in sys.argv
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            args.append(arg)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if not args:
        sys.exit(1)
    
    content = " ".join(args) 
    messages = [types.Content(role="user", parts=[types.Part(text=content)]),]
    if verbose:
        print(f"User prompt: {content}\n")

    generate_content(client, messages, verbose)

def generate_content(client, messages,verbose):
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print("Response:")
    print(response.text)
    

if __name__ == "__main__":
    main()
