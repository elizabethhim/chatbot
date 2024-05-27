import config
from openai import OpenAI

client = OpenAI(api_key=config.openai_key)

def generate_response(myprompt):
    response = client.completions.create(model="gpt-3.5-turbo",
    prompt=myprompt,
    temperature=.1,
    max_tokens=1024)
    print (response.choices)
    return response.choices[0].text.strip()

def main ():
    myprompt = input("How can I help you? \n")
    print(generate_response(myprompt))

if __name__ == "__main__":
    main()