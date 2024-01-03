import discord
from discord.ext import commands
import os, asyncio

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='hv', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')
TOKEN  = 'MTE3MzY2Mjg0MTI5MTY3MzY2Mg.Gx6S4Q.mAW_qXTvV0ZWWU76fFs33h4Bn_V9rnPGixjyZk'
async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())