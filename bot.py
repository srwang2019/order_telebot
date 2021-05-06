import telebot
import config
import re
import datetime
import pytz
import json
import traceback
from telegram import ParseMode

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

# create bot with pyTelegramBotAPI library
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        text="Welcome! We hear that you are interested in a particular item in our [Weekend Live Shopping Telegram](t.me/liveakanekuji) group. \n\nDo circle the item(s) and send us a photo of it!",
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Contact Akane for any enquiries", url="t.me/akane_ayi89"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Direct me back to Weekend Live Channel", url="t.me/liveakanekuji"
        )
    )

    bot.send_message(
        message.chat.id,
        "You can control me by sending these commands: \n\n/start - kickstart the bot \n/exchange - exchange rates for different sized items \n/faq - frequently asked questions",
        reply_markup=keyboard
    )


@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Small items", callback_data="F"),
        telebot.types.InlineKeyboardButton("Large items", callback_data="J")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            "Full list (Both Small and Large)", callback_data="All")
    )

    bot.send_message(
        message.chat.id,
        "Click on the size of item of choice:",
        reply_markup=keyboard
    )


@bot.message_handler(commands=['faq'])
def faq_command(message):
    bot.send_message(
        message.chat.id,
        text="<i><b>1. Question: Is there a telebot for the PO & Instock Channel?</b></i> \nThere are currently no telebots for this channel \U0001F927" +
        "\n\n<i><b>2. Question: Are there any other channels for anime products?</b></i> \nYes! Feel free to check out <a href='https://t.me/Akanekuji'>🐮 Akane's PO & Instock Channel 🐮</a>",
        parse_mode=ParseMode.HTML
    )


# time to bot !
# constantly request for getUpdates method
# none_stop parameter is responsible for polling to continue even if the API returns an error while executing the method
bot.polling(none_stop=True)
