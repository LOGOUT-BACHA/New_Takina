import telebot

# Initialize your bot with the Telegram Bot Token
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

@app.message(filters.command("start"=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! How can I assist you?")

@app.message(filters.command("wish") lambda message: True)
def send_birthday_wish(message):
    if message.text.lower() == "/wish":
        bot.reply_to(message, "Happy birthday! 🎉🎂🎈")
    else:
        bot.reply_to(message, "Sorry, I don't understand that command. Type /wish to get a birthday wish!")

# Start the bot
bot.("Vipx")
