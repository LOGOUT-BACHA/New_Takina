import requests
import random
import os
import re
import asyncio
import time
from VipX import app
import string
from strings import get_command
from VipX.misc import SUDOERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Initialize your bot with the Telegram Bot Token
bot = VipX.VipX('YOUR_TELEGRAM_BOT_TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! How can I assist you?")

@bot.message_handler(func=lambda message: True)
def send_birthday_wish(message):
    if message.text.lower() == "/wish":
        bot.reply_to(message, "Happy birthday! 🎉🎂🎈")
    else:
        bot.reply_to(message, "Sorry, I don't understand that command. Type /wish to get a birthday wish!")

# Start the bot
bot.polling()
