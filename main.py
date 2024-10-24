import os
import asyncio

from custom_logger import Logger
logger = Logger('gwaff.main')

logger.info("Starting")

from warnings import filterwarnings
filterwarnings("ignore", category=RuntimeWarning, module="matplotlib\..*", lineno=0)
filterwarnings("ignore", category=UserWarning, module="matplotlib\..*", lineno=0)

logger.info("Filtering warnings")


from collector import collect
collect()
logger.info("Collecting")

from gwaff.bot.bot import run_the_bot

TOKEN = os.environ['BOT_TOKEN']
asyncio.run(run_the_bot(TOKEN))

logger.info("Fin!")
