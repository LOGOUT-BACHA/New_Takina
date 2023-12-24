
from VipX.ext import Updater, CommandHandler, MessageHandler, Filters

# AFK message handler
def afk_message(update, context):
    name = update.effective_user.first_name
    update.message.reply_text(f"Hello {name}, I'm currently not available. I'll get back to you soon.")

def main():
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register the AFK message handler
    dp.add_handler(MessageHandler(Filters.text, afk_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
