import discord
import random
client = discord.Client()
prefix = "a!"

def r_color():
    hexa = "0123456789abcdef"
    random_hex = "0x"
    for l in range(6):
        random_hex += random.choice(hexa)
    return discord.Colour(int(random_hex, 16))

def create_embed(title, description, color, img=""):
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.color = color
    if(img != ""):
        embed.set_image(url=img)
    return embed


@client.event
async def on_ready():
    print("heya , im ready")


@client.event
async def on_message(message):
    print(message.content)

    if message.content.startswith(prefix + "del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()

    if message.content.startswith(prefix + "embed"):
        color = r_color()
        description = "Embed"
        embed = create_embed("Embed maker 1.0", description, color, message.author.avatar_url)

        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "invite"):
        invite = await message.channel.create_invite(unique= False)
        await message.channel.send(invite.url)

    if message.content.startswith(prefix + "d_invites"):
        invites = await message.guild.invites()
        for i in invites:
            await i.delete()

    if message.content.startswith(prefix + "fortnite"):
        await message.channel.send("https://fr.wikipedia.org/wiki/Fortnite")

    if message.content.startswith(prefix + "kick"):
        msg = message.content.split(" ")
        if len(msg) < 2:
            print("erreur nombre d'argument")
            return
        user = msg[1]
        reason = msg[2:]

        print(user[3:-1])

client.run(TOKEN)
