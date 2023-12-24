from pyrogram import Client, filters
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

# Function to handle the "/afk" command
def set_afk(update, context):
    user = update.message.from_user
    context.user_data['afk'] = True
    update.message.reply_text(f"{message.from_user.mention} is now AFK.")

# Function to handle all incoming messages
def handle_messages(update, context):
    if 'afk' in context.user_data and context.user_data['afk']:
        user = update.message.from_user
        update.message.reply_text(f"Sorry, {message.from_user.mention} is currently AFK.")

# Function to handle the "/back" command
def set_back(update, context):
    user = update.message.from_user
    if 'afk' in context.user_data and context.user_data['afk']:
        del context.user_data['afk']
        update.message.reply_text(f"Welcome back, {message.from_user.mention}!")

# Create an instance of the Updater class
updater = Updater('YOUR_TELEGRAM_BOT_TOKEN', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler('afk', set_afk))
dispatcher.add_handler(CommandHandler('back', set_back))

# Register message handler
dispatcher.add_handler(MessageHandler(Filters.text, handle_messages))

# Start polling for updates from Telegram
updater.start_polling()
