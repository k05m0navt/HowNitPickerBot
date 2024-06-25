import secrets

from telegram import Update
from telegram.ext import CallbackContext


def how_nit_picker(update: Update, context: CallbackContext) -> None:
    """Send a random percentage of how nit picker the user is."""
    user = update.effective_user.first_name
    percentage = secrets.randbelow(101)
    response = f"{user}, ты душнила на {percentage}% ! 💨"
    update.message.reply_text(response)