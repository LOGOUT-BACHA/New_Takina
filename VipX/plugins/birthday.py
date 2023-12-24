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

@AdminActual
async def birthday(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
    await save_authuser(message.chat.id, token, assis)
    return await message.reply_text("**» ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴏɴ ᴜsᴇʀ ᴍᴇssᴀɢᴇ.**") 
            
WISH = [ '''
✧✧🔥🔥🔥🔥🔥✧✧
✧╭┻┻┻┻┻┻┻┻┻┻╮✧
✧┃╱╲ 🍓╱╲🍒 ╱╲┃✧
╭┻━🍒━━━🍍━━━┻╮
┃╱╲╱╲ 🍈╱╲🍇 ╱╲ ┃
🎁━━━━━━━━━━━━🎁
✨💕Happy Birthday💕✨''' ,
    '''
🌹🌹🌹🌹🌹🌹🌹
🌹✨✨🎀✨✨🌹
🌹🌟🎁🙆🎁🌟🌹
🌹🌟🎁💎🎁🌟🌹
🌹🌟🎁💖🎁🌟🌹
🌹 Happy bday🌹
🌹🌹🌹🌹🌹🌹🌹''' ,
@app.on_message(
    filters.command("wish")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(GALI),
        
    )


@app.on_message(
    filters.command("wish")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**𝐆𝐚𝐥𝐢 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐨𝐫𝐤 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 >> /gali 𝐂𝐨𝐦𝐦𝐚𝐧𝐝.**")        
