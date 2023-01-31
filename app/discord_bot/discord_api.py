from dotenv import load_dotenv
import discord
import os

from app.chatGPT_ai.openai import chatgpt_response, chatgpt_image_response


load_dotenv()
discord_token = os.getenv("DISCORD-TOKEN")


class Client(discord.Client):
    async def on_ready(self):
        print("logged in as ", self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None
        if message.content.startswith("/ai"):
            command = message.content.split(" ")[0]
            user_message = message.content.replace("/ai", "")
            print(command, user_message)
        elif message.content.startswith("/ai-img"):
            command = message.content.split(" ")[0]
            user_message = message.content.replace("/ai-img", "")
            print(command, user_message)

        if command == "/ai":
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
        elif command == "/ai-img":
            bot_response = chatgpt_image_response(prompt=user_message)
            await message.channel.send(bot_response)


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
