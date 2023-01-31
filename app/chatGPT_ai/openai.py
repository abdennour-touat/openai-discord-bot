from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("CHATGPT-TOKEN")


def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=100
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
        return prompt_response


def chatgpt_image_response(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    return image_url
