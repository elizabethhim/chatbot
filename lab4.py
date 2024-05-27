import config
from openai import OpenAI

client = OpenAI(api_key=config.openai_key)

#Set API Key

#Create prompt
prompt = "A women in technology conference showing a person presenting in front of a large audience"

#Call the API
response = client.images.generate(prompt=prompt, n=1, size="512x512")

#Get image
image = response.data[0].url

#Output url
print(image)
