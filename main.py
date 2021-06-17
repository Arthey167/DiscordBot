import discord
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "anxious", "miserable", "depressing"]

starter_encouragements = ["Cheer up!", "Hang in there!", "You are a great person!"]

# quotes api from zenquotes.io
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)

# login
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

#  don't print bot's messages, print user's messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$hello"):
        await message.channel.send("Hello!")

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.author == client.emojis:
        await message.channel.send("lol")

# client.run("~token~")