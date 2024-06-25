import logging
import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater

from commands import how_nit_picker

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    updater = Updater(os.getenv("BOT_TOKEN"))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hownitpicker", how_nit_picker))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
