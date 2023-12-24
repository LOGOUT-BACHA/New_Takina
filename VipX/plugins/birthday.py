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

WISH = [ '''
✧✧🔥🔥🔥🔥🔥✧✧
✧╭┻┻┻┻┻┻┻┻┻┻╮✧
✧┃╱╲ 🍓╱╲🍒 ╱╲┃✧
╭┻━🍒━━━🍍━━━┻╮
┃╱╲╱╲ 🍈╱╲🍇 ╱╲ ┃
🎁━━━━━━━━━━━━🎁
✨💕Happy Birthday💕✨''' ,

]


@app.on_message(
    filters.command("wish")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(WISH),
        
    )


@app.on_message(
    filters.command("wish")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**𝐖𝐢𝐬𝐡 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐨𝐫𝐤 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 >> /wish 𝐂𝐨𝐦𝐦𝐚𝐧𝐝.**")
