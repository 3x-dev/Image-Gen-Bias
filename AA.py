import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if OPENAI_API_KEY is not None:
    openai.api_key = OPENAI_API_KEY
else:
    raise ValueError("No OpenAI API key found. Make sure your .env file is present with the required key.")

def generate_images_from_prompts(prompts, n=1, size="1024x1024", quality="standard"):
    image_urls = []
    for prompt in prompts:
        try:
            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                n=n,
            )
            image_url = response['data'][0]['url']
            image_urls.append(image_url)
        except Exception as e:
            print(f"Error generating image for prompt '{prompt}': {str(e)}")
    return image_urls

with open('African_American_Prompts.txt', 'r') as file:
    prompts = [line.strip() for line in file.readlines()]

image_urls = generate_images_from_prompts(prompts[:3])

for url in image_urls:
    print(url)
