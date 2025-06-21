from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#API KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def user_input():
    prompt = input("Enter the prompt! ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return None
    #Exception handling if entered value is not valid
    try: 
        temperature = float(input("Enter temperture (creativity limits, 0.7 is the default) ") or 0.7)
        max_tokens = int(input("Max tokens? (100 is the default) ") or 100)
        top_p = float(input("Enter top_p (between 0 and 1) ")or 1)
    except ValueError:
        print("Invalid number, Try again!")
        return None
    
    return prompt, temperature, max_tokens, top_p


#Calls openAI
def ai_response(prompt, temperature, max_tokens, top_p):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": prompt}], 
        temperature=temperature, 
        max_tokens=max_tokens, 
        top_p =top_p
    )

    return completion.choices[0].message.content.strip()

#Calls the function where data is collected from the user
user_prompt = user_input() 

if user_prompt:
    #unpack the tuple
    prompt, temperature, max_tokens, top_p = user_prompt

    #tuple values inserted inside the response function
    response = ai_response(prompt, temperature, max_tokens, top_p)

    # Split the haiku into lines
    lines = response.split("\n")
    # Print each line clearly
    print("Response:\n")
    for line in lines:
        print(line.strip())
