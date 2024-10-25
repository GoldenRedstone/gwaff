import discord
from discord import app_commands
from discord.ext import commands

from gwaff.custom_logger import Logger
from gwaff.bot.bot import GwaffBot

logger = Logger('gwaff.bot.github')

from gwaff.permissions import require_admin


class GithubCog(commands.GroupCog, group_name='github'):
    def __init__(self, bot: GwaffBot):
        self.bot = bot

        self.bot.schedule_task(
            self.upload,
            trigger="cron",
            hour=1,
            timezone="Australia/Brisbane",
            day='last'
        )

    async def upload(self):
        logger.info("Starting upload")
        if self.bot.logging_channel:
            await self.bot.logging_channel.send("Hello!")
        else:
            logger.warning(f"Could not find required channel")
        logger.info("Upload was not completed successfully")

    @app_commands.command(name="upload",
                          description="(Admin only) Upload the data to github")
    @require_admin
    async def command_upload(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await self.upload()
        await interaction.followup.send("No such luck")

    @app_commands.command(name="update",
                          description="(Admin only) Update the bot from github")
    @require_admin
    async def update(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        # logger.info("Starting update")
        await interaction.followup.send("No such luck")
        logger.warning("Update was not completed successfully")

    async def scheduled_upload(self):
        await self.upload()


async def setup(bot: GwaffBot):
    """
    Sets up the GithubCog and adds it to the bot.

    Args:
        bot (GwaffBot): The bot instance.
    """
    cog = GithubCog(bot)
    await bot.add_cog(cog, guilds=bot.guilds)
