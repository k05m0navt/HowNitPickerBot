import secrets
import uuid

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update,
)
from telegram.ext import CallbackContext


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    user = update.inline_query.from_user.first_name

    percentage = secrets.randbelow(101)
    response = f"{user}, ты душнила на {percentage}% ! 💨"
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Share you nitpickness 💨", switch_inline_query="")]]
    )

    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            thumb_url="https://i.imgur.com/hAtQR07.jpeg",
            title="How NitPicker you are ?",
            description="Find out how much of a nitpicker you are.",
            input_message_content=InputTextMessageContent(
                response,
            ),
            reply_markup=keyboard,
        )
    ]

    update.inline_query.answer(results, cache_time=0)
