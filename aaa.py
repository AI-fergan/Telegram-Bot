from telegram.ext import Updater, MessageHandler, filters, ContextTypes, Application, CommandHandler
from telegram import Update
from hashlib import md5
import os

TOKEN = "7056541263:AAFRZLU5TMNRicql-urv0EEPzSxkWMB42G0"

def hash_image(path):
    pass

async def start_command(update, context):
    await update.message.reply_text("Welcome to the CybeRat image convertor to hash!")

def main():
    print("starts bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))

    print("starts polling...")
    app.run_polling()

if __name__ == '__main__':
    main()
