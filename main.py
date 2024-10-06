import discord
import asyncio
import os
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

phrases = [
    "« Le problème se situe entre la chaises et le clavier » ~ O.Perart",
    "« Bonjouuuuur » ~ O.Perart",
    "« Ordinatueur » ~ I.Muller",
    "« tata, tata, tata » ~ G.Younes",
    "« Je vais te frapper ! » ~ G.Younes",
    "« Je te mets une note complète » ~ G.Younes",
    "« Le problème se situe entre la chaises et le clavier » ~ Olivier Perart",
    "« Je te mets un 0 ! » ~ G.Younes",
    "« Est-ce qu’il y a un jeune qui peut effacer le tableau ? » ~ G.Younes",
    "« Ça c’est George, ça c’est George. PAM PAM » ~ G.Younes",
    "« Jeunesse » ~ G.Younes",

]

async def send_message_every_minute():
    await client.wait_until_ready()
    channel = client.get_channel(1291877797006151734)
    while not client.is_closed():
        if channel:
            message = random.choice(phrases)
            await channel.send(message)
            print(f"Message envoyé : {message}")
        else:
            print("Le canal n'a pas été trouvé !")

        await asyncio.sleep(10)  # en secondes

@client.event
async def on_ready():
    print(f'Bot connecté en tant que {client.user}')
    client.loop.create_task(send_message_every_minute())

client.run(TOKEN)
