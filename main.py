import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

#
from call_functions import available_functions
from sys_prompt import system_prompt

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
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
    )
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    if not response.function_calls:
        print("Response:")
        print(response.text)
    else:
        for item in response.function_calls:
            print(f"Calling function: {item}")
  
            
            
    

if __name__ == "__main__":
    main()
