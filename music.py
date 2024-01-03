import discord
from discord.ext import commands
import os, asyncio

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='hv', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')
TOKEN  = ''
async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())
