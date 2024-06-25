import logging
import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, InlineQueryHandler, Updater

from commands import how_nitpicker, start
from inline_queries import inlinequery

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    updater = Updater(os.getenv("BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("hownitpicker", how_nitpicker))

    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
