import os

from discord.ext import commands

from wbld.log import logger
from wbld.cogs.wbld import WbldCog

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIXES = ["./"]


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super(Bot, self).__init__(**kwargs)

    async def on_ready(self):
        logger.info("{} has connected to Discord!", self.user)
        logger.complete()


bot = Bot(
    command_prefix=PREFIXES,
    case_insensitive=True,
    description="A WLED firmware Discord bot.",
)


if __name__ == "__main__":
    if TOKEN:
        bot.add_cog(WbldCog(bot))
        bot.run(TOKEN)
    else:
        logger.error("Please set your DISCORD_TOKEN.")