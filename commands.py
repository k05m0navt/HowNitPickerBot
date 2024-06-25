import secrets

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    response = "Welcome to HowNitPickerBot! 💨\n\nUse the /hownitpicker command to find out how nitpicker you are.\n\nEnjoy!"

    update.message.reply_text(response)


def how_nitpicker(update: Update, context: CallbackContext) -> None:
    """Send a random percentage of how nitpicker the user is."""
    user = update.effective_user.first_name
    percentage = secrets.randbelow(101)
    response = f"{user}, ты душнила на {percentage}% ! 💨"

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Share you nitpickness 💨", switch_inline_query="hownitpicker"
                )
            ]
        ]
    )

    update.message.reply_text(response, reply_markup=keyboard)
