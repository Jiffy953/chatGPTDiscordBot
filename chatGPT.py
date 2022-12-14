from revChatGPT.revChatGPT import Chatbot
import discord
from discord.ext import commands
import os
import re



token = 'your_discord_bot_token_goes_here' #can also move .env for better security if you care about that

config = {
  "session_token": "your_chatgpt_token_goes_here", #follow guide on  https://github.com/acheong08/ChatGPT on how to obtain
}

chatbot = Chatbot(config, conversation_id=None)
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready(): #ready check
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!chat'): #TODO add toggle to stop allowing inputs until message has been sent 
    responce = getResponce(message.content)
    await message.channel.send(responce)

def getResponce(message): #TODO fix async issues, fix string parsing issues with discord text formatting
  print(str(message))
  responce2 = chatbot.get_chat_response(str(message), output="text"))
  responce2 = str(responce2)
  m = re.search(r"(?<=message).*?(?=conversation_id)", responce2).group(0)
  m  = m[4:]
  size = len(m)
  m = m[:size - 4]
  return m

client.run(token)
