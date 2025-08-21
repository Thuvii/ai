import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

#
from call_functions import available_functions
from sys_prompt import system_prompt

#
from call_functions import call_function

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
    for i in range(1,21):
        try:
            result = generate_content(client, messages, verbose)
            if result is not None:
                print(result)
                break
                
        except Exception as e:
            raise Exception(f'Error: {e}')
        
    

def generate_content(client, messages,verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
    )
    
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
    
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    if not response.function_calls:
        return response.text
    
    function_responses = []
    for item in response.function_calls:
            function_call_result = call_function(item,verbose)
            if not function_call_result.parts or not function_call_result.parts[0].function_response:
                raise Exception("Empty function call result")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
            if not function_responses:
                raise Exception("no function responses generated, exiting.")
    for item in function_responses:
        messages.append(types.Content(role="user", parts=[item]),)
    
    
   
            
            
    

if __name__ == "__main__":
    main()
