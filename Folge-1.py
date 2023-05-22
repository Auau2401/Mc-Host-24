import disnake as discord
from disnake.ext import commands

client = commands.Bot(command_prefix=None, intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Der Bot ist fertig geladen und bereit!")
    await client.change_presence(activity=discord.Activity(name="auf eurem Server", type=discord.ActivityType.playing),
                                 status=discord.Status.dnd)


@client.slash_command(name="info", description="Dies ist ein Test Command")
async def info(interaction):
    embed = discord.Embed(title="Test", description="Test")
    await interaction.response.send_message("Hallo, ich bin ein Test Bot", embed=embed)


client.run("YOUR TOKEN HERE")
